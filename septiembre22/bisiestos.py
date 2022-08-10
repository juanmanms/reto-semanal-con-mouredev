# Crea una función que imprima los 30 próximos años bisiestos
# siguientes a uno dado.
# - Utiliza el menor número de líneas para resolver el ejercicio.


print ("-------------------------------------")
print ("-------------------------------------")
print ("Calcula los siguientes 30 años bisiestos:")
print ("-------------------------------------")
print ("Introduce un año desde el que quieras empezar:")
anyo = int(input())
bisiesto=0
while bisiesto < 30:
    if anyo % 4 == 0:
        bisiesto += 1
        print (str(anyo) + "--" + str(bisiesto) + "ºaño bisiesto")
    anyo += 1
print ("-------------------------------------")
print ("Fin del programa")
print ("-------------------------------------")

