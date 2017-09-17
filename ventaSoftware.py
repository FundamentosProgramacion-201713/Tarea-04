#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
"""
Este programa le indica al usuario el total a pagar por cierto número de paquetes de software, así como la cantidad
descontada (la segunda aplica sólo si se compran de diez piezas en adelante).
"""


#Se calcula el total bruto. A éste se le descuenta (o no) un porcentaje en función de la canditad de paquetes comprados.
def calcularTotalAPagar(purchasedPacks):
    totalBruto = (1500 * purchasedPacks)
    if purchasedPacks >= 100 :
        totalApagar = (totalBruto * 0.5)
    elif purchasedPacks >= 50 :
        totalApagar = (totalBruto * 0.6)
    elif purchasedPacks >= 20 :
        totalApagar = (totalBruto * 0.7)
    elif purchasedPacks >= 10 :
        totalApagar = (totalBruto * 0.8)
    else:
        totalApagar = totalBruto
    return totalApagar


#Se piden los paquetes comprados. Se imprimen total a pagar y cantidad descontada, o se imprime error si se introduce
# una cantidad inválida.
def main():
    purchasedPacks = int(input("¿Cuántos paquetes de software desea comprar? "))

    totalPagar = calcularTotalAPagar(purchasedPacks)
    amountSaved = (1500 * purchasedPacks) - totalPagar

    if purchasedPacks == 0 :
        print ("¿Está seguro de que no desea comprar ningún paquete?")
    elif purchasedPacks < 0 :
        print ("Ese número NO es válido.")
    else:
        print("------------")
        print("Por pagar: $", "%.2f" % (totalPagar))
        if amountSaved >= 10:
            print("Al comprar con nosotros, Ud. ha ahorrado $", "%.2f" % (amountSaved))


main()