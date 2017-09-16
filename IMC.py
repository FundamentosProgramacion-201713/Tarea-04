# encoding: UTF-8
# autor: Eduardo Gallegos Solís
# programa que calcula el IMC e indica si está en peso bajo, normal o sobrepeso

#Calcula el IMC con los datos registrados
def calcularIMC(peso, estatura):
    imc = peso / (estatura**2)
    return imc

#Clasifica el IMC con los parámetros señalados
def clasificarIMC(imc):
    if imc<=0:
        estadoIMC = ("Error")
    elif imc<18.5:
        estadoIMC = ("Usted tiene Bajo peso")
    elif imc>=18.5 and imc<=25:
        estadoIMC = ("Usted está en peso normal")
    else:
        estadoIMC = ("Usted tiene Sobrepeso")
    return estadoIMC

def main():
    peso = float(input("Ingrese el peso en kg:"))
    estatura = float(input("Ingrese la estatura en metros:"))
    if peso<=0:
        print("Error")
    elif estatura <=0:
        print("Error")
    else:
        imc = calcularIMC(peso, estatura)
        print("Su Indice de Masa Corporal es: %.2f"%(imc))
        estadoIMC = clasificarIMC(imc)
        print(estadoIMC)
main()