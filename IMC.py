#encoding: UTF-8
#Especificaciones del programa: Programa que calcula el IMC del usuario
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
def calcularimc(peso,estatura):
    imc=(peso)/(estatura**2)
    return imc
def estado(imc,estatura):
    if (imc<18.5):
        return "Bajo peso"
    elif (imc>=18.5)and(imc<=25):
        return "Peso normal"
    elif(imc>25):
        return "Sobrepeso"
    elif estatura==0:
        return "Error"
    else:
        return "Error"
def main():
    peso=float(input("Peso en kg: "))
    estatura= float(input("Estatura en metros: "))
    imc= calcularimc(peso,estatura)
    print("IMC: ", imc,",", estado(imc,estatura))
main()