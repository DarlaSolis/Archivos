class Personaje:
    #Atributos de la clase
    nombre = 'Default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

# variable del constructor vacio 
mi_personaje = Personaje()

print("El nombre de mi personaje es: ", mi_Personaje.nombre)
print("La fuerza de mi personaje es: ", mi_Personaje.fuerza)
print("La inteligencia personaje es: ", mi_Personaje.inteligencia)
print("La defensa personaje es: ", mi_Personaje.defensa)
print("La vida mi personaje es: ", mi_Personaje.vida)

#Modificando valores de los atributos
mi_Personaje.nombre = "EstebanDido"
mi_Personaje.defensa = 300
mi_Personaje.fuerza = 30
mi_Personaje.inteligencia = -2
mi_Personaje.vida = 2
