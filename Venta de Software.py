#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Mátricula: A01376152
#Descripción: Sacar el total de una compra y hacer el respectivo descuento(Si lo hay)

#Calcula el subtotal a pagar

def calcularSubtotal(paquetes):
    subtotal = paquetes * 1500
    return subtotal


#Calcula el descuento de la compra(si lo hay)

def calcularDescuento(paquetes):
    subtotal= calcularSubtotal(paquetes)
    if paquetes>=10 and paquetes<=19:
        descuento= subtotal*.20
    elif paquetes>=20 and paquetes<=49:
        descuento= subtotal*.30
    elif paquetes>=50 and paquetes<=99:
        descuento= subtotal*.40
    elif paquetes>=100:
        descuento= subtotal*.50
    else:
        descuento=subtotal*0
    return descuento


#Calcula el total de la compra
def calcularTotal(paquetes):
    total=calcularSubtotal(paquetes)-calcularDescuento(paquetes)
    return total


#Función principal

def main():
    paquetes=int(input("Introduzca el número de paquetes comprados: "))
    print("")
    if paquetes<=0:
        print("¡Error!, inserte un número correcto.")
    else:
        print("El subtotal a pagar es: $ %.2f" %calcularSubtotal(paquetes))
        print("Descuesto de la compra: $ %.2f" %calcularDescuento(paquetes))
        print("El total a pagar por", paquetes, "paquetes es de: $ %.2f" %calcularTotal(paquetes))

main()