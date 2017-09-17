#encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Programa que regresa el precio por la compra cierta cantidad de paquetes.

#Esta función, calcula la cantidad a descontar del subtotal
def calcularDescuento(paquetes):
    if paquetes >= 100:
        descuento = ((paquetes * 1500) * 0.5)
    elif paquetes >= 50:
        descuento = ((paquetes * 1500) * 0.4)
    elif paquetes >= 20:
        descuento = ((paquetes * 1500) * 0.3)
    elif paquetes >= 10:
        descuento = ((paquetes * 1500) * 0.2)
    elif paquetes >= 0:
        descuento = 0
    return descuento

#Esta función calcula el total, al restar el descuento al subtotal
def calcularTotal(paquetes, descuento):
    total = (paquetes * 1500) - descuento
    return total

#Esta función es la función principal del programa, en la que captura los datos e imprime el resultado.
def main():
    #En esta parte del main, se presentan las reglas de descuento al usuario
    print("Para la compra de nuestros paquetes, existen los siguientes descuentos")
    print("")
    print("Cantidad de paquetes | Descuento")
    print("10-19                | 20%")
    print("20-49                | 30%")
    print("50-99                | 40%")
    print("100 o más            | 50%")
    print("")
    #En esta parte del main se captura los paquetes adquiridos
    paquetes =int(input("Cantidad de paquetes comprados: "))
    print("")
    #En esta parte del main se revisa que el valor ingresado haya sido positivo
    if paquetes < 0:
        print("Error, debes introducir numeros positivos")
        exit()
    descuento = calcularDescuento(paquetes)
    total = calcularTotal(paquetes, descuento)
    print("El descuento realiado fue: ", descuento)
    print("El total a pagar es: ", total)

main()