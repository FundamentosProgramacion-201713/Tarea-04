# encoding: UTF-8


# Autor: Iván Alejandro Dumas
# Descripción: Este programa calcula el total a pagar por la compra de software, incluyendo el descuento


# Esta función calcula el precio incluyendo el descuento
def calcularPrecio(paquetes):
    precio = paquetes * 1500.00
    descuento = 0
    if paquetes > 99:
        descuento = paquetes * 1500.00 * 0.5
        precio = paquetes * 1500.00 * 0.5
    elif paquetes > 49:
        descuento = paquetes * 1500.00 * 0.4
        precio = paquetes * 1500.00 * 0.6
    elif paquetes > 19:
        descuento = paquetes * 1500.00 * 0.3
        precio = paquetes * 1500.00 * 0.7
    elif paquetes > 9:
        descuento = paquetes * 1500.00 * 0.3
        precio = paquetes *1500.00 * 0.8
    return precio, descuento

# Función principal del programa
def main():
    paquetes = int(input("Número de paquetes comprados: "))
    print("––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––")
    if paquetes >= 0:
        precio, descuento = calcularPrecio(paquetes)
        print("El total a pagar por %d paquete(s) de software es de $ %.2f" % (paquetes,precio))
        if paquetes > 9:
            print("Se le realizó un descuento por $ %.2f" % (descuento))
    else:
        print ("ERROR: Valores invalidos, intenta ingresando valores enteros positivos")


# Llamar a la función principal
main()