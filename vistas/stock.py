import tkinter as tk
from tkinter import ttk, messagebox


class VistaStock:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        
        self.app.limpiar_contenedor()
        
        # Encabezado y Botón Volver
        frame_top = tk.Frame(self.parent, bg="#f4f6f9")
        frame_top.pack(fill="x", pady=(0, 15))
        
        lbl_titulo = tk.Label(
            frame_top, 
            text="📋 CONTROL Y CONSULTA DE STOCK ACTUAL", 
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
        
        # 1. TARJETAS DE ESTADO
        frame_cards = tk.Frame(self.parent, bg="#f4f6f9")
        frame_cards.pack(fill="x", pady=(0, 15))
        
        card1 = tk.Frame(frame_cards, bg="#3498db", padx=15, pady=10, relief="flat")
        card1.pack(side="left", expand=True, fill="x", padx=10)
        
        tk.Label(card1, text="TOTAL PRODUCTOS", font=("Helvetica", 9, "bold"), fg="#ecf0f1", bg="#3498db").pack(anchor="w")
        tk.Label(card1, text="4 Ítems", font=("Helvetica", 16, "bold"), fg="white", bg="#3498db").pack(anchor="w")
        
        card2 = tk.Frame(frame_cards, bg="#e74c3c", padx=15, pady=10, relief="flat")
        card2.pack(side="left", expand=True, fill="x", padx=10)
        
        tk.Label(card2, text="ALERTA STOCK BAJO", font=("Helvetica", 9, "bold"), fg="#ecf0f1", bg="#e74c3c").pack(anchor="w")
        tk.Label(card2, text="2 Productos ⚠️", font=("Helvetica", 16, "bold"), fg="white", bg="#e74c3c").pack(anchor="w")
        
        # 2. FILTROS
        frame_filtros = tk.Frame(self.parent, bg="#f4f6f9")
        frame_filtros.pack(fill="x", pady=(0, 10))
        
        btn_todos = tk.Button(frame_filtros, text="Ver Todos los Productos", bg="#2980b9", fg="white", font=("Helvetica", 9, "bold"), relief="flat", cursor="hand2", command=self.cargar_todos)
        btn_todos.pack(side="left", padx=5)
        
        btn_bajos = tk.Button(frame_filtros, text="⚠️ Filtrar Solo Stock Bajo", bg="#c0392b", fg="white", font=("Helvetica", 9, "bold"), relief="flat", cursor="hand2", command=self.filtrar_stock_bajo)
        btn_bajos.pack(side="left", padx=5)
        
        # 3. TABLA
        frame_tabla = tk.LabelFrame(
            self.parent, 
            text=" Estado de Disponibilidad de Inventario ", 
            font=("Helvetica", 10, "bold"), 
            bg="#f4f6f9", 
            fg="#2c3e50", 
            padx=10, 
            pady=10
        )
        frame_tabla.pack(fill="both", expand=True)
        
        columnas = ("id", "producto", "categoria", "stock_actual", "stock_min", "estado")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings", height=8)
        
        self.tabla.heading("id", text="ID")
        self.tabla.heading("producto", text="Producto")
        self.tabla.heading("categoria", text="Categoría")
        self.tabla.heading("stock_actual", text="Stock Actual")
        self.tabla.heading("stock_min", text="Stock Mínimo")
        self.tabla.heading("estado", text="Estado")
        
        self.tabla.column("id", width=40, anchor="center")
        self.tabla.column("producto", width=200)
        self.tabla.column("categoria", width=120)
        self.tabla.column("stock_actual", width=100, anchor="center")
        self.tabla.column("stock_min", width=100, anchor="center")
        self.tabla.column("estado", width=110, anchor="center")
        
        self.tabla.pack(fill="both", expand=True)
        
        self.cargar_todos()

    def cargar_todos(self):
        self.limpiar_tabla()
        datos = [
            (1, "Pan Francés (Kg)", "Panadería", 18, 10, "OK"),
            (2, "Criollo de Hoja (Kg)", "Facturería", 3, 5, "⚠️ BAJO"),
            (3, "Medialuna de Manteca", "Facturería", 5, 20, "⚠️ BAJO"),
            (4, "Torta Selva Negra", "Repostería", 4, 2, "OK")
        ]
        for item in datos:
            self.tabla.insert("", "end", values=item)

    def filtrar_stock_bajo(self):
        self.limpiar_tabla()
        datos = [
            (2, "Criollo de Hoja (Kg)", "Facturería", 3, 5, "⚠️ BAJO"),
            (3, "Medialuna de Manteca", "Facturería", 5, 20, "⚠️ BAJO")
        ]
        for item in datos:
            self.tabla.insert("", "end", values=item)

    def limpiar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)