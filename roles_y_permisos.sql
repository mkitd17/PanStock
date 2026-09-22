-- =========================================================
-- CONFIGURACIÓN DE ROLES Y PERMISOS - PANSTOCK
-- Autor: Francisco Benito Páez (Rol: Acceso a Datos)
-- =========================================================

-- 1. Creación de roles de usuario en el SGBD
CREATE ROLE IF NOT EXISTS rol_admin;
CREATE ROLE IF NOT EXISTS rol_operador;

-- 2. Asignación de permisos al Administrador (Acceso total)
GRANT ALL PRIVILEGES ON panstock.* TO rol_admin;

-- 3. Asignación de permisos al Operador (Lectura y Escritura operativa controlada)
GRANT SELECT, INSERT, UPDATE ON panstock.productos TO rol_operador;
GRANT SELECT, INSERT ON panstock.movimientos TO rol_operador;
GRANT SELECT ON panstock.categorias TO rol_operador;

-- Aplicar cambios de privilegios
FLUSH PRIVILEGES;