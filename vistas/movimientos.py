import tkinter as tk
from tkinter import ttk, messagebox


class VistaMovimientos:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        
        self.app.limpiar_contenedor()
        
        # Encabezado y Botón Volver
        frame_top = tk.Frame(self.parent, bg="#f4f6f9")
        frame_top.pack(fill="x", pady=(0, 15))
        
        lbl_titulo = tk.Label(
            frame_top, 
            text="📊 REGISTRO DE MOVIMIENTOS DE STOCK", 
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
        
        # 1. FORMULARIO DE MOVIMIENTO
        frame_form = tk.LabelFrame(
            self.parent, 
            text=" Registrar Entrada / Salida ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=15, 
            pady=15
        )
        frame_form.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame_form, text="Producto:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.cmb_producto = ttk.Combobox(
            frame_form, 
            values=["Pan Francés (Kg)", "Criollo de Hoja (Kg)", "Medialuna de Manteca", "Torta Selva Negra"], 
            state="readonly", 
            width=25, 
            font=("Helvetica", 10)
        )
        self.cmb_producto.grid(row=0, column=1, padx=10, pady=5)
        self.cmb_producto.current(0)
        
        tk.Label(frame_form, text="Tipo Movimiento:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=0, column=2, sticky="w", pady=5)
        self.cmb_tipo = ttk.Combobox(
            frame_form, 
            values=["ENTRADA", "SALIDA"], 
            state="readonly", 
            width=15, 
            font=("Helvetica", 10)
        )
        self.cmb_tipo.grid(row=0, column=3, padx=10, pady=5)
        self.cmb_tipo.current(0)
        
        tk.Label(frame_form, text="Cantidad:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.txt_cantidad = tk.Entry(frame_form, width=15, font=("Helvetica", 10))
        self.txt_cantidad.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        
        tk.Label(frame_form, text="Fecha:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=1, column=2, sticky="w", pady=5)
        self.txt_fecha = tk.Entry(frame_form, width=18, font=("Helvetica", 10))
        self.txt_fecha.insert(0, "12/09/2026")
        self.txt_fecha.grid(row=1, column=3, padx=10, pady=5)
        
        tk.Label(frame_form, text="Observación:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.txt_obs = tk.Entry(frame_form, width=50, font=("Helvetica", 10))
        self.txt_obs.grid(row=2, column=1, columnspan=3, padx=10, pady=5, sticky="w")
        self.txt_obs.insert(0, "Venta mostrador / Compra proveedor")
        
        # Botonera
        frame_botones = tk.Frame(frame_form, bg="#f4f6f9")
        frame_botones.grid(row=3, column=0, columnspan=4, pady=15)
        
        btn_registrar = tk.Button(frame_botones, text="✅ Registrar Movimiento", bg="#e67e22", fg="white", font=("Helvetica", 9, "bold"), width=20, relief="flat", cursor="hand2", command=self.registrar)
        btn_registrar.pack(side="left", padx=5)
        
        btn_limpiar = tk.Button(frame_botones, text="🧹 Limpiar Campos", bg="#95a5a6", fg="white", font=("Helvetica", 9, "bold"), width=15, relief="flat", cursor="hand2", command=self.limpiar)
        btn_limpiar.pack(side="left", padx=5)
        
        # 2. HISTORIAL DE MOVIMIENTOS
        frame_tabla = tk.LabelFrame(
            self.parent, 
            text=" Historial Reciente de Movimientos ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=10, 
            pady=10
        )
        frame_tabla.pack(fill="both", expand=True)
        
        columnas = ("id", "fecha", "producto", "tipo", "cantidad", "obs")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        
        self.tabla.heading("id", text="ID")
        self.tabla.heading("fecha", text="Fecha")
        self.tabla.heading("producto", text="Producto")
        self.tabla.heading("tipo", text="Tipo")
        self.tabla.heading("cantidad", text="Cantidad")
        self.tabla.heading("obs", text="Observaciones")
        
        self.tabla.column("id", width=40, anchor="center")
        self.tabla.column("fecha", width=90, anchor="center")
        self.tabla.column("producto", width=180)
        self.tabla.column("tipo", width=90, anchor="center")
        self.tabla.column("cantidad", width=80, anchor="center")
        self.tabla.column("obs", width=220)
        
        self.tabla.pack(fill="both", expand=True)
        
        self.cargar_datos_ejemplo()

    def cargar_datos_ejemplo(self):
        datos = [
            (101, "12/09/2026", "Pan Francés (Kg)", "ENTRADA", 30, "Horneado mañana"),
            (102, "12/09/2026", "Pan Francés (Kg)", "SALIDA", 12, "Venta mostrador"),
            (103, "11/09/2026", "Criollo de Hoja (Kg)", "ENTRADA", 15, "Producción diaria"),
            (104, "11/09/2026", "Medialuna de Manteca", "SALIDA", 45, "Venta mostrador")
        ]
        for item in datos:
            self.tabla.insert("", "end", values=item)

    def registrar(self):
        cant = self.txt_cantidad.get()
        if not cant or not cant.isdigit():
            messagebox.showwarning("Advertencia", "Ingrese una cantidad numérica válida mayor a 0.")
            return
            
        prod = self.cmb_producto.get()
        tipo = self.cmb_tipo.get()
        messagebox.showinfo("Éxito", f"Movimiento de {tipo} ({cant} u.) para '{prod}' registrado correctamente.")
        self.limpiar()

    def limpiar(self):
        self.txt_cantidad.delete(0, tk.END)
        self.cmb_producto.current(0)
        self.cmb_tipo.current(0)
        self.txt_obs.delete(0, tk.END)
        self.txt_obs.insert(0, "Venta mostrador / Compra proveedor")