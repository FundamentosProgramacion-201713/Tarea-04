# encoding: UTF-8
# Sebastian Morales Martin
# calcula el descuento de los paquetes de software

paquete = 1500
def main():
    paquetes = int(input("introduzca el número de paquetes comprados: "))
    if paquetes<(0):
        print("ERROR")
    else:
            descuento = calcularDescuento(paquetes)
            print("Tu total con el descuento es de: ", descuento)

def calcularDescuento(valor): # calcula el descuento dado y manda el resultado de regreso
    if valor>0 and valor<=10:
        descuento = (valor*paquete)
        return descuento
    elif valor>=10 and valor<20:
        descuento = (valor*paquete)-((paquete*valor)*.20)
        return descuento
    elif valor>=20 and valor<50:
        descuento = (valor*paquete)-((paquete*valor)*.30)
        return descuento
    elif valor>=50 and valor<100:
        descuento = (valor*paquete)-((paquete*valor)*.40)
        return descuento
    elif valor>=100:
        descuento = (valor*paquete)-((paquete*valor)*.50)
        return descuento
main()