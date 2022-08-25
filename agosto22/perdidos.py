# Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule
# y retorne todos los que faltan entre el mayor y el menor.
# - Lanza un error si el array de entrada no es correcto.



numeros =[]
#Imprime numeros pedidos de la array
def pintar_perdidos(numeros):
    max_value = max(numeros)
    min_value = min(numeros)
    print("Los numeros perdidos son:")
    while min_value<max_value:
        min_value=min_value+1
        if min_value not in numeros:
            print(min_value)

#Introduce array ordenada y sin repetidos
def array_ordenada():
    print ("----------------------------------------------------")
    print ("Introduce numeros enteros ordenados y sin repetir, separados por comas")
    listado = input().split(',')
    try:
        listado = [int(i) for i in listado]
        estaOrdenado(listado)
        esRepetido(listado)
        pintar_perdidos(listado)
    except:
        print ("----------------------------------------------------")
        print("Oops!  Alguna de las normas no se cumple,")
    
    
#Hay repetido
def esRepetido(listado):
    if (len(listado) - len(set(listado))<=0):
        print ("Comprobación de repetidos ok")
    else:
        print ("Hay repetidos")
        print ("----------------------------------------------------")
        exit()
    



#Esta ordenado
def estaOrdenado(listado):
    if(all(listado[i] <= listado[i + 1] for i in range(len(listado)-1))):
        print ("Comprobación de orden ok")
    else:
        print ("No estan ordenados")
        print ("----------------------------------------------------")
        exit()

#introduce n enteros que forman array solicitada
def intarray(n):
    print ("Introduce números que compongan la array")
    while n > 0 :
        numeros.append(int(input()))
        print ("----------------------------------------------------")
        n=n-1
    print ("----------------------------------------------------")
    print ("----------------------------------------------------")
    pintar_perdidos(numeros)


def main():
   print ("----------------------------------------------------")
   print ("----------------------------------------------------")
   print ("Introduce el tamaño de la array a comprobar:")
   #n = int(input())
   print ("----------------------------------------------------")
   #intarray(n)
   array_ordenada()

if __name__ == "__main__":
   main()