#ecnoding: UTF-8
#Autor: Neftalí Rodríguez Martínez, A01375808.
#El programa calcula el total a pagar por paquetes de software comprados y aplica, dependiendo del caso, un descuento.

def calcularCosto(numero_paquetes): #Calcula el costo total de los paquetes comprados, con descuento.
    if (numero_paquetes >0 and numero_paquetes <=9):
        costo_total = numero_paquetes * 1500
        return costo_total
    elif (numero_paquetes >= 10 and numero_paquetes <= 19):
        costo_total = (numero_paquetes * 1500) - ((numero_paquetes * 1500) * 0.20)
        return costo_total
    elif (numero_paquetes >= 20 and numero_paquetes <= 49):
        costo_total = (numero_paquetes * 1500) - ((numero_paquetes * 1500) * 0.30)
        return costo_total
    elif (numero_paquetes >= 50 and numero_paquetes <= 99):
        costo_total = (numero_paquetes * 1500) - ((numero_paquetes * 1500) * 0.40)
        return costo_total
    elif (numero_paquetes >= 100):
        costo_total = (numero_paquetes * 1500) - ((numero_paquetes * 1500) * 0.50)
        return costo_total


def calcularDescuento(numero_paquetes): #Calcula el importe de descuento.
    if (numero_paquetes > 0 and numero_paquetes <= 9):
        descuento = 0
        return descuento
    elif (numero_paquetes >= 10 and numero_paquetes <= 19):
        descuento = (numero_paquetes * 1500) * 0.20
        return descuento
    elif (numero_paquetes >= 20 and numero_paquetes <= 49):
        descuento = (numero_paquetes * 1500) * 0.30
        return descuento
    elif (numero_paquetes >= 50 and numero_paquetes <= 99):
        descuento = (numero_paquetes * 1500) * 0.40
        return descuento
    elif (numero_paquetes >= 100):
        descuento = (numero_paquetes * 1500) * 0.50
        return descuento


def main (): #Programa principal.

    numero_paquetes = int(input("Teclea la cantidad de paquetes de software que compraste: "))

    if numero_paquetes < 0:
        print("ERROR, teclea la cantidad entera y positiva de paquetes de software que compraste.")

    elif numero_paquetes > 0:
        descuento = calcularDescuento(numero_paquetes)
        print("El importe de descuento es: $%.2f" % descuento)
        costo_total = calcularCosto(numero_paquetes)
        print("El costo total de los paquetes comprados es: $%.2f" % costo_total)

main ()

