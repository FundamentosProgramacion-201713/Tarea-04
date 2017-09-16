#encode: UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: Da el precio total del software comprado

def main():
    paquetesComprados = int(input("Teclea el número de softwares comprados: "))
    if paquetesComprados > 0:
        descuento = calcularDescuento(paquetesComprados)
        totalPagar = calcularTotal(paquetesComprados)
        print("El descuento fue de $%.2f" %(descuento))
        print("EL total a pagar es de $%.2f" %(totalPagar))
    else:
        print("Cantidad invalida")



# Calcula la cantidad de descuento que se hara
def calcularDescuento(paquetesComprados):
    if paquetesComprados >= 10 and paquetesComprados  <= 19:
        return ((paquetesComprados * 1500) * .2)
    elif paquetesComprados >= 20 and paquetesComprados <= 49:
        return ((paquetesComprados * 1500) * .3)
    elif paquetesComprados >= 50 and paquetesComprados <= 99:
        return ((paquetesComprados * 1500) * .4)
    elif paquetesComprados >= 100:
        return ((paquetesComprados * 1500)* .5)
    else:
        return 0

# Calcula el precio total aplicando el descuento
def calcularTotal(paquetesComprados):
    total = (paquetesComprados * 1500) - calcularDescuento(paquetesComprados)
    return total


main()
