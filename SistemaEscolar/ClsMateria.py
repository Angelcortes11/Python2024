import sqlite3

class Materia:

    def _init_(self, id_materia, nombre, curso, descripcion, horario):
        self.id_materia = id_materia
        self.nombre = nombre        
        self.curso = curso
        self.descripcion = descripcion
        self.horario = horario

    def guardar(self):

        conn = sqlite3.connect('escolar.db')
        c = conn.cursor()

        c.execute('INSERT INTO Materias (nombre, edad, anho_id) VALUES (?, ?, ?)',
            (self.nombre, self.edad, self.anho_id))

        conn.commit()
        conn.close()

        @staticmethod
        def obtener_materia():
            conn = sqlite3.connect('escolar.db')
            c = conn.cursor()

            c.execute('SELECT * FROM Materias')

            materias = c.fetchall()
            conn.close()

            return Materia