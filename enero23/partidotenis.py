##Crear partido de tenis

import random

puntuaciones =["0", "15", "30", "40", "Ventaja"]

def main():
    pj1 = 0
    pj2 = 0
    mostrado=False
    while pj1 <= 3 and pj2 <= 3:
        mostrado=False
        pj1, pj2 = jugar_punto(pj1, pj2)
        if pj1 == pj2:
            pj1, pj2, mostrado = deuce(pj1, pj2)
        else:
            mostrado = ventaja(pj1, pj2)
            if mostrado==True:
                jugar_punto(pj1, pj2)
                mostrar_puntuacion(pj1, pj2)
            else:
                mostrar_puntuacion(pj1, pj2)
        
    

def jugar_punto(pj1, pj2):
    if random.random() < 0.5:
        pj1 += 1
    else:
        pj2 += 1
    return pj1, pj2

def mostrar_puntuacion(pj1, pj2):
    if pj1 == 4:
        print("Gana el jugador 1")
    elif pj2 == 4:
        print("Gana el jugador 2")
    else:
        print("Puntuación: {} - {}".format(puntuaciones[pj1], puntuaciones[pj2]))

#si es deuce se imprime y se resta un punto a los dos
def deuce(pj1, pj2):
    if pj1 == 4 and pj2 == 4:
        pj1 -= 1
        pj2 -= 1
        print("Deuce")
    elif pj1 == 3 and pj2 == 3:
        print("Deuce")
    return pj1, pj2, True

def ventaja(pj1, pj2):
    if pj1 == 4 and pj2 == 3:
        print("Ventaja jugador 1")
        return True
    if pj2 == 4 and pj1 == 3:
        print("Ventaja jugador 2")
        return True
    return False

main()
