#Encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo A01374942
#Descripcion: A partir del numero de paquetes que el usuario ingrese, se aplicará un descuento y se imprimirá el total a pagar con el descuentos que se compró.

def calcularDescuento(paquetes,precio): #Definir la función que calculará el descuento
    if paquetes <= 0:
        return("Error, ingresar numero de paquetes validos")
    elif paquetes >=1 and paquetes <=9:      #Si los paquetes son de 1 a 9 no se aplicará el descuentoio
        descuento = 1
        total = (paquetes * precio) * descuento

        return (total)
    elif paquetes>=10 and paquetes<=19:   #Si los paquetes son iguales y mayores a 10 y menores o iguales a 19 se aplicará un descuento de 20%
        descuento = .20
        total = (paquetes*precio)*descuento
        return(total)
    elif paquetes >= 20 and paquetes <=49:  #Si los paquetes son iguales y mayores a 20 y menores o iguales a 49 se aplicará un descuento de 30%
        descuento = .30
        total = (paquetes*precio)*descuento
        return(total)
    elif paquetes >=50 and paquetes <=99:  #Si los paquetes son iguales y mayores a 50 y menores o iguales a 99 se aplicará un descuento de 40%
        descuento = .40
        total = (paquetes*precio)*descuento
        return(total)
    else:
        descuento = .50    #Si los paquetes son iguales o mayores a 100 se aplicará un descuento de 50%
        total = (paquetes * precio) * descuento
        return (total)

def main():
    paq = int(input("Ingrese los paquetes que va a comprar: "))  #Pedir al usuario el numero de paquetes
    precio = 1500.00   #Definimos el precio por paquete
    total = calcularDescuento(paq, precio)   #Obtenemos el total del descuento, después de mandar a la función calcularDescuento los datos dados por el usuario
    print("El numero de paquetes comprados son: ", paq)
    print("El descuento es de: $", total) #Imprimir el descuento aplicado
    print("El total a pagar aplicando el descuento es de: $", (precio*paq) - total) #Imprimir el total a pagar aplicando el descuento

main()       #Llamamos a la funcion main para que realice lo que  tiene dentro de ella