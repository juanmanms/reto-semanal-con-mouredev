#listado de n numeros de la serie de fibonacci
def list_fibonaci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a, end=" ")

list_fibonaci(15)