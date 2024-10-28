import sqlite3
from estudiante import Estudiante 
from profesor import Profesor
from materia import Materia
from calificacion import Calificacion

# Función para conectar la base de datos SQLite
def conectar_db():
        #crear conexion a la base de datos  llamada 'escolar.db'
        conn = sqlite3.connect ('escolar.db')
        return conn

# Función principal que ejecuta el programa 
def main():
    #Establece la conexión con la base de datos
    conn = conectar_db()
    # Crea un cursor para ejecutar consultas SQL
    cursor = conn.cursor()

    # Bucle infinito hasta que el usuario decida salir
    while True:
        print("\nSistema de Gestión Escolar")
        print("1. Agregar estudiante")
        print("2. Agregar profesor")
        print("3. Agregar materia" )
        print("4. Agregar calificación")
        print("5. Mostrar estudiantes")
        print("6. Mostrar profesores")
        print("7. Mostrar materias")
        print("8. Mostrar calificaciones")
        print("9. Salir")
        opcion = input("Seleccione una opcion: ")

        #Procesa la opción ingresada por el usuario
        if opcion == '1':
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            Estudiante.agregar(conn, nombre, edad)