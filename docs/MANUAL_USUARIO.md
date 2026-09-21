# Manual de Usuario y Plan de Pruebas - PanStock

**Proyecto Integrador ABP - ISPC**  
**Carrera:** Tecnicatura Superior en Desarrollo de Software  
**Responsable:** Nicolás Sebastián Chumbita - Documentación y Pruebas  
**Año:** 2026

## 1. Introducción y alcance

PanStock permite administrar los productos de una panadería, registrar entradas y salidas y conocer el stock disponible. Esta guía describe el uso de las seis pantallas funcionales y los casos de prueba realizados.

## 2. Guía de uso y casos de prueba

### 2.1 Pantalla inicial - Menú principal

**Descripción:** muestra los accesos a Productos, Categorías, Movimientos, Stock actual y Reportes.

| Caso | Acción | Resultado esperado | Estado |
|---|---|---|---|
| CP-01 Navegación | Presionar cada opción del menú lateral. | La vista cambia correctamente sin abrir ventanas adicionales. | Aprobado |

### 2.2 Gestión de productos

**Descripción:** permite dar de alta, modificar, eliminar y consultar productos.

| Caso | Acción | Resultado esperado | Estado |
|---|---|---|---|
| CP-02 Alta de producto | Ingresar nombre, descripción, precio, stock mínimo y categoría; presionar **Guardar**. | Se muestra confirmación y el producto aparece en la tabla. | Aprobado |
| CP-03 Validación | Intentar guardar sin nombre o sin precio. | Se muestra un mensaje indicando el campo obligatorio. | Aprobado |
| CP-04 Modificación | Seleccionar una fila, editar un dato y presionar **Guardar**. | Se actualiza el registro seleccionado. | Aprobado |

### 2.3 Gestión de categorías

**Descripción:** administra las categorías disponibles en el selector de productos.

| Caso | Acción | Resultado esperado | Estado |
|---|---|---|---|
| CP-05 Alta de categoría | Ingresar nombre y descripción; presionar **Guardar categoría**. | La categoría se añade al listado y queda disponible en Productos. | Aprobado |

### 2.4 Registro de movimientos

**Descripción:** registra ingresos por compras o producción y salidas por ventas.

| Caso | Acción | Resultado esperado | Estado |
|---|---|---|---|
| CP-06 Entrada | Seleccionar producto, tipo ENTRADA, cantidad, fecha y observación. Presionar **Registrar movimiento**. | Se agrega el movimiento al historial. | Aprobado |
| CP-07 Salida sin stock | Intentar registrar una salida mayor que el stock disponible. | Se muestra una advertencia de stock insuficiente y no se registra la salida. | Aprobado |

### 2.5 Control de stock actual

**Descripción:** muestra stock disponible, mínimo configurado y estado de cada producto.

| Caso | Acción | Resultado esperado | Estado |
|---|---|---|---|
| CP-08 Indicador de mínimo | Consultar la tabla después de registrar movimientos. | Muestra **OK** si el stock alcanza el mínimo o **BAJO** si está por debajo. | Aprobado |
| CP-09 Filtro rápido | Presionar **Filtrar solo stock bajo**. | La tabla muestra solamente productos con estado BAJO. | Aprobado |

### 2.6 Reportes y consultas

**Descripción:** permite consultar movimientos históricos por rango de fechas y tipo.

| Caso | Acción | Resultado esperado | Estado |
|---|---|---|---|
| CP-10 Consulta filtrada | Elegir fechas entre 01/09/2026 y 12/09/2026, seleccionar tipo y presionar **Generar reporte**. | Se muestran únicamente los movimientos que cumplen los filtros. | Aprobado |

## 3. Conclusión de pruebas

Las pruebas funcionales realizadas sobre PanStock verifican la navegación, carga de datos, validaciones, movimientos, cálculo de stock y consultas. La versión 1.0 cumple los requisitos funcionales definidos para el prototipo.

## 4. Capturas requeridas

Las evidencias visuales se guardan en `docs/capturas/` con los siguientes nombres:

- `01_menu_principal.png`
- `02_productos.png`
- `03_categorias.png`
- `04_movimientos.png`
- `05_stock_actual.png`
- `06_reportes.png`
