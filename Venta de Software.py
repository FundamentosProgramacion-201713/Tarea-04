#Javier Pascal Flores
def hacer_descuento(paquetes): #Esta funcion es para calcular el descuento
    if paquetes < 10 and paquetes >= 0:
        descuento= 0
    elif paquetes >= 10 and  paquetes <= 19:
        descuento= (paquetes*1500)*.2
    elif paquetes >= 20 and  paquetes <= 49:
        descuento = (paquetes * 1500) * .3
    elif paquetes >= 50 and  paquetes <= 99:
        descuento = (paquetes * 1500) * .4
    elif paquetes >= 100:
        descuento = (paquetes * 1500) * .5
    return descuento

def main(): #Aqui pedimos el numero de paquetes e imprimimos el descuento en porcentaje, en cantidad, el subtotal y el total
    numero_de_paquetes=int(input("Cuantos paquetes quieres? "))
    if numero_de_paquetes < 0:
        print("NO SE PUEDE COMPRAR PAQUETES NEGATIVOS")
    else:
        subtotal= numero_de_paquetes*1500
        descuento=hacer_descuento(numero_de_paquetes)
        total= subtotal-descuento
        if numero_de_paquetes < 10:
            print("No hay descuento")
        elif numero_de_paquetes >= 10 and  numero_de_paquetes <= 19:
            print("Tu descuento fue de 20%")
        elif numero_de_paquetes >= 20 and  numero_de_paquetes <= 49:
            print("Tu descuento fue de 30%")
        elif numero_de_paquetes >= 50 and  numero_de_paquetes <= 99:
            print("Tu descuento fue de 40%")
        elif numero_de_paquetes >= 100:
            print("Tu descuento fue de 50%")
        print("El subtotal fue de $ %d , el total es de $ %d " %(subtotal, total))
main()
