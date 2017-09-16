#Encoding: UTF-8
#Autor: Rodrigo Rivera Salinas
#Descripcion: Dependiendo el numero de paquetes que se compro, se aplicara un descuento dependiendo del numero de paquetes y se  imprimira el costo total

def descuentoEnPaquetes(paq,precio):
    if paq <= 0:
        return("Error, ingresar numero de paquetes validos")
    elif paq <= 9 and paq >= 1:      #si el numero de paquetes es entre 9 y 1 no se aplica el descuento
        desc = 1
        total = (paq * precio) * desc
        desc = 0
        return (total)

    elif paq <= 19 and paq >= 10:   #si el numero de paquetes es entre 19 y 10 se aplica un descuento del 20%
        desc = .80
        total = (paq*precio)*desc
        return(total)

    elif paq <= 49 and paq >= 20:  #si el numero de paquetes es entre 49 y 20 se aplica un descuento del 30%
        desc = .70
        total = (paq*precio)*desc
        return(total)

    elif paq <= 99 and paq >= 50:  #si el numero de paquetes es entre 99 y 50 se aplica un descuento del 40%
        desc = .60
        total = (paq*precio)*desc
        return(total)
    else:
        desc = .50    #si el numero de paquetes es de 100 o mas  se aplica un descuento del 50%
        total = (paq * precio) * desc
        return (total)

def main():
    paq = int(input("Ingrese el numero de paquetes a comprar: "))  #pedir numero de pauetes
    precio = 1500.00   #precio por paquete
    total = descuentoEnPaquetes(paq, precio)   #Total de los paquetes
    print("numero de paquetes comprados: ", paq)      #Imprimir numero de paquetes
    print("El descuento es de: $", (precio * paq) - total) #Imprimir el descuento
    print("El total menos el descuento es : $", total) #Imprimir el total con descuento

main()