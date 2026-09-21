-- ============================================================
-- PanStock - Sistema de Control de Stock para Panadería
-- Responsable: Ibañez, Mario Ricardo
-- Rol: Base de Datos / Modelo de datos
-- Motor objetivo: MySQL 8.0+
-- Datos de prueba: 2026
-- ============================================================

CREATE DATABASE IF NOT EXISTS panstock
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE panstock;

-- ------------------------------------------------------------
-- LIMPIEZA PARA PODER EJECUTAR EL SCRIPT NUEVAMENTE
-- ------------------------------------------------------------
DROP TABLE IF EXISTS movimientos;
DROP TABLE IF EXISTS productos;
DROP TABLE IF EXISTS categorias;

-- ------------------------------------------------------------
-- TABLA: categorias
-- ------------------------------------------------------------
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(150),
    CONSTRAINT uq_categorias_nombre UNIQUE (nombre)
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- TABLA: productos
-- ------------------------------------------------------------
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200),
    precio DECIMAL(10,2) NOT NULL,
    stock_minimo INT NOT NULL DEFAULT 5,
    id_categoria INT NOT NULL,

    CONSTRAINT chk_productos_precio
        CHECK (precio >= 0),
    CONSTRAINT chk_productos_stock_minimo
        CHECK (stock_minimo >= 0),
    CONSTRAINT fk_productos_categorias
        FOREIGN KEY (id_categoria)
        REFERENCES categorias(id_categoria)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- TABLA: movimientos
-- ------------------------------------------------------------
CREATE TABLE movimientos (
    id_movimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    tipo_movimiento VARCHAR(10) NOT NULL,
    cantidad INT NOT NULL,
    fecha DATETIME NOT NULL,
    observacion VARCHAR(200),

    CONSTRAINT chk_movimientos_tipo
        CHECK (tipo_movimiento IN ('ENTRADA', 'SALIDA')),
    CONSTRAINT chk_movimientos_cantidad
        CHECK (cantidad > 0),
    CONSTRAINT fk_movimientos_productos
        FOREIGN KEY (id_producto)
        REFERENCES productos(id_producto)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ------------------------------------------------------------
-- ROLES Y PERMISOS
-- ------------------------------------------------------------
CREATE ROLE IF NOT EXISTS 'rol_admin';
CREATE ROLE IF NOT EXISTS 'rol_operador';

-- Administrador: acceso total al esquema PanStock.
GRANT ALL PRIVILEGES ON panstock.* TO 'rol_admin';

-- Operador: lectura/escritura de productos y movimientos;
-- lectura de categorías.
GRANT SELECT, INSERT, UPDATE ON panstock.productos TO 'rol_operador';
GRANT SELECT, INSERT ON panstock.movimientos TO 'rol_operador';
GRANT SELECT ON panstock.categorias TO 'rol_operador';

-- ------------------------------------------------------------
-- DATOS DE PRUEBA - AÑO 2026
-- ------------------------------------------------------------
INSERT INTO categorias (nombre, descripcion) VALUES
('Panadería', 'Variedades de panes tradicionales y artesanales'),
('Facturería', 'Facturas, criollos, medialunas y hojaldres'),
('Repostería', 'Tortas, tartas dulces, postres y masitas');

INSERT INTO productos
(nombre, descripcion, precio, stock_minimo, id_categoria)
VALUES
('Pan Francés (Kg)', 'Pan tradicional tipo francés', 2200.00, 10, 1),
('Criollo de Hoja (Kg)', 'Criollos tradicionales con grasa', 3500.00, 5, 2),
('Medialuna de Manteca', 'Medialunas dulce de manteca', 450.00, 20, 2),
('Torta Selva Negra', 'Torta con crema y cerezas', 18000.00, 2, 3);

INSERT INTO movimientos
(id_producto, tipo_movimiento, cantidad, fecha, observacion)
VALUES
(1, 'ENTRADA', 30, '2026-09-10 07:00:00', 'Horneado producción mañana'),
(1, 'SALIDA', 12, '2026-09-10 10:30:00', 'Venta mostrador'),
(2, 'ENTRADA', 15, '2026-09-11 08:00:00', 'Producción diaria'),
(2, 'SALIDA', 12, '2026-09-11 12:00:00', 'Venta mostrador'),
(3, 'ENTRADA', 50, '2026-09-12 06:30:00', 'Compra/Producción'),
(3, 'SALIDA', 45, '2026-09-12 18:00:00', 'Venta mostrador');

-- ------------------------------------------------------------
-- CONSULTA DE CONTROL: stock actual calculado por movimientos
-- ------------------------------------------------------------
SELECT
    p.id_producto,
    p.nombre,
    p.stock_minimo,
    COALESCE(SUM(
        CASE
            WHEN m.tipo_movimiento = 'ENTRADA' THEN m.cantidad
            WHEN m.tipo_movimiento = 'SALIDA' THEN -m.cantidad
            ELSE 0
        END
    ), 0) AS stock_actual,
    CASE
        WHEN COALESCE(SUM(
            CASE
                WHEN m.tipo_movimiento = 'ENTRADA' THEN m.cantidad
                WHEN m.tipo_movimiento = 'SALIDA' THEN -m.cantidad
                ELSE 0
            END
        ), 0) < p.stock_minimo
        THEN 'BAJO'
        ELSE 'OK'
    END AS estado_stock
FROM productos p
LEFT JOIN movimientos m
    ON p.id_producto = m.id_producto
GROUP BY p.id_producto, p.nombre, p.stock_minimo
ORDER BY p.id_producto;

-- ============================================================
-- FIN DEL SCRIPT
-- ============================================================
