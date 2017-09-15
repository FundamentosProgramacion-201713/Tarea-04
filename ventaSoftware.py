#UTF-8
#Autor: Natalia Meraz Tostado          A01745008
#Descripción: lee los paquetes comprados e imprime una cantidad descontada y el total a pagar

def calcularDescuento(paquete):                         #calcula el descuento dependiendo la cantidad de paquetes
    if (paquete>=0) and (paquete<=9):
        descuento = 0
        return descuento
    if (paquete>=10) and (paquete<=19):
        descuento = (1500 * paquete) * .20
        return descuento
    elif (paquete>=20) and (paquete<=49):
        descuento = (1500 * paquete) * .30
        return descuento
    elif (paquete>=50) and (paquete<=99):
        descuento = (1500 * paquete) * .40
        return descuento
    elif (paquete>=100):
        descuento = (1500 * paquete) * .50
        return descuento
    return "Error"

def calcularTotal(paquete, descuento):                  #calcula el total a pagar tomando en cuenta el descuento
    total = (1500 * paquete) - descuento
    return total

def main():
    paquete = int(input("Paquetes comprados: "))
    descuento = calcularDescuento(paquete)
    print("El descuento es de $", calcularDescuento(paquete))
    print("El total a pagar es de $", calcularTotal(paquete, descuento))

main()