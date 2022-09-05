# Simula el funcionamiento de una máquina expendedora creando una operación
# que reciba dinero (array de monedas) y un número que indique la selección
# del producto.
# - El programa retornará el nombre del producto y un array con el dinero
#   de vuelta (con el menor número de monedas).
# - Si el dinero es insuficiente o el número de producto no existe,
#   deberá indicarse con un mensaje y retornar todas las monedas.
# - Si no hay dinero de vuelta, el array se retornará vacío.
# - Para que resulte más simple, trabajaremos en céntimos con monedas
#   de 5, 10, 50, 100 y 200.
# - Debemos controlar que las monedas enviadas estén dentro de las soportadas.

#definir globales
monedas = [
    {'cantidad': 0, 'valor': 5},
    {'cantidad': 0, 'valor': 10},
    {'cantidad': 0, 'valor': 50},
    {'cantidad': 0, 'valor': 100},
    {'cantidad': 0, 'valor': 200}
]

##definir ingreso de monedas
def ingreso_monedas():
    print ("Introduce el valor de las monedas:")
    for moneda in monedas:
        print ("Moneda de " + str(moneda['valor']) + ":")
        moneda['cantidad'] = int(input())
    return monedas

#Obtener valor de monedas
def obtener_valor_monedas(monedas):
    valor = 0
    for moneda in monedas:
        valor = moneda['valor'] * moneda['cantidad'] + valor
    return valor

#Definir extraccion de monedas
def extraccion_monedas(valor):
    for moneda in monedas:
        if moneda['valor'] == valor:
            moneda['cantidad'] = moneda['cantidad'] - 1
            return moneda['cantidad']
    extracto_cuenta()
    return 0


#Definir extracto de cuenta
def extracto_cuenta():
    print ("Extracto de cuenta:")
    for moneda in monedas:
        print (str(moneda['cantidad']) + " monedas de " + str(moneda['valor']))
    return


#definir funcion principal
def main():
    print ("Bienvenido a la expendedora")
    print ("Selecciona el producto:")
    ingreso_monedas()
    extracto_cuenta()
    print (obtener_valor_monedas(monedas))

    # print ("1. Cerveza")
    # print ("2. Vino")
    # print ("3. Agua")
    # print ("4. Salir")1
    # producto = int(input())
    # if producto == 1:
    #     print ("Seleccionaste cerveza")
    #     valor = 200
    # elif producto == 2:
    #     print ("Seleccionaste vino")
    #     valor = 100
    # elif producto == 3:
    #     print ("Seleccionaste agua")
    #     valor = 50
    # elif producto == 4:
    #     print ("Gracias por usar la expendedora")
    #     return
    # else:
    #     print ("Producto no disponible")
    #     return
    # monedas = ingreso_monedas()
    # print ("Introduce el valor a pagar:")
    # valor_pagar = int(input())
    # if valor_pagar < valor:
    #     print ("No se puede pagar el producto")
    #     return
    # while valor_pagar > valor:
    #     if extraccion_monedas(valor) == 0:
    #         print ("No se puede pagar el producto")
    #         return
    #     valor_pagar = valor_pagar - valor
    # print ("Producto seleccionado")
    # extracto_cuenta()
    return

if __name__ == "__main__":
    main()