import sqlite3
from ClsEstudiante import Estudiante 
from ClsProfesor import Profesor
from ClsMateria import Materia
from ClsCalificacion import Calificacion

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
        elif opcion == '2':
            nombre = input ("Nombre del profesor: ")
            edad = input("Edad del profesor: ")
            Profesor.agregar(conn,nombre,edad)
        elif opcion == '3':
            nombre = input("Nombre de la materi:")
            Materia.agregar(conn, nombre)
        elif opcion == '4':
            id_estudiante = input("ID del estudiante")
            id_materia = input("ID de la materia: ")
            nota = input("Calificación: ")
            Calificacion.agregar(conn, id_estudiante, id_materia, nota)
        elif opcion == '5' : 
            Estudiante.mostrar_todos(conn)
        elif opcion == '6' :
            Profesor.mostrar_todos(conn)
        elif opcion == '7' :
            Materia.mostrar_todos(conn)
        elif opcion == '8' :
            Calificacion.mostrar_todos(conn)
        elif opcion == '9' :
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

    #Cierra la conexión a la base de datos al salir del programa
    conn.close()

#Punto de entrada del programa
if __name__ == "__main__":
    main()
