import sqlite3

class Profesor:

    def _init_(self, dni_id, nombre, apellido, curso, estado, email):
        self.dni_id = dni_id
        self.nombre = nombre
        self.apellido = apellido
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