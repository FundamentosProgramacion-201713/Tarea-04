#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219
#Escribe un programa que lea el peso y la estatura, calcule el IMC y diga si la persona tiene o no sobrepeso

def main():
    peso = float(input("Peso en kilogramos: "))
    estatura = float(input("Estatura en metros: "))
    if peso <= 0:
        return "Error"
    if estatura <= 0:
        return "Error"
    IMC = calcularIMC(peso, estatura)
    print("Indice de Masa Corporal:", IMC)
    sobrepeso = definirsobrepeso(IMC)
    print(sobrepeso)

def calcularIMC(peso, estatura):
    IMC = peso / (estatura ** 2)
    return IMC

def definirsobrepeso(IMC):
    if IMC < 18.5:
        return "La persona esta baja de peso"
    elif IMC < 25 and IMC > 18.5:
        return "La persona esta en un peso normal"
    elif IMC > 25:
        return "La persona sufre sobrepeso"
main()