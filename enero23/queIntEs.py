#funcion para introducir un numero entero
def entero():
    while True:
        try:
            num = int(input("Introduce un numero entero: "))
            break
        except ValueError:
            print("No es un numero entero")
    return num

#funcion para saber si un numero es primo
def primo(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
#funcion para saber si un numero es fibonacci
def fibonacci(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a + b
        if a == num:
            return True
    return False

#funcion para saber si un numero es par
def par(num):
    if num % 2 == 0:
        return True
    return False

#main
def main():
    num = entero()
    if primo(num):
        print("El numero es primo")
    else:
        print("El numero no es primo")
    if fibonacci(num):
        print("El numero es fibonacci")
    else:
        print("El numero no es fibonacci")
    if par(num):
        print("El numero es par")
    else:
        print("El numero es impar")

main()


