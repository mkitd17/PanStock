import mysql.connector
from mysql.connector import Error

def conectar_bd():
    """
    Establece y retorna la conexión con la base de datos MySQL 'panstock'.
    Maneja las excepciones ante errores de conexión.
    """
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            database="panstock",
            user="root",          # Cambiar según tu usuario configurado
            password=""           # Cambiar según tu contraseña configurada
        )
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def ejecutar_consulta(query, parametros=None, es_lectura=True):
    """
    Ejecuta consultas SQL (SELECT, INSERT, UPDATE, DELETE) 
    utilizando parámetros para prevenir inyección SQL.
    """
    conexion = conectar_bd()
    if not conexion:
        return None
    
    cursor = conexion.cursor(dictionary=True)
    try:
        if parametros:
            cursor.execute(query, parametros)
        else:
            cursor.execute(query)
            
        if es_lectura:
            resultado = cursor.fetchall()
            return resultado
        else:
            conexion.commit()
            return cursor.rowcount
    except Error as e:
        print(f"Error en la ejecución de la consulta: {e}")
        return None
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()