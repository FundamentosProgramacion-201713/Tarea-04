#encoding: UTF-8
#Especificaciones del programa: Otorga el descuento y total a pagar dependiendo el paquete que compres.
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
def descuento(paquete): #Funcion que realiza todos los descuentos posibles
    if (paquete>=0)and(paquete<=9):
        descuento=0
        return descuento
    elif (paquete>=10)and(paquete<=19):
        descuento=(1500*paquete)*.20
        return descuento
    elif (paquete>=20)and(paquete<=49):
        descuento=(1500*paquete)*.30
        return descuento
    elif (paquete>=50)and(paquete<=99):
        descuento=(1500*paquete)*.40
        return descuento
    elif (paquete==100):
        descuento=(1500*paquete)*.50
        return descuento
    else:
        return "Error"
def total(paquete,descuento): #Funcion que calcula el total
    total=(1500*paquete)-descuento
    return total
def main():
    paquete=int(input("Paquetes comprados: "))
    descuentoo= descuento(paquete)
    print("El descuento de $",descuento(paquete))
    print("El total es de $",total(paquete,descuentoo))
main()