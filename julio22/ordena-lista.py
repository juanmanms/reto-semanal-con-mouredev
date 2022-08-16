 # Crea una función que ordene y retorne una matriz de números.
 # - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 #   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 #   o de mayor a menor.
 # - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 #   automáticamente.

def ordena (listado, orden):
    if orden == "Asc":
        for i in range(len(listado)):
            for j in range(len(listado)):
                if listado[i] < listado[j]:
                    aux = listado[i]
                    listado[i] = listado[j]
                    listado[j] = aux
                    continue
                continue
            continue
        return listado
    elif orden == "Desc":
        for i in range(len(listado)):
            for j in range(len(listado)):
                if listado[i] > listado[j]:
                    aux = listado[i]
                    listado[i] = listado[j]
                    listado[j] = aux
                    continue
                continue
            continue
        return listado
    else:
        return "El orden indicado no es correcto"


print ("-------------------------------------")
print ("-------------------------------------")
print ("Ordena un listado de números:")
print ("-------------------------------------")
print ("Introduce un listado de números separados por comas:")
listado = input().split(',')
listado = [int(i) for i in listado]
print ("-------------------------------------")
print ("-------------------------------------")
orden = input("Introduce el orden (Asc o Desc): ")
print ("-------------------------------------")
print ("-------------------------------------")
print ("Listado original: " + str(listado))
print ("-------------------------------------")
print ("-------------------------------------")
print ("Listado ordenado " + orden +": " + str(ordena(listado, orden)))
print ("-------------------------------------")
print ("-------------------------------------")
print ("Fin del programa")

