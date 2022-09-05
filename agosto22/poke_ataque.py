import random
from tkinter import NoDefaultRoot
#
#Enunciado: Crea un programa que calcule el daño de un ataque durante
#una batalla Pokémon.
#- La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
#- Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
#- Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico 
#  (buscar su efectividad)
#- El programa recibe los siguientes parámetros:
# - Tipo del Pokémon atacante.
# - Tipo del Pokémon defensor.
# - Ataque: Entre 1 y 100.
# - Defensa: Entre 1 y 100.
#
tipo_pokemo = ['Agua', 'Fuego', 'Planta', 'Eléctrico']

def efectividad(at, de):
    if at==0 and de==1 or at==1 and de==2 or at==4 and de==0:
        return 2
    if at==1 and de==0 or at==2 and de==0 or at==2 and de==1 or at==3 and de==2 or at==0 and de==2 :
        return 0.5
    else:
        return 1

def tipo_efectividad(efec):
    if efec==2:
        print ("Súper efectivo")
    if efec==0.5:
        print("No es muy efectivo")
    else:
        print ("Ha sido un buen ataque")
    

def ramdom_pokemon_defensa():
    p_defensa=random.randrange(0,4, 1)
    print("---------------------------")
    print ("El ordenadro defendera con un pokemon tipo: "+ tipo_pokemo[p_defensa] )
    return p_defensa

def elige_pokemon_ataque():
    print("Elige tipo de pokemon con el que atacaras")
    print ("1. Agua")
    print ("2. Fuego")
    print ("3. Planta")
    print ("4. Eléctrico")
    p_ataque = (int(input())-1)
    print("---------------------------")
    print ("Has elegido un pokemon de tipo: "+ tipo_pokemo[p_ataque] )
    return p_ataque

def reaccion():
    return random.randrange(1,100, 1)

def pelea():
    print("---------------------------")
    at=elige_pokemon_ataque()
    de=ramdom_pokemon_defensa()
    print("Que comience la pelea")
    ataque=reaccion()
    defensa=reaccion()
    print("El ataque es de "+ str(ataque))
    print("La defensa es de "+ str(defensa))
    
    print("---------------------------")
    resultado = 50 * (ataque/defensa)*efectividad(at, de)
    tipo_efectividad(efectividad(at, de))
    print ("Has hecho un daño de :"+str(resultado))




#main
def main():
    print("Programa de atque pokemos")
    print("---------------------------")
    print("---------------------------")

    pelea()

if __name__ == "__main__":
    main()