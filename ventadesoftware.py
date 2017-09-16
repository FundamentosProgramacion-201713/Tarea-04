#encoding UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: Este programa lee el número de paquetes comprados y despliega la cantidad descontada (si la hay) y el total a pagar de la compra.

#Esta función calcula el porcentaje de descuento que será aplicado a la compra a parir de los paquetes que se reciben como parámetro
def calcularporcentaje(paquetesC):
    if paquetesC <10:
        return 0
    elif paquetesC >=10 and paquetesC <20:
        return 20
    elif paquetesC >=20 and paquetesC <50:
        return 30
    elif paquetesC >=50 and paquetesC <100:
        return 40
    elif paquetesC >=100:
        return 50

#Esta función calcula el monto que será descontado de la compra a partir del costo y porcentaje que se reciben como parámetros
def calculardescuento(costo, porcentaje):
    descuento = costo*(porcentaje/100)
    return descuento

#Esta función calcula el costo sin descuento de la compra a partir del número de paquetes comprados que recibe como parámetro
def Calcularcosto(paquetesC):
    costo = paquetesC*1500
    return costo

#Esta función calcula el total de la compra a partir del costo y el descuento que recibe como parámetros
def calcularcompra(costo, descuento):
    compra = costo-descuento
    return compra

#La función main, valida el número de paquetes comprados, si la cantidad es valida llama a las funciones anteriores para calcular el descuento y la compra total.
def main():
    paquetesC = int(input('Ingrese los paquetes comprados: '))
    if paquetesC >=0:
        costo=Calcularcosto(paquetesC)
        porcentaje = calcularporcentaje(paquetesC)
        descuento= calculardescuento(costo,porcentaje)
        compra = calcularcompra(costo,descuento)
        print('El descuento de tu compra es de %d porciento, $%.2f' %(porcentaje,descuento))
        print('El costo de la compra sin descuento es de $%.2f' %costo)
        print('El valor de la compra con descuento es de $%.2f' %compra)
    else:
        print('El valor ingresado es inválido')
main()