 # Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 # - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 # - EXTRA: ¿Eres capaz de dibujar más figuras?

#definir globales
lados = []

#Pide el largo de cada lado --- pendiente de hacerlo
def medidas(nlados):
    print ("Introduce el largo de cada lado:")
    for i in range(nlados):
        print ("Lado " + str(i+1) + ":")
        lado=t_lado()
        lados.append(lado)
        continue
    return lados

#Pide el largo de lado
def t_lado():
    print ("Introduce el largo de un lado:")
    lado = int(input())
    return lado
    
    
#definir funcion que mande dibujar poligono segun lados.
def dibujar_poligono(nlados):
    if nlados == 1:
        print ("No se puede dibujar un poligono con un solo lado")
    if nlados == 2:
        print ("No se puede hacer un poligono de 2 lados")
    if nlados == 3:
        print ("Dibujar un triangulo")
        dibujar_triangulo(t_lado())
    if nlados == 4:
        print ("Dibujar un cuadrado")
        dibujar_cuadrado(t_lado())
    if nlados > 4:
        print ("Todavia no estoy preparado para dibujar poligonos de mas de 4 lados")

#definir funciones de dibujo de poligonos.

#dibujar triangulo con *
def dibujar_triangulo(t_lado):
    for linea1 in range(t_lado):
        for largo in range(linea1+1):
            while linea1+1-largo < t_lado:
                if largo < linea1+1-largo and largo <= 0:
                    print (" ", end="")
                linea1 += 1
            if linea1 >= largo:
                print ("*", end="")
            if largo < t_lado:
                print (" ", end="")
        print ("")
    return

#dibujar cuadrado con *
def dibujar_cuadrado(t_lado):
    for ladoa in range(t_lado):
        for ladob in range(t_lado):
            print ("*".center(3), end="")
        print ("")
    return

#ejecutar el program
print ("-------------------------------------")
print ("-------------------------------------")
print ("Programa que dibuja poligono de x lados")
print ("-------------------------------------")
print ("-------------------------------------")
print ("Introduce el numero de lados del poligono:")
nlados = int(input())
print ("-------------------------------------")
print ("-------------------------------------")
dibujar_poligono(nlados)
print ("-------------------------------------")
print ("-------------------------------------")
