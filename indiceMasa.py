#encoding: UTF-8
#Autor: Daniel Sahuer
#programa que calcula el IMC de una persona e imprime su peso


def calcularIMC(masa, estatura): #Calcula el IMC
    total = masa / (estatura ** 2)
    return total #Regresa


def calcularPesoTotal(imc): #Calcula el peso de una persona
    if imc > 0 and imc < 18.5:
        peso = "Peso bajo"
    elif imc >= 18.5 and imc <= 25:
        peso = "Peso normal"
    elif imc > 25:
        peso = "Sobrepeso"
    else:
        peso = "Error"
    return peso #Regresa


def main():
    masa = float(input("Escribe tu peso en kilográmos: "))
    estatura = float(input("Escribe tu estarura en metros: "))

    if estatura == 0:
        print("Error")

    else:
        imc = calcularIMC(masa,estatura)
        peso = calcularPesoTotal(imc)

        print("\nTu Índice de Masa Corporal es de: %.2f\nTienes %s" % (imc,peso))

main()