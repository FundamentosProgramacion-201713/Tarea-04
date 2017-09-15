#UTF-8
#Autor: Natalia Meraz Tostado          A01745008
#Descripción: Desarrollar un progrma que lea el peso y la estatura y calcule el IMC de la persona

def calcularIMC(peso, estatura):                #calcula el imc con peso y estatura
    imc = (peso) / (estatura ** 2)
    return imc

def indicarEstado(imc,estatura):                #compara el imc para indicar el estado
    if (imc<18.5):
        return "Bajo peso"
    elif (imc>=18.5) and (imc<= 25):
        return "Peso normal"
    elif (imc>25):
        return "Sobrepeso"
    elif estatura==0:
        return "Error"
    return "Error"

def main():
    peso = float(input("Peso en kg: "))
    estatura = float(input("Estatura en metros: "))
    imc = calcularIMC(peso, estatura)
    print("IMC: ", imc, indicarEstado(imc,estatura))

main()





