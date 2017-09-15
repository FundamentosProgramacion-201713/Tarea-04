#Autor: Joaquin Rios Corvera A01375441
#Encoding: UTF-8

#Este programa calcula el descuento de una compra y el precio total

#Esta función calcula el descuento aplicado
def calcularDescuento(cantidad):
    if cantidad < 10:
        descuento = 0
    elif cantidad < 20:
        descuento = 0.2
    elif cantidad < 50:
        descuento = 0.3
    elif cantidad < 100:
        descuento = 0.4
    else:
        descuento = 0.5
    return descuento

#Esta función calcula el precio que se descuenta
def calcularDescontado(cantidad, descuento):
    descontado = cantidad * 1500 * descuento
    return descontado

#Esta función calcula el total a pagar
def calcularTotal(cantidad, descontado):
    total = cantidad * 1500 - descontado
    return total

def main():
    cantidad = int(input("Teclea el número de paquetes comprados: "))

    if cantidad < 0:
        print("La cantidad no puede ser negativa.")
    else:
        descuento = calcularDescuento(cantidad)
        descontado = calcularDescontado(cantidad, descuento)
        total = calcularTotal(cantidad, descontado)

        print("Cantidad descontada: $%.2f" %descontado)
        print("Total a pagar: $%.2f" %total)

main()