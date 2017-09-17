# encoding: UTF-8
# Raúl Ortíz A01375407
#programa que calcula el IMC de una persona e indicarle si en estado de peso la persona se encuentra

def calculaIMC(masa,estatura):
    IMC=masa/(estatura**2)
    return IMC

def calcularEstadoImc(IMC):
    if IMC<18.5:
        return ("Tu estado de Indice de masa Coorporal esta bajo")
    elif IMC>=18.5 and IMC<=25:
        return ("Tu estado de Indice de masa Coorporal esta en peso normal ")
    elif IMC>25:
        return("Tu estado de Indice de masa Coorporal esta en sobrepeso")



def main():
    m=float(input("dame tu masa en kilogramos: "))
    k=float(input("dame estatura en metros:"))
    if m>0 and k>0:
        IMC = calculaIMC(m, k)
        print("tu indice de masa coorporal es de:", IMC)
        m = float(input("dame tu masa en kilogramos: "))
        k = float(input("dame estatura en metros:"))
        IMC = calculaIMC(m, k)
        print("tu indice de masa coorporal es de:", IMC)
        EstadoIMC = calcularEstadoImc(IMC)
        print(EstadoIMC)
    else:
        print("error, no se puede calcular con los numeros negativos, por favor intenta de nuevo poniendo los valores adecuados")


main()