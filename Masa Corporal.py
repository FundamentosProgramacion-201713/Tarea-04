#encoding UTF-8
#Omar Israel Galván García A01745810
#Este programa lee el peso y estatura de una persona y calcula su índice de masa corporal
#IMC = masa / estatura*2

def calcularIMC(peso, estatura):   #Calcula el IMC con los datos  leidos
    imc = (peso/estatura**2)
    return imc

def calcularResultado(imc):     #En base a los datos detecta si tiene sobrepeso, normal o bajo peso
    if imc < 18.5:
        resultado = "Bajo Peso"
        return resultado
    elif imc >= 18.5 and imc <=25:
        resultado = "Peso Normal"
        return resultado
    else:
        resultado = "Sobrepeso"
        return resultado


def main():         #Lee el peso y altura. Imprime el  IMC y su estado
    peso = float(input("Ingrese su peso en kilogramos: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    if peso > 1 and estatura > 1:
        imc = calcularIMC(peso,estatura)
        resultado = calcularResultado(imc)
        print("Su IMC es: %.2f"%(imc))
        print("Su estado es: ",resultado)
    else:
        print("Error! Inntrouzca valores  válidos")


main()