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
        return max(0, self.fuerza - enemigo.defensa)  #El max(0,...) sirve para que si da num negativos, este se deja en 0
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)
        print(self.nombre, 'ha realizado', daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)

class Guerrero (Personaje):
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    #Sobreescribir  imprimir atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print ("-Espada:", self.espada)

    #Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa

    #Escojer navaja
    def escoger_navaja(self):
        opcion = int(input("Escoger la navaja de la muerte:\n(1) Navaja Suiza, daño 10.\n (2) Navaja pioja, daño 6.\n>>>"))
        if (opcion == 1):
            self.espada = 10
        elif (opcion == 2):
            self.espada = 6
        else:
            print("Valor inválido, intente nuevamente")
            #Vuelva a ejecutar el método escoger_navaja
            self.escoger_navaja()
        

class Mago (Personaje):
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #Sobreescribir  imprimir atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print ("-Libro:", self.libro)

    #Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

    #Escojer navaja
    def escoger_libro(self):
        opcion = int(input("Escoger el libro de la sabidura:\n(1) El principito, daño 10.\n (2) Crepúsculo, daño 6.\n>>>"))
        if (opcion == 1):
            self.libro = 10
        elif (opcion == 2):
            self.libro = 6
        else:
            print("Valor inválido, intente nuevamente")
            #Vuelva a ejecutar el método escoger_navaja
            self.escoger_libro()

#Crear todos los objetos
persona = Personaje("Ángel Súarez", 20, 15, 10, 100)
arturoSuarez = Guerrero("Arturo Súarez", 20, 15, 10, 100, 5)
gandalf = Mago("Galdaf", 20, 15, 10, 100, 5)

#Atributos antes de la tragedia
print("Atrubutos antes: \n")
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()

#Ataque sin piedad
persona.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(persona)

#Atributos después de la tragedia
print("Atrubutos después: \n")
persona.imprimir_atributos()
arturoSuarez.imprimir_atributos()
gandalf.imprimir_atributos()



#arturoSuarez.escoger_navaja()
#arturoSuarez.imprimir_atributos()

# print("El valor de espada es: ", arturoSuarez.espada)

# variable del constructor 
# mi_personaje = Personaje("EsteBandido", 100, 50, 45, 100)
# mi_enemigo = Personaje("Angel", 70, 100, 40, 100 )
# mi_personaje.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)
# mi_personaje.subir_nivel(15, 5, 10)
# print("Valores actualizados")
# mi_personaje.imprimir_atributos()


#Modificando valores de los atributos





