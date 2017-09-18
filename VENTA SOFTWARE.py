#encoding: UTF-8
#Autor: Ana María López Soto
#Programa calcula el precio total y descuento de la compra de softwares


precioIncial = 1500

#calcula el descuento correspondiente por número de paquetes
def calcularDescuento(cantPaquetes):
    if cantPaquetes >= 10 and cantPaquetes <= 19:
        descuento = cantPaquetes * precioIncial * 0.2
    elif cantPaquetes >= 20 and cantPaquetes <= 49:
        descuento = cantPaquetes * precioIncial * 0.3
    elif cantPaquetes >= 50 and cantPaquetes <= 99:
        descuento = cantPaquetes * precioIncial * 0.4
    elif cantPaquetes >= 100:
        descuento = cantPaquetes * precioIncial * 0.5
    else:
        descuento = 0
    return descuento

#calcula el pago total con paquetes y descuento
def calcularPagoTotal(cantPaquetes,descuento):
    if cantPaquetes >= 1 and cantPaquetes <= 9:
        pagoTotal = cantPaquetes * precioIncial
    elif cantPaquetes >= 10 and cantPaquetes <= 19:
        pagoTotal = cantPaquetes * precioIncial - descuento
    elif cantPaquetes >= 20 and cantPaquetes <= 49:
        pagoTotal = cantPaquetes * precioIncial - descuento
    elif cantPaquetes >= 50 and cantPaquetes <= 99:
        pagoTotal = cantPaquetes * precioIncial - descuento
    elif cantPaquetes >= 100:
        pagoTotal = cantPaquetes * precioIncial - descuento
    else:
        pagoTotal = "x"
    return pagoTotal


#Leer cantidad de paquetes, calcular e imprimir.
def main ():
    cantPaquetes = int(input("Inserte la cantidad de paquetes que desea adquirir: "))
    descuento = calcularDescuento(cantPaquetes)
    pagoTotal = calcularPagoTotal(cantPaquetes,descuento)
    print("------------------------------------------")
    if pagoTotal == "x":
        print("Inserte número de paquetes mayor a 0 ")
    elif cantPaquetes <= 9:
        print("El total a pagar es: $%d" % (pagoTotal))
    else:
        print("Usted ahorró: $%d" % (descuento))
        print("El total a pagar es: $%d" % (pagoTotal))

main()