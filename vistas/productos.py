import tkinter as tk
from tkinter import ttk, messagebox


class VistaProductos:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        
        self.app.limpiar_contenedor()
        
        # Título y Botón Volver
        frame_top = tk.Frame(self.parent, bg="#f4f6f9")
        frame_top.pack(fill="x", pady=(0, 15))
        
        lbl_titulo = tk.Label(
            frame_top, 
            text="📦 GESTIÓN DE PRODUCTOS (ABM)", 
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
            text=" Datos del Producto ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=15, 
            pady=15
        )
        frame_form.pack(fill="x", pady=(0, 15))
        
        # Campos de entrada
        tk.Label(frame_form, text="Nombre:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.txt_nombre = tk.Entry(frame_form, width=25, font=("Helvetica", 10))
        self.txt_nombre.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Precio ($):", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=0, column=2, sticky="w", pady=5)
        self.txt_precio = tk.Entry(frame_form, width=15, font=("Helvetica", 10))
        self.txt_precio.grid(row=0, column=3, padx=10, pady=5)
        
        tk.Label(frame_form, text="Descripción:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.txt_descripcion = tk.Entry(frame_form, width=25, font=("Helvetica", 10))
        self.txt_descripcion.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(frame_form, text="Stock Mínimo:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=1, column=2, sticky="w", pady=5)
        self.txt_stock_min = tk.Entry(frame_form, width=15, font=("Helvetica", 10))
        self.txt_stock_min.grid(row=1, column=3, padx=10, pady=5)
        
        tk.Label(frame_form, text="Categoría:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.cmb_categoria = ttk.Combobox(
            frame_form, 
            values=["Panadería", "Facturería", "Repostería"], 
            state="readonly", 
            width=23, 
            font=("Helvetica", 10)
        )
        self.cmb_categoria.grid(row=2, column=1, padx=10, pady=5)
        self.cmb_categoria.current(0)
        
        # Botonera de acciones
        frame_botones = tk.Frame(frame_form, bg="#f4f6f9")
        frame_botones.grid(row=3, column=0, columnspan=4, pady=15)
        
        btn_guardar = tk.Button(frame_botones, text="💾 Guardar", bg="#2ecc71", fg="white", font=("Helvetica", 9, "bold"), width=12, relief="flat", cursor="hand2", command=self.guardar)
        btn_guardar.pack(side="left", padx=5)
        
        btn_modificar = tk.Button(frame_botones, text="✏️ Modificar", bg="#f39c12", fg="white", font=("Helvetica", 9, "bold"), width=12, relief="flat", cursor="hand2", command=self.modificar)
        btn_modificar.pack(side="left", padx=5)
        
        btn_eliminar = tk.Button(frame_botones, text="🗑️ Eliminar", bg="#e74c3c", fg="white", font=("Helvetica", 9, "bold"), width=12, relief="flat", cursor="hand2", command=self.eliminar)
        btn_eliminar.pack(side="left", padx=5)
        
        btn_limpiar = tk.Button(frame_botones, text="🧹 Limpiar", bg="#95a5a6", fg="white", font=("Helvetica", 9, "bold"), width=12, relief="flat", cursor="hand2", command=self.limpiar)
        btn_limpiar.pack(side="left", padx=5)
        
        # 2. TABLA DE PRODUCTOS (Treeview)
        frame_tabla = tk.LabelFrame(
            self.parent, 
            text=" Productos Registrados ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=10, 
            pady=10
        )
        frame_tabla.pack(fill="both", expand=True)
        
        # Buscador
        frame_search = tk.Frame(frame_tabla, bg="#f4f6f9")
        frame_search.pack(fill="x", pady=(0, 10))
        
        tk.Label(frame_search, text="🔍 Buscar Producto:", bg="#f4f6f9", font=("Helvetica", 9, "bold")).pack(side="left", padx=5)
        self.txt_buscar = tk.Entry(frame_search, width=25, font=("Helvetica", 9))
        self.txt_buscar.pack(side="left", padx=5)
        
        # Tabla
        columnas = ("id", "nombre", "categoria", "precio", "stock_minimo")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("precio", text="Precio ($)")
        self.tabla.heading("stock_minimo", text="Stock Mínimo")
        
        self.tabla.column("id", width=40, anchor="center")
        self.tabla.column("nombre", width=200)
        self.tabla.column("categoria", width=120)
        self.tabla.column("precio", width=100, anchor="e")
        self.tabla.column("stock_minimo", width=100, anchor="center")
        
        self.tabla.pack(fill="both", expand=True)
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_registro)
        
        self.cargar_datos_ejemplo()

    def cargar_datos_ejemplo(self):
        datos = [
            (1, "Pan Francés (Kg)", "Panadería", 2200.00, 10),
            (2, "Criollo de Hoja (Kg)", "Facturería", 3500.00, 5),
            (3, "Medialuna de Manteca", "Facturería", 450.00, 20),
            (4, "Torta Selva Negra", "Repostería", 18000.00, 2)
        ]
        for item in datos:
            self.tabla.insert("", "end", values=item)

    def seleccionar_registro(self, event):
        item_sel = self.tabla.selection()
        if item_sel:
            valores = self.tabla.item(item_sel[0], "values")
            self.limpiar()
            self.txt_nombre.insert(0, valores[1])
            self.cmb_categoria.set(valores[2])
            self.txt_precio.insert(0, valores[3])
            self.txt_stock_min.insert(0, valores[4])

    def guardar(self):
        if not self.txt_nombre.get() or not self.txt_precio.get():
            messagebox.showwarning("Advertencia", "Por favor complete los campos obligatorios.")
            return
        messagebox.showinfo("Éxito", f"Producto '{self.txt_nombre.get()}' guardado correctamente.")
        self.limpiar()

    def modificar(self):
        if not self.tabla.selection():
            messagebox.showwarning("Advertencia", "Seleccione un producto de la tabla para modificar.")
            return
        messagebox.showinfo("Éxito", "Producto modificado correctamente.")
        self.limpiar()

    def eliminar(self):
        if not self.tabla.selection():
            messagebox.showwarning("Advertencia", "Seleccione un producto para eliminar.")
            return
        confirmar = messagebox.askyesno("Confirmar", "¿Está seguro de eliminar el producto seleccionado?")
        if confirmar:
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            self.limpiar()

    def limpiar(self):
        self.txt_nombre.delete(0, tk.END)
        self.txt_descripcion.delete(0, tk.END)
        self.txt_precio.delete(0, tk.END)
        self.txt_stock_min.delete(0, tk.END)
        self.cmb_categoria.current(0)