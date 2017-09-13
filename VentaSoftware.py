# encode UTF-8
# Autor: Luis Enrique Neri Pérez
# Descripción: 	Programa que lee el	número de paquetes comprados y despliega la	cantidad descontada	(si	la	hay) y el total	a pagar de la compra

def validarNumeroPaquetes(numeroPaquetes): #Función que valida si el número leido es positivo
    if numeroPaquetes >= 0:
        return numeroPaquetes
    else:
        return "ERROR: Dígite únicamente números positivos"


def calcularSubtotal(numeroPaquetes): #Función que calcula el subtotal de la compra
    precio = float(numeroPaquetes * 1500)
    return precio


def calcularPorcentaje(numeroPaquetes): #Función que selecciona el porcentaje que tendrá de descuento
    if  10> numeroPaquetes:
        x= float(0)
        return x
    elif 10 <= numeroPaquetes <= 19:
        x = float(0.1)
        return x
    elif 20<= numeroPaquetes <= 49:
        x = float(0.3)
        return x
    elif 50<= numeroPaquetes <= 99:
        x = float(0.4)
        return x
    elif numeroPaquetes>= 100:
        x = float(0.5)
        return x
    else:
        pass


def calcularDescuento(precioPaquetes, porcentajeDescuento): #Función que calcula la cantidad monetaria descontada
    descuento = precioPaquetes * porcentajeDescuento
    return descuento


def calcularTotal(precioPaquetes, descuento): #Función que calcula el total de la compra
    total = precioPaquetes - descuento
    return total


def main(): #Función principal
    numeroPaquetes = int(input("Ingrese el número de paquetes adquiridos: "))
    paquetes = validarNumeroPaquetes(numeroPaquetes)
    if numeroPaquetes == paquetes:
        precioPaquetes = calcularSubtotal(numeroPaquetes)
        porcentajeDescuento = float(calcularPorcentaje(numeroPaquetes))
        descuento = calcularDescuento(precioPaquetes,porcentajeDescuento)
        total = calcularTotal(precioPaquetes,descuento)
        print("TICKET DE COMPRA")
        print("Paquetes Comprados:", numeroPaquetes)
        print("Precio Unitario: $1,500.00")
        print("Subtotal: $%.2f" % precioPaquetes)
        print("Descuento: -$%.2f" % descuento)
        print("-------------------")
        print("TOTAL: $%.2f" % total)

    else:
        print(paquetes)


main()