#encoding: UTF-8
#Autor: Ángel Guillermo Ortiz González
#Matrícula: A01745998
#Descripción: Calcula la cantidad a pagar por un software con descuento dependiendo de la cantidad de paquetes comprados.

COSTO_PAQUETE = 1500

#calcula el descuento correspondiente por número de paquetes
def calcularDescuento(paquetes):
    if paquetes >= 10 and paquetes <= 19:
        descuento = paquetes * COSTO_PAQUETE * 0.2
    elif paquetes >= 20 and paquetes <= 49:
        descuento = paquetes * COSTO_PAQUETE * 0.3
    elif paquetes >= 50 and paquetes <= 99:
        descuento = paquetes * COSTO_PAQUETE * 0.4
    elif paquetes >= 100:
        descuento = paquetes * COSTO_PAQUETE * 0.5
    else:
        descuento = 0
    return descuento

#calcula el pago tomando en cuenta paquetes y descuento
def calcularPagoPorVenta(paquetes,descuento):
    if paquetes >= 1 and paquetes <= 9:
        total = paquetes * COSTO_PAQUETE
    elif paquetes >= 10 and paquetes <= 19:
        total = paquetes * COSTO_PAQUETE - descuento
    elif paquetes >= 20 and paquetes <= 49:
        total = paquetes * COSTO_PAQUETE - descuento
    elif paquetes >= 50 and paquetes <= 99:
        total = paquetes * COSTO_PAQUETE - descuento
    elif paquetes >= 100:
        total = paquetes * COSTO_PAQUETE - descuento
    else:
        total = 0
    return total

def main ():
    paquetes = int(input("Inserte el número de paquetes que desea: "))
    descuento = calcularDescuento(paquetes)
    total = calcularPagoPorVenta(paquetes,descuento)
    print("------------------------------------------")
    if total == 0:
        print("ERROR. Inserte número de paquetes válido.")
    elif paquetes <= 9:
        print("El total a pagar es: $%d" % (total))
    else:
        print("Usted ahorró: $%d" % (descuento))
        print("El total a pagar es: $%d" % (total))
main()