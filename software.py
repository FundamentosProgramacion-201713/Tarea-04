# encoding UTF-8
# Autor: Jaime Orlando López Ramos, A01374696

# Descripción: Un programa que calcula la cantidad a pagar de paquetes aplicando un descuento


# Función que calcule el precio con descuento de los paquetes comprados
def calcularPrecio(paquetesComprados):
    if paquetesComprados <= 0:
        precio="error"
    else:
        if 1<= paquetesComprados < 10:
            precio = (paquetesComprados * 1500)
        elif 10<=paquetesComprados<=19:
            precio = (paquetesComprados * 1500) *0.80
        elif 20 <= paquetesComprados <= 49:
            precio = (paquetesComprados * 1500) * 0.70
        elif 50<=paquetesComprados<=99:
            precio = (paquetesComprados * 1500) * 0.60
        elif 100<= paquetesComprados:
            precio = (paquetesComprados * 1500) * 0.50
    return precio

# Función principal
def main():
    paquetesComprados= int(input("Introduzca la cantidad de paquetes comprados: "))
    precio = calcularPrecio(paquetesComprados)
    print("El precio a pagar es de $ %.2f" % (precio))

main()