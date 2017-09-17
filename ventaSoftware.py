#encoding: UTF-8
#Autor: Daniel Sahuer
#programa que calcula un descuento de acuerdo al número de paquetes de software comprados


def calcularPrecioPaquetes(numPaquetes): #Calcula precio de los paquetes sin descuento
    precio = numPaquetes * 1500
    return precio


def calcularDescuento(p): #Calcula porcentaje de descuento
    if p >= 10 and p <= 19:
        desc = 20
    elif p >= 20 and p <= 49:
        desc = 30
    elif p >= 50 and p <= 99:
        desc = 40
    elif p >= 100:
        desc = 50
    else:
        desc = False
    return desc #Regresa


def calcularPrecioTotal(precio, descuento): #Calcula total a pagar
    totalDescuento = precio * (descuento/100)
    total = precio - totalDescuento
    return total #Regresa


def main():
    numPaquetes = int(input("Escribe el número de paquetes comprados: "))

    precioPaquetes = calcularPrecioPaquetes(numPaquetes)
    descuento = calcularDescuento(numPaquetes)

    if numPaquetes >=0 and numPaquetes<= 9:
        print("\nNo hay descuento\nTotal a pagar: $",precioPaquetes)

    elif numPaquetes >=10:
        precioTotal = calcularPrecioTotal(precioPaquetes, descuento)
        print("\nDescuento en porcentaje: %d\nCantidad a pagar: $ %.2f" % (descuento, precioTotal))

    else:
        print("Error")


main()