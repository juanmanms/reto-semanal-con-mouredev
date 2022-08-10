# Dado un listado de números, encuentra el SEGUNDO más grande.

# listado dado
numeros = [1, 2, 5, 4, 17, 17, 4, 15, 9, 10]
n1=0
n2=0
for numero in numeros:
    if numero > n1:
        n1 = numero

    if numero > n2 and numero < n1:
        n2 = numero
        continue
    continue
print ("El segundo numero más alto es: " + str(n2))
