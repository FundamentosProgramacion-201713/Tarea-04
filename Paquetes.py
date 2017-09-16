#UTF-08
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que calcula la cantidad a pagar por paquetes comprados

precio = float(1500.00)

def calcularDescuento(paquetes, precio):            #Función que calcula el descuento
    if paquetes < 10 and paquetes >= 0:
        descuento= 0
    if (paquetes >= 10) and (paquetes <= 19):
        descuento= (paquetes * precio) *0.20
        return descuento
    elif (paquetes >= 20) and (paquetes <= 49):
        descuento = (paquetes * precio) * .30
        return descuento
    elif (paquetes >= 50) and (paquetes <= 99):
        descuento = (paquetes * precio) * .40
        return descuento
    elif (paquetes >= 100):
        descuento = (paquetes * precio) * .50
        return descuento
    else:
        print("Error")

def calcularTotal(paquetes, precio):            #Función que calcula el total a pagar
    if paquetes<10 and paquetes>=0:
        total=(paquetes*precio)
        return total
    if (paquetes >= 10) and (paquetes <= 19):
        total =(paquetes * precio) * .80
        return total
    elif (paquetes >= 20) and (paquetes <= 49):
        total =(paquetes * precio) * .70
        return total
    elif (paquetes >=50) and (paquetes <=99):
        total =(paquetes * precio) * .60
        return total
    elif (paquetes >=100):
        total = (paquetes * precio) * .50
        return total
    else:
        print("Error")

def main():
    paquetes = int(input("Introducir número de paquetes comprados: "))
    descuento=calcularDescuento(paquetes, precio)
    total=calcularTotal(paquetes, precio)
    print("El total a pagar es: $ ", total)
    print("El descuento fue de: $ ", descuento)

main()
