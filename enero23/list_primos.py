#listado de primos antes de llegar a n
def list_primos(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i, end=" ")

list_primos(100)