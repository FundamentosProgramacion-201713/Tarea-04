#encoding:UTF-8

#Autor: Carlos Pano Hernández
#Descripción: Este programa es para calcular el IMC de las personas.

#Funcion y llamado de main:

#IMC:
def calcularIMC(p,e):
    indiceM=p/(e**2)
    return indiceM

def main():
    peso=float(input("Introduzca su peso (kg):"))
    estatura=float(input("Introduzca su estatura(m):"))
    if peso or estatura < 0:
        print("ERROR")

    print("------------------------------------------")

    IMC=calcularIMC(peso,estatura)

    if IMC<18.5:
        print("Estás bajo de peso.")

    elif 25>=IMC>=18.5:
        print("Tu peso es normal.")

    elif IMC>25:
        print("Sobrepeso. Visite a su médico.")


main()