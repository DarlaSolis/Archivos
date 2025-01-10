class Personaje:
    #Atributos de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = fuerza
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza 
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa += defensa
    
    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, 'ha realizado', daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)

# variable del constructor 
mi_personaje = Personaje("EsteBandido", 100, 50, 45, 100)
mi_enemigo = Personaje("Angel", 70, 100, 40, 100 )
mi_personaje.imprimir_atributos()
mi_personaje.atacar(mi_enemigo)
# mi_personaje.subir_nivel(15, 5, 10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()


#Modificando valores de los atributos





