#encoding:UTF-8

#Autor: Carlos Pano Hernández
#Descripción: Este programa calcula el precio por paquete y un descuento dependiendo de la cantidad.

#Precio
def calcularPrecioTotal(cP):
    totalPagar=cP*1500
    return totalPagar

#Descuento
def calcularDescuento(cp):
    a=calcularPrecioTotal(cp)
    if cp<=9:
        return a

    elif 19>=cp>=10:
        b=a-(a*.20)
        return b

    elif 49>=cp>=20:
        b=a-(a*.30)
        return b

    elif 99 >= cp >= 50:
        b = a - (a * .40)
        return b

    elif cp>=100:
        b = a - (a * .50)
        return b


#Funcion main y llamada:
def main():

    cP=int(input("Ingrese la cantidad de paquetes comprados: "))
    print("---------------------------------------------------")
    if cP>=0:
        a=calcularDescuento(cP)
        print ("Por", cP,"paquete(s), el costo total sería de:$",a)
    else:
        print("ERROR: prueba con números positivos")

main()