#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139
#El programa lee el numero de paquetes comprados para sacar el total y hacer el respectivo descuento(Si lo hay.)

#Funcion que calcula el subtotal a pagar
def calcularSubtotal(paquetes):
    subtotal = paquetes * 1500
    return subtotal

#Funcion que calcula el descuento de la compra(si lo hay)
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

def main():
    paquetes=int(input("Numero de paquetes comprados: "))
    print("")
    if paquetes<=0:
        print("Error: Valor invalido.")
    else:
        print("El subtotal a pagar es: $ %.2f" %calcularSubtotal(paquetes))
        print("Descuesto de la compra: $ %.2f" %calcularDescuento(paquetes))
        print("El total a pagar por", paquetes, "paquetes es de: $ %.2f" %calcularTotal(paquetes))

main()