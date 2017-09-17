#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez, A01375808.
#Calcula el índice de masa corporal e indica si estás bajo de peso, normal o con sobrepeso.

def calcularIMC(peso, estatura): #Calcula el IMC deacuerdo a los datos recibidos.
    imc = (peso / (estatura ** 2))
    return imc


def checarNivelIMC(imc):#Indica si el usuario está bajo de peso, normal o tiene sobrepeso.
    if imc < 18.5:
        nivel = "BAJO DE PESO"
        return nivel
    elif imc >= 18.5 and imc <= 25:
        nivel = "IMC NORMAL"
        return nivel
    elif imc > 25:
        nivel = "SOBREPESO"
        return nivel


def main (): #Programa principal.
    peso = float(input("Teclea tu pueso en kilogramos: "))
    estatura = float(input("Teclea tu estatura en metros: "))

    if peso > 0 and estatura > 0:
        imc = calcularIMC(peso, estatura)
        print("Tu IMC es: %.2f" % imc)
        nivel = checarNivelIMC(imc)
        print("De acuerdo con tu IMC tu nivel es:", nivel)
    else:
        print("ERROR, debes escribir valores positivos para el peso y la estatura.")

main()