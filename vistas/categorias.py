import tkinter as tk
from tkinter import ttk, messagebox


class VistaCategorias:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        
        self.app.limpiar_contenedor()
        
        # Encabezado y Botón Volver
        frame_top = tk.Frame(self.parent, bg="#f4f6f9")
        frame_top.pack(fill="x", pady=(0, 15))
        
        lbl_titulo = tk.Label(
            frame_top, 
            text="🏷️ GESTIÓN DE CATEGORÍAS (ABM)", 
            font=("Helvetica", 14, "bold"), 
            fg="#2c3e50", 
            bg="#f4f6f9"
        )
        lbl_titulo.pack(side="left")
        
        btn_volver = tk.Button(
            frame_top, 
            text="⬅️ Volver al Menú", 
            font=("Helvetica", 10, "bold"), 
            fg="white", 
            bg="#7f8c8d", 
            relief="flat", 
            cursor="hand2", 
            command=self.app.mostrar_menu_principal
        )
        btn_volver.pack(side="right")
        
        # 1. FORMULARIO DE CARGA
        frame_form = tk.LabelFrame(
            self.parent, 
            text=" Datos de la Categoría ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=15, 
            pady=15
        )
        frame_form.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame_form, text="Nombre:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.txt_nombre = tk.Entry(frame_form, width=30, font=("Helvetica", 10))
        self.txt_nombre.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Descripción:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.txt_descripcion = tk.Entry(frame_form, width=45, font=("Helvetica", 10))
        self.txt_descripcion.grid(row=1, column=1, padx=10, pady=5)
        
        # Botonera
        frame_botones = tk.Frame(frame_form, bg="#f4f6f9")
        frame_botones.grid(row=2, column=0, columnspan=2, pady=15)
        
        btn_guardar = tk.Button(frame_botones, text="💾 Agregar", bg="#2ecc71", fg="white", font=("Helvetica", 9, "bold"), width=12, relief="flat", cursor="hand2", command=self.guardar)
        btn_guardar.pack(side="left", padx=5)
        
        btn_modificar = tk.Button(frame_botones, text="✏️ Modificar", bg="#f39c12", fg="white", font=("Helvetica", 9, "bold"), width=12, relief="flat", cursor="hand2", command=self.modificar)
        btn_modificar.pack(side="left", padx=5)
        
        btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", bg="#e74c3c", fg="white", font=("Helvetica", 9, "bold"), width=12, relief="flat", cursor="hand2", command=self.eliminar)
        btn_eliminar.pack(side="left", padx=5)
        
        btn_limpiar = tk.Button(frame_botones, text="🧹 Limpiar", bg="#95a5a6", fg="white", font=("Helvetica", 9, "bold"), width=12, relief="flat", cursor="hand2", command=self.limpiar)
        btn_limpiar.pack(side="left", padx=5)
        
        # 2. TABLA DE CATEGORÍAS
        frame_tabla = tk.LabelFrame(
            self.parent, 
            text=" Categorías Registradas ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=10, 
            pady=10
        )
        frame_tabla.pack(fill="both", expand=True)
        
        columnas = ("id", "nombre", "descripcion")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre Categoría")
        self.tabla.heading("descripcion", text="Descripción")
        
        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("nombre", width=180)
        self.tabla.column("descripcion", width=350)
        
        self.tabla.pack(fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_registro)
        
        self.cargar_datos_ejemplo()

    def cargar_datos_ejemplo(self):
        datos = [
            (1, "Panadería", "Variedades de panes tradicionales y artesanales"),
            (2, "Facturería", "Facturas, criollos, medialunas y hojaldres"),
            (3, "Repostería", "Tortas, tartas dulces, postres y masitas")
        ]
        for item in datos:
            self.tabla.insert("", "end", values=item)

    def seleccionar_registro(self, event):
        item_sel = self.tabla.selection()
        if item_sel:
            valores = self.tabla.item(item_sel[0], "values")
            self.limpiar()
            self.txt_nombre.insert(0, valores[1])
            self.txt_descripcion.insert(0, valores[2])

    def guardar(self):
        if not self.txt_nombre.get():
            messagebox.showwarning("Advertencia", "Ingrese el nombre de la categoría.")
            return
        messagebox.showinfo("Éxito", f"Categoría '{self.txt_nombre.get()}' guardada con éxito.")
        self.limpiar()

    def modificar(self):
        if not self.tabla.selection():
            messagebox.showwarning("Advertencia", "Seleccione una categoría para modificar.")
            return
        messagebox.showinfo("Éxito", "Categoría modificada con éxito.")
        self.limpiar()

    def eliminar(self):
        if not self.tabla.selection():
            messagebox.showwarning("Advertencia", "Seleccione una categoría para eliminar.")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar la categoría seleccionada?")
        if confirmar:
            messagebox.showinfo("Éxito", "Categoría eliminada con éxito.")
            self.limpiar()

    def limpiar(self):
        self.txt_nombre.delete(0, tk.END)
        self.txt_descripcion.delete(0, tk.END)