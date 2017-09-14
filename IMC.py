#encoding:UTF-8

#Autor: Carlos Pano Hernández
#Descripción: Este programa es para calcular el IMC de las personas.


#IMC:
def calcularIMC(p,e):
    indiceM=p/(e**2)
    return indiceM

#Funcion y llamado de main:
def main():
    peso=float(input("Introduzca su peso (kg):"))
    estatura=float(input("Introduzca su estatura(m):"))

    print("------------------------------------------")

    #Numeros negativos
    if peso<=0 or estatura<=0:
        print("ERROR: utilizar valores positivos")
    #Comparaciones
    elif peso>0 and estatura>0:
        IMC=calcularIMC(peso,estatura)

        if IMC<18.5:
            print("Tu IMC es de: %.2f - Estás bajo de peso."%(IMC))
        if 18.5<=IMC<=25:
            print("Tu IMC es de: %.2f - Tu peso es normal."%(IMC))
        if IMC>25:
            print("Tu IMC es de: %.2f - SOBREPESO. Visite a su médico."%(IMC))
main()