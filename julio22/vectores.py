 # - Crea un programa que determine si dos vectores son ortogonales.
 # - Los dos array deben tener la misma longitud.
 # - Cada vector se podría representar como un array. Ejemplo: [1, -2]

def vector_ortogonal(vector1, vector2):
    x = 0
    for i in range(len(vector1)):
        escalar = vector1[i] * vector2[i]
        x = x + escalar
        
    if x == 0:
        return True
    else:
        return False

def introducir_vector(n):
    vector = []
    for i in range(n):
        print ("Introduce el valor " + str(i+1) + " del vector :")
        valor = int(input())
        vector.append(valor)
    print ("Fin del vector ")
    print ("----------------------------------------------------")
    return vector



def main():
    print ("----------------------------------------------------")
    print ("----------------------------------------------------")
    print ("Introduce el tamaño de los vectores que quieres comparar:")
    n = int(input())
    vector1 = introducir_vector(n)
    vector2 = introducir_vector(n)
    print ("Los vectores son ortogonales: " + str(vector_ortogonal(vector1, vector2)))
    
if __name__ == "__main__":
    main()