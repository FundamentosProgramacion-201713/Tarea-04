#encoding: UTF-8
#Autor: Javier Martínez Hernández A01375496
#Descripción: Se calculara el IMC de una persona
def calcularIMC(peso, altura): #calcula el IMC de la persona
    imc=peso/altura**2
    return imc


def main ():
    peso=float(input("Ingresa tu peso en kg: "))
    altura=float(input("Ingresa tu altura en mts: "))
    imc=calcularIMC(peso,altura)
    if imc<18.5:
        print("Estas bajo de peso, tu IMC es ", imc)
    elif imc>=18.5 and imc<=25:
        print("Estas en tu peso, tu IMC es ", imc)
    else:
        print ("Estas en sobre peso, tu IMC es", imc)
main()