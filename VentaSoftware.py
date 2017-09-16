#encoding: UTF-8
#Autor: Javier Martínez Hernández A01375496
#Descripción: Se calcula el descuento que se hace por comprar paquetes

def calcularDescuentoPorPaquete(paquetesComprados,precio): #Calcula el descuento dependiendo de los paquetes comprados
    if paquetesComprados <= 9 and paquetesComprados >= 1:
        descuento=1
        total=(paquetesComprados*precio)*descuento
        return (total)

    elif paquetesComprados<=19 and paquetesComprados>=10:
        descuento = .80
        total=(paquetesComprados*precio)*descuento
        return(total)

    elif paquetesComprados<=49 and paquetesComprados>=20:
        descuento=.70
        total=(paquetesComprados*precio)*descuento
        return(total)

    elif paquetesComprados<=99 and paquetesComprados >=50:
        descuento=.60
        total=(paquetesComprados*precio)*descuento
        return(total)
    else:
        descuento=.50
        total = (paquetesComprados*precio)*descuento
        return(total)



def main():
    paquetesComprados = float(input("Ingrese el numero de paquetes que se compraron: "))
    precio = 1500.00
    if paquetesComprados>0:
        total = calcularDescuentoPorPaquete(paquetesComprados,precio)
        print("El descuento que se hace es de: ",(precio*paquetesComprados)-total)
        print("El total ,con el descuento incluido, a pagar es de: ",total)
    else:
        print("Ingresa numero valido")
main()