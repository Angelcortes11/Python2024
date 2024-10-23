import sqlite3

class Califi:

    def _init_(self, id_estudiante, id_materia, nota, fecha):
        self.id_estudiante = id_estudiante
        self.id_materia = id_materia
        self.nota = nota
        self.fecha = fecha

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