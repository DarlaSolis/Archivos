class Personaje:
    #Atributos de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def imprimir_atributos(self):
        print(self.__nombre)
        print("-Fuerza:", self.__fuerza)
        print("-Inteligencia:", self.__inteligencia)
        print("-Defensa:", self.__defensa)
        print("-Vida:", self.__vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza 
        self.inteligencia = self.inteligencia + inteligencia
        self.__defensa += defensa
    
    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        # if daño < 0:
        #    daño = 0
        # if enemigo.__vida - daño < 0:
        #     enemigo.__vida
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, 'ha realizado', daño, "puntos de daño a", enemigo.__nombre)
        print("Vida de", enemigo.__nombre, "es", enemigo.__vida)
    def get_vida(self):
        return self.__vida
    
    #asignamos a la variable vida, los datos que teniamos en self.__vida de la clase
    def set_vida(self, vida):
        self.__vida = vida
        if self.__vida == vida <= 0:
            self.morir()

# variable del constructor 
mi_personaje = Personaje("EsteBandido", 100, 50, 45, 100)
mi_enemigo = Personaje("Angel", 70, 100, 40, 100 )
#mi_personaje.vida
print(mi_personaje.get_vida())
mi_personaje.set_vida(-5)
mi_personaje._Personaje__vida = -50
print(mi_personaje.get_vida())
#mi_personaje.vida = 0
#mi_personaje.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)
# mi_personaje.subir_nivel(15, 5, 10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()


#Modificando valores de los atributos





