 # Crea un función, que dado un año, indique el elemento 
 # y animal correspondiente en el ciclo sexagenario del zodíaco chino.

 #global variables

materiales = [ "madera", "fuego", "tierra", "metal", "agua"]
animales = [ "rata", "buey", "tigre","conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo"]

#function
def zodiaco(anyo):
    #igualamos anyo al 0
    anyo=anyo-4

    #obtenemos el resto de la division entre el anyo y 12 para saber animal
    animal = anyo % 12
    #obtenemos el resto de la division entre el anyo y 10 y lo partimos entre dos para saber elemento
    elemento = anyo % 10 / 2
    #imprimimos el animal y el elemento
    print (str(animal) + " -- " + str(int(elemento)))
    print ("El animal del ciclo sexagenario chino es: " + animales[animal])
    print ("El elmento del ciclo es  " + materiales[int(elemento)])
    return



#main
def main():
    print ("-------------------------------------")
    print ("------------------------------------")
    print ("Calcula el elemento y animal del ciclo sexagenario chino:")
    print ("-------------------------------------")
    print ("Introduce un año:")
    anyo = int(input())
    zodiaco(anyo)
    print ("-------------------------------------")
    print ("Fin del programa")
    print ("-------------------------------------")
    return

if __name__ == "__main__":
    main()


