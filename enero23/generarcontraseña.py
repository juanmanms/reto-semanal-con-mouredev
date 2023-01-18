# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 #Podrás configurar generar contraseñas con los siguientes parámetros:
 #- Longitud: Entre 8 y 16.
 #- Con o sin letras mayúsculas.
 #- Con o sin números.
 #- Con o sin símbolos.
 #(Pudiendo combinar todos estos parámetros entre ellos)
 #

import random
import string

#main
def main():
    print("Generador de contraseñas")
    print ("========================")
    long = longitud()
    mayus = mayusculas()
    num = numeros()
    simb = simbolos()
    print("Tu contraseña es: {}".format(generar(long, mayus, num, simb)))


#Elegir longitud
def longitud():
    long = int(input("Introduce la longitud de la contraseña: "))
    if long < 8 or long > 16:
        print("Introduce una longitud entre 8 y 16")
        longitud()
    else:
        return long

#Elegir mayusculas
def mayusculas():
    mayus = input("¿Quieres mayusculas? (s/n): ")
    if mayus == "s":
        return True
    elif mayus == "n":
        return False
    else:
        print("Introduce una opción correcta")
        mayusculas()

#Elegir numeros
def numeros():
    num = input("¿Quieres numeros? (s/n): ")
    if num == "s":
        return True
    elif num == "n":
        return False
    else:
        print("Introduce una opción correcta")
        numeros()

#Elegir simbolos
def simbolos():
    simb = input("¿Quieres simbolos? (s/n): ")
    if simb == "s":
        return True
    elif simb == "n":
        return False
    else:
        print("Introduce una opción correcta")
        simbolos()

#Generar contraseña
def generar(long, mayus, num, simb):
    caracteres = string.ascii_lowercase
    if mayus == True:
        caracteres += string.ascii_uppercase
    if num == True:
        caracteres += string.digits
    if simb == True:
        caracteres += string.punctuation
    password = "".join(random.choice(caracteres) for i in range(long))
    return password

    


main()