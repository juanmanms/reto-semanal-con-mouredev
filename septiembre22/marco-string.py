#
# Crea una función que reciba un texto y muestre cada palabra en una línea,
# formando un marco rectangular de asteriscos.
# - ¿Qué te parece el reto? Se vería así:
#   **********
#   * ¿Qué   *
#   * te     *
#   * parece *
#   * el     *
#   * reto?  *
#   **********


def pintarx (larga):
    larga = larga +4 
    for i in range(larga):
        print ("*", end="")
        continue
    print ("*")
    return

print ("-------------------------------------")
print ("-------------------------------------")
print ("Enmarca la siguiente frase, separando cada palabra en una linea")
print ("-------------------------------------")
print ("Introduce frase")
frase = input()
print ("-------------------------------------")
print ("-------------------------------------")
frase_separada = frase.split(' ')
larga = 0
for palabra in frase_separada:
    if len(palabra) > larga:
        larga = len(palabra)
        continue
    continue
pintarx (larga)
for palabra in frase_separada:
    print ("*" + palabra.center(larga+4) + "*")
    continue
pintarx (larga)





