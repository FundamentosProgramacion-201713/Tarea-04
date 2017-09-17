#encoding: UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que recibe un número de paquetes comprados e imprimie el descuento y el total de la compra

#Funcion que calcula la cifra del descuento de los paquetes comprados
def calculardescuento(nuPaquetes):
    if nuPaquetes >=0 and nuPaquetes <= 9:
        descuento = 0
        return descuento
    elif nuPaquetes >= 10 and nuPaquetes <= 19:
        descuento = (1500*.20)*nuPaquetes
        return descuento
    elif nuPaquetes >= 20 and nuPaquetes <= 49:
        descuento = (1500*.20)*nuPaquetes
        return descuento
    elif nuPaquetes >= 50 and nuPaquetes <= 99:
        descuento = (1500*.20)*nuPaquetes
        return descuento
    else:
        descuento = (1500*.20)*nuPaquetes
        return descuento

#Funcion que calcula el total a pagar
def calculartotal(nuPaquetes, descuento):
    total = (nuPaquetes * 1500) - descuento
    return total


#Funcion principal main que lee, procesa e imprime datos
def main():
    nuPaquetes = int(input("Teclea el número de paquetes comprados: "))
    if nuPaquetes >=0:
        print("El descuento es de $%.2f" % calculardescuento(nuPaquetes))
        print("El total de la compra es de $%.2f" % calculartotal(nuPaquetes,calculardescuento(nuPaquetes)))
    else:
        print("ERROR: El número que introdujo no es válido")


main()