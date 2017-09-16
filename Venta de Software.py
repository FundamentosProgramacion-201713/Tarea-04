#Encoding: UTF-8
#Autor: Luis Daniel Rivera Salinas   A01374997
#Descripcion: Al recibir cuantos paquetes se compraron, se aplica un descuento dependiendo del numero de paquetes e imprime el costo total

def descontarPorPaquetes(paquetes,precio): #Saca el precio con descuento y decide que descuento se aplicara
    if paquetes <= 0:
        return("Error, número de paquetes no validos")
    if paquetes <= 9 and paquetes >= 1:
        descuento = 1
        total = (paquetes * precio) * descuento
        descuento = 0
        return (total)

    elif paquetes <= 19 and paquetes >= 10:
        descuento = .80
        total = (paquetes*precio)*descuento
        return(total)

    elif paquetes <= 49 and paquetes >= 20:
        descuento = .70
        total = (paquetes*precio)*descuento
        return(total)

    elif paquetes <= 99 and paquetes >= 50:
        descuento = .60
        total = (paquetes*precio)*descuento
        return(total)
    else:
        descuento = .50
        total = (paquetes * precio) * descuento
        return (total)



def main(): #imprime la cantidad descontada, la cantidad de paquetes, y la cantidad final a pagar
    paquetes = int(input("Ingrese el numero de paquetes a comprar: "))
    precio = 1500.00
    total = descontarPorPaquetes(paquetes,precio)
    print("               ")
    print("El numero de paquetes comprados es de: ", paquetes)
    print("El descuento que se hace es de: $", (precio*paquetes)-total)
    print("El total ,con el descuento incluido, a pagar es de: $",total)

main()
