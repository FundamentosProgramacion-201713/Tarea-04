#encode: UTF-8
# Autor: David Ramírez Ríos; A01338802


#Calcula la cantidad a pagar en base al número de paqutes comprados
def calcularPago(cantidad):
    pago = cantidad * 1500

    if cantidad >= 10 and cantidad <=19:
        pago = cantidad * 1500 * .8
    elif cantidad >= 20 and cantidad <= 49:
        pago = cantidad * 1500 * .7
    elif cantidad >= 50 and cantidad <= 99:
        pago = cantidad * 1500 * .6
    elif cantidad >= 100:
        pago = cantidad * 1500 * .5

    return pago


def main ():
    cantidad = int (input("Escriba la cantidad de paquetes a comprar: "))
    if cantidad >= 0:
        pago = calcularPago(cantidad)
        print("El total a pagar es: $%.2f" % pago)
    else:
        print("Error: cantidad inválida.")

main()