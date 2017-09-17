#encoding: UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que recibe el peso en kilos y estatura en metros  e imprime el IMC y lo compara

#Funcion que calula el IMC
def calcularIMC(peso, estatura):
    imc = peso/(estatura**2)
    return imc

#Funcion que determina si el peso es bajo, normal o alto
def determinarNivelPeso(imc):
    if imc < 18.5:
        return "Tienes bajo peso"
    elif imc >= 18.5 and imc <= 25:
        return "Tienes peso normal"
    else:
        return "Tienes sobrepeso"

#Funcion principal main que lee, procesa e imprime datos
def main():
    peso = float(input("Introduce tu peso en kilogramos: "))
    estatura = float(input("Introduce tu altura en metros: "))
    if peso >=1 and estatura >=1:
        print("Tu Indice de Masa Corporal es de %.2f" % calcularIMC(peso, estatura))
        print(determinarNivelPeso(calcularIMC(peso, estatura)))
    elif estatura == 0 and peso >=1:
        print("ERROR: La altura que diste es inválida")
    else:
        print("ERROR: El peso o la altura que diste es inválida")

main()