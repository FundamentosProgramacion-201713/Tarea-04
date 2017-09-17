#encoding: UTF-8

#Autor: Alberto López Reyes
#Descripción: Este programa imprime el total a pagar de acuerdo a un descuento calculado basado en el número de paquetes otorgados.

#Esta función calcula el descuento -también lo imprime- y cuánto se debe de pagar de acuerdo al número de paquetes otorgados.
def CalcularPagoTotal(intNumPaquetes):
    if intNumPaquetes > 0 and intNumPaquetes < 10:
        fltTotalDescontado = 0
        print("No se aplica descuento,")
    elif intNumPaquetes > 9 and intNumPaquetes < 20:
        fltTotalDescontado = float(intNumPaquetes) * 1500 * .2
        print("Se aplica un descuento del 20%.")
        print("Se descontará un total de: $"+format(fltTotalDescontado, '.2f'))
    elif intNumPaquetes > 20 and intNumPaquetes < 50:
        fltTotalDescontado = float(intNumPaquetes) * 1500 * .3
        print("Se aplica un descuento del 30%.")
        print("Se descontará un total de: $"+format(fltTotalDescontado, '.2f'))
    elif intNumPaquetes > 50 and intNumPaquetes < 100:
        fltTotalDescontado = float(intNumPaquetes) * 1500 * .4
        print("Se aplica un descuento del 40%.")
        print("Se descontará un total de: $"+format(fltTotalDescontado, '.2f'))
    elif intNumPaquetes > 100:
        fltTotalDescontado = float(intNumPaquetes) * 1500 * .5
        print("Se aplica un descuento del 50%.")
        print("Se descontará un total de: $"+format(fltTotalDescontado, '.2f'))
    else:
        print("""===========================""")
        print("""ERROR: EL NÚMERO DE PAQUETES NO DEBE SER MENOR DE 0.
EL PROGRAMA TERMINARÁ.""")
        exit()

    fltPagoTotal = float(intNumPaquetes * 1500) - fltTotalDescontado

    return fltPagoTotal

#Esta función pide el número de paquetes que se quieren comprar para otorgárselos a la función "CalcularPagoTotal"
#para recibir y luego imprimir el total a pagar.
def main():
    print("""""")
    print("""===========================""")
    print("Número de paquetes.")
    intNumPaquetes = int(input("Teclea el número de paquetes a comprar: "))

    fltPagoTotal = CalcularPagoTotal(intNumPaquetes)

    print("""===========================""")
    print("El total a pagar: $"+format(fltPagoTotal, '.2f'))

main()
