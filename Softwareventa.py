# encoding-UTF-8
# AUTOR: José Antonio Vázquez Gabián
# Este programa calcula cuanto cuesta un paquete de software con su descuento
#esta funcion evalua el descuento de los paquetes
def saberDescuento(paquete):
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
def valorarTotal(paquete, descuento):                  #evalua el total con su descuento
        total = (1500 * paquete) - descuento
        return total
def main():
    paquete = int(input("Cual es la cantidad de paquetes comprados: "))
    descuento = saberDescuento(paquete)
    print("El descuento es de $", saberDescuento(paquete))
    print("El total a pagar es de $", valorarTotal(paquete, descuento))
main()