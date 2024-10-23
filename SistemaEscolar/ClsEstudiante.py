import sqlite3

class Estudiante:

    def _init_(self, legajo_id, dni_id, nombre, apellido, edad, fechadenacimiento, curso, estado, email):
        self.legajo_id = legajo_id
        self.dni_id = dni_id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fechadenacimiento = fechadenacimiento
        self.curso = curso
        self.estado = estado
        self.email = email

    def guardar(self):

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Estudiantes (nombre, edad, anho_id) VALUES (?, ?, ?)',
            (self.nombre, self.edad, self.anho_id))

        conn.commit()
        conn.close()

        @staticmethod
        def obtener_estudiantes():
            conn = sqlite3.connect('escolar.db')
            c = conn.cursor()

            c.execute('SELECT * FROM Estudiantes')

            estudiantes = c.fetchall()
            conn.close()

            return estudiantes 