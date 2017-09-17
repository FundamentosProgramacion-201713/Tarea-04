#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa es para calcular el precio de un paquete, aplicando un descuento deacuerdo a la cantidad de artículos comprados.

def calcularTotalAPagar(articulosComprados,descuento): #Calcula el total a pagar
    if articulosComprados>=1 and articulosComprados<10:
        totalAPagar=1500*articulosComprados
        return totalAPagar
    elif articulosComprados>=10 and articulosComprados<=19:
        totalAPagar=(1500*articulosComprados)-(descuento)
        return totalAPagar
    elif articulosComprados>=20 and articulosComprados<=49:
        totalAPagar=(1500*articulosComprados)-(descuento)
        return totalAPagar
    elif articulosComprados>=50 and articulosComprados<=99:
        totalAPagar=(1500*articulosComprados)-(descuento)
        return totalAPagar
    elif articulosComprados>=100:
        totalAPagar=(1500*articulosComprados)-(descuento)
        return totalAPagar


def calcularDescuento(articulosComprados):#Calcula el descuento
    if articulosComprados>=1 and articulosComprados<10:
        descuento=0*articulosComprados
        return descuento
    elif articulosComprados>=10 and articulosComprados<=19:
        descuento=(1500* articulosComprados) * 0.20
        return descuento
    elif articulosComprados>=20 and articulosComprados<=49:
        descuento=((1500*articulosComprados)*.030)
        return descuento
    elif articulosComprados>=50 and articulosComprados<=99:
        descuento=((1500*articulosComprados)*0.40)
        return descuento
    elif articulosComprados>=100:
        descuento=((1500*articulosComprados)*0.50)
        return descuento


def main():#Programa principal
    articulosComprados=float(input("¿Cuántos artículos compraste?: "))

    if articulosComprados>0:
        descuento=calcularDescuento(articulosComprados)
        totalAPagar= calcularTotalAPagar (articulosComprados,descuento)
        print ("El total a pagar es: $", totalAPagar)
        if descuento>0:
            print ("El descuento fue de $%.2f"% descuento)
    else :
        print ("No puede haber valores negativos")
main()