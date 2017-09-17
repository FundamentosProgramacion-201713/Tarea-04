# encoding: UTF-8
# Raúl Ortíz A01375407
# programa en donde cada cierta compra de paquetes se aplica un descuento

def calcularDescuento(paquetes):
    if paquetes>=10 and paquetes<=19:
        precio = ((paquetes*1500)*.8)
    elif paquetes>20 and paquetes<=49:
        precio = ((paquetes*1500)*.7)
    elif paquetes>50 and paquetes<=99:
        precio = ((paquetes*1500)*.6)
    elif paquetes>100:
        precio = ((paquetes*1500)*.5)
    else:
        precio = ("Error, los descuentos solo estan contemplados de 10 paquetes para arriba")
    return precio

def main():
    paquetes = int(input("Cuántos paquetes quieres comprar? "))
    precioTotal = calcularDescuento(paquetes)
    print(precioTotal)

main()