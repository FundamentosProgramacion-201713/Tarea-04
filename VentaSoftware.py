#encoding: UTF-8
# Autor: Dora Gabriela Lizárraga González - A01229599
# Este programa lee la cantidad comprada de paquetes de software y regresa el precio a pagar y su descuento.

# Esta función calcula el descuento que se le aplicará a la compra.
def calcularDescuento(cantidadPaquetes):
    paquetes = cantidadPaquetes
    if paquetes<10:
        descuento = 0
    elif 10<=paquetes<=19:
        descuento = paquetes*1500*.2
    elif 20<=paquetes<=49:
        descuento = paquetes*1500*.3
    elif 50<=paquetes<=99:
        descuento = paquetes*1500*.4
    else:
        descuento = paquetes*1500*.5
    return descuento

# Esta función calcula el precio total de la compra apicando el descuento ya calculado.
def calcularPrecio(descuento,cantidadPaquetes):
    precio= (cantidadPaquetes*1500)-descuento
    return precio

# Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado.
def main():
    cantidadPaquetes = int(input("Introduzca la cantidad de paquetes que comprará: "))
    print()
    print("--------------------------------")
    if 1<=cantidadPaquetes:
        descuento = calcularDescuento(cantidadPaquetes)
        precio = calcularPrecio(descuento,cantidadPaquetes)
        print("El descuento aplicado le ahorró: $",descuento)
        print("Su total a pagar es de: $",precio)
    else:
        print("La cantidad de paquetes que ha introducido es inválida.")

main()