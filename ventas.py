#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785
#Programa para calcular el total a pagar dependiendo del número de paquetes introducidos

#Función para validar la entrada
def validarEntrada(num):
    return num >= 0

#Función para calcular el precio
def calcularPrecio(num):
    subtotal = 1500 * num
    if num >= 1 and num <= 9:
        descuento = 0
    elif num >= 10 and num <= 19:
        descuento = 20
    elif num >= 20 and num <= 49:
        descuento = 30
    elif num >= 50 and num <= 99:
        descuento = 40
    elif num >= 100:
        descuento = 50
    else:
        descuento = 0

    precio = subtotal * ((100-descuento)/100)
    return precio

def cantidadDescontada(precio, num):
    return (1500*num) - precio
def main():
    numPaquetes = int(input("Ingresa el número de paquetes: "))
    validacion = validarEntrada(numPaquetes)

    if validacion:

        precio = calcularPrecio(numPaquetes)
        descuento = cantidadDescontada(precio, numPaquetes)
        print("Descuento: ", "$", descuento, sep="")
        print("Total a pagar: ", "$", precio, sep="")
    else:
        print("Número inválido")

main()