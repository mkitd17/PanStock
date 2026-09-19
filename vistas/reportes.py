import tkinter as tk
from tkinter import ttk, messagebox


class VistaReportes:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        
        self.app.limpiar_contenedor()
        
        # Encabezado y Botón Volver
        frame_top = tk.Frame(self.parent, bg="#f4f6f9")
        frame_top.pack(fill="x", pady=(0, 15))
        
        lbl_titulo = tk.Label(
            frame_top, 
            text="📈 REPORTES Y CONSULTAS DE MOVIMIENTOS", 
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
        
        # 1. FILTROS
        frame_filtros = tk.LabelFrame(
            self.parent, 
            text=" Filtros de Consulta ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=15, 
            pady=15
        )
        frame_filtros.pack(fill="x", pady=(0, 15))
        
        tk.Label(frame_filtros, text="Fecha Desde:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.txt_desde = tk.Entry(frame_filtros, width=12, font=("Helvetica", 10))
        self.txt_desde.insert(0, "01/09/2026")
        self.txt_desde.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(frame_filtros, text="Fecha Hasta:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=0, column=2, sticky="w", pady=5)
        self.txt_hasta = tk.Entry(frame_filtros, width=12, font=("Helvetica", 10))
        self.txt_hasta.insert(0, "12/09/2026")
        self.txt_hasta.grid(row=0, column=3, padx=10, pady=5)
        
        tk.Label(frame_filtros, text="Categoría:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=1, column=0, sticky="w", py=5)
        self.cmb_cat = ttk.Combobox(
            frame_filtros, 
            values=["Todas", "Panadería", "Facturería", "Repostería"], 
            state="readonly", 
            width=18, 
            font=("Helvetica", 10)
        )
        self.cmb_cat.grid(row=1, column=1, padx=10, pady=5)
        self.cmb_cat.current(0)
        
        tk.Label(frame_filtros, text="Tipo Movimiento:", bg="#f4f6f9", font=("Helvetica", 10)).grid(row=1, column=2, sticky="w", py=5)
        self.cmb_tipo = ttk.Combobox(
            frame_filtros, 
            values=["Todos", "ENTRADA", "SALIDA"], 
            state="readonly", 
            width=15, 
            font=("Helvetica", 10)
        )
        self.cmb_tipo.grid(row=1, column=3, padx=10, pady=5)
        self.cmb_tipo.current(0)
        
        # Botonera
        frame_btn = tk.Frame(frame_filtros, bg="#f4f6f9")
        frame_btn.grid(row=2, column=0, columnspan=4, pady=10)
        
        btn_generar = tk.Button(frame_btn, text="🔍 Generar Reporte", bg="#e74c3c", fg="white", font=("Helvetica", 9, "bold"), width=16, relief="flat", cursor="hand2", command=self.generar_reporte)
        btn_generar.pack(side="left", padx=5)
        
        btn_exportar = tk.Button(frame_btn, text="🖨️ Exportar / Imprimir", bg="#34495e", fg="white", font=("Helvetica", 9, "bold"), width=16, relief="flat", cursor="hand2", command=self.exportar)
        btn_exportar.pack(side="left", padx=5)
        
        # 2. RESULTADOS
        frame_tabla = tk.LabelFrame(
            self.parent, 
            text=" Consolidado de Movimientos ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=10, 
            pady=10
        )
        frame_tabla.pack(fill="both", expand=True)
        
        columnas = ("fecha", "producto", "categoria", "tipo", "cantidad", "total")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        
        self.tabla.heading("fecha", text="Fecha")
        self.tabla.heading("producto", text="Producto")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("tipo", text="Tipo")
        self.tabla.heading("cantidad", text="Cantidad")
        self.tabla.heading("total", text="Monto Est. ($)")
        
        self.tabla.column("fecha", width=90, anchor="center")
        self.tabla.column("producto", width=180)
        self.tabla.column("categoria", width=110)
        self.tabla.column("tipo", width=90, anchor="center")
        self.tabla.column("cantidad", width=80, anchor="center")
        self.tabla.column("total", width=110, anchor="e")
        
        self.tabla.pack(fill="both", expand=True)
        
        self.generar_reporte()

    def generar_reporte(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
            
        datos = [
            ("11/09/2026", "Criollo de Hoja (Kg)", "Facturería", "SALIDA", 12, "$ 42,000.00"),
            ("12/09/2026", "Pan Francés (Kg)", "Panadería", "ENTRADA", 30, "$ 66,000.00"),
            ("12/09/2026", "Medialuna de Manteca", "Facturería", "SALIDA", 45, "$ 20,250.00")
        ]
        for item in datos:
            self.tabla.insert("", "end", values=item)

    def exportar(self):
        messagebox.showinfo("Reporte Exportado", "El reporte ha sido generado exitosamente.")