# encoding: UTF-8
#autor: Eduardo Gallegos Solís
# programa que calcula el precio total con descuento, en venta de sofwares.

# Calcula es total a pagar aplicando el descuento correspondiente
def calcularPrecio(software):
    if software>-1 and software<10:
        precio = (software * 1500)
    elif software>= 10 and software<20:
        precio = ((software * 1500)*.80)
    elif software>=20 and software<50:
        precio = ((software * 1500)*.70)
    elif software>=50 and software<100:
        precio = ((software*1500)*.60)
    elif software>=100:
        precio = ((software*1500)*.50)
    else:
        precio = ("Error")
    return precio

#calcula el descuento que se obtuvo
def calcularDescuento(software):
    if software>-1 and software<10:
        descuento = (0)
    elif software>= 10 and software<20:
        descuento = ((software * 1500)*.20)
    elif software>=20 and software<50:
        descuento = ((software * 1500)*.30)
    elif software>=50 and software<100:
        descuento = ((software*1500)*.40)
    elif software>=100:
        descuento = ((software*1500)*.50)
    else:
        descuento = ("Error")
    return descuento

def main():
    software = int(input("Cuántos softwares vas a comprar? "))
    precio = calcularPrecio(software)
    print("El precio a pagar es: $",precio)
    descuento = calcularDescuento(software)
    print("Usted ahorró: $",descuento)
main()