class Personaje : 
    #atributo de clase
    estado = True #vivo
    vida = 100 #cantidad de vida
    #constructor / atributo de instancia
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self .estado = Personaje.estado
        self. vida = Personaje.vida


def atacar (self, otro_personaje):
    if self.estado: #si está vivo
        danio = self.fuerza - (otro_personaje.resistencia)
        danio = max (0, danio) #evitar danio negativo
        print(f"{self.nombre} ataca a {otro_personaje.nombre} causando danio")
        otro_personaje.recibir_dano(danio) #llamando al metodo recibir dano y la cantidad es igual a danio
    else:
            print (f"{self.nombre} esta muerto y no puede atacar ")

# "cantidad" va a tomar el valor deL "danio"
def recibir_dano (self, cantidad):
    if self.estado:
        self.vida = self.vida - cantidad
        print(f"{self.nombre} recibe {cantidad} de danio. Vida restante es {self.vida} ")
        if self.vida <=0:
            self.vida = 0
            print(f"{self.nombre} ha muerto.")
    else:
        print(f"{self.nombre} ya esta muerto")

def mostrar_info(self):
    print

def estado (self):