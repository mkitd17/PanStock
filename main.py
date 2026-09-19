import tkinter as tk
from tkinter import ttk, messagebox

# Importación de las vistas
from vistas.productos import VistaProductos
from vistas.categorias import VistaCategorias
from vistas.movimientos import VistaMovimientos
from vistas.stock import VistaStock
from vistas.reportes import VistaReportes


class AplicacionPanStock(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("PanStock - Sistema de Control de Stock para Panadería")
        self.geometry("950x650")
        self.minsize(850, 550)
        self.config(bg="#f4f6f9")
        
        # Centrar la ventana en la pantalla
        self.eval('tk::PlaceWindow . center')
        
        # Encabezado Institucional
        self.crear_encabezado()
        
        # Contenedor dinámico principal
        self.contenedor = tk.Frame(self, bg="#f4f6f9")
        self.contenedor.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Pie de página / Barra de estado
        self.crear_pie_pagina()
        
        # Iniciar en el Menú Principal
        self.mostrar_menu_principal()

    def crear_encabezado(self):
        frame_header = tk.Frame(self, bg="#2c3e50", height=70)
        frame_header.pack(fill="x", side="top")
        
        titulo = tk.Label(
            frame_header, 
            text="🍞 PanStock — Panadería Artesanal", 
            font=("Helvetica", 18, "bold"), 
            fg="white", 
            bg="#2c3e50"
        )
        titulo.pack(side="left", padx=20, pady=15)
        
        subtitulo = tk.Label(
            frame_header, 
            text="Control de Stock e Inventario", 
            font=("Helvetica", 11, "italic"), 
            fg="#bdc3c7", 
            bg="#2c3e50"
        )
        subtitulo.pack(side="right", padx=20, pady=20)

    def crear_pie_pagina(self):
        frame_footer = tk.Frame(self, bg="#ecf0f1", height=30)
        frame_footer.pack(fill="x", side="bottom")
        
        info = tk.Label(
            frame_footer, 
            text="Módulo Programador ISPC 2026 | Sistema de Gestión PanStock v1.0", 
            font=("Helvetica", 9), 
            fg="#7f8c8d", 
            bg="#ecf0f1"
        )
        info.pack(side="left", padx=15, pady=5)

    def limpiar_contenedor(self):
        for widget in self.contenedor.winfo_children():
            widget.destroy()

    def mostrar_menu_principal(self):
        self.limpiar_contenedor()
        
        # Título del menú
        lbl_titulo = tk.Label(
            self.contenedor, 
            text="MENÚ PRINCIPAL DE GESTIÓN", 
            font=("Helvetica", 16, "bold"), 
            fg="#2c3e50", 
            bg="#f4f6f9"
        )
        lbl_titulo.pack(pady=(10, 30))
        
        # Grid de Botones
        frame_grid = tk.Frame(self.contenedor, bg="#f4f6f9")
        frame_grid.pack(expand=True)
        
        botones = [
            ("📦 Productos", "#3498db", lambda: VistaProductos(self.contenedor, self)),
            ("🏷️ Categorías", "#9b59b6", lambda: VistaCategorias(self.contenedor, self)),
            ("📊 Movimientos", "#e67e22", lambda: VistaMovimientos(self.contenedor, self)),
            ("📋 Stock Actual", "#2ecc71", lambda: VistaStock(self.contenedor, self)),
            ("📈 Reportes y Consultas", "#e74c3c", lambda: VistaReportes(self.contenedor, self))
        ]
        
        # Posicionar botones en cuadrícula
        posiciones = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for i, (texto, color, comando) in enumerate(botones[:4]):
            r, c = posiciones[i]
            btn = tk.Button(
                frame_grid, text=texto, font=("Helvetica", 13, "bold"), fg="white", bg=color,
                width=22, height=3, relief="flat", cursor="hand2", command=comando
            )
            btn.grid(row=r, column=c, padx=15, pady=15)
        
        # Botón central de Reportes
        btn_reportes = tk.Button(
            frame_grid, text=botones[4][0], font=("Helvetica", 13, "bold"), fg="white", bg=botones[4][1],
            width=30, height=2, relief="flat", cursor="hand2", command=botones[4][2]
        )
        btn_reportes.grid(row=2, column=0, columnspan=2, pady=15)


if __name__ == "__main__":
    app = AplicacionPanStock()
    app.mainloop()