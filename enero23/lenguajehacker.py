
# Escribe un programa que reciba un texto y transforme lenguaje natural a
# "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  se caracteriza por sustituir caracteres alfanuméricos.
# - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#   con el alfabeto y los números en "leet".
#   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")

# - El programa debe recibir un texto y transformarlo a "leet".
# def leer texto
def  leer_texto ():
    texto =  input ( "Introduce un texto: " )
    return texto

# def transformar texto
def traducir_leet(texto):
    leet = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5",
        "t": "7",
        " ": "_",
    }
    for letra in texto:
        if letra in leet:
            texto = texto.replace(letra, leet[letra])
    return texto

# def imprimir texto
def imprimir_texto(texto):
    print (texto)

def main():
    texto = leer_texto()
    texto = traducir_leet(texto)
    imprimir_texto(texto)

main()
  

