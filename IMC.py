#encode: UTF-8
# Autor: David Ramírez Ríos; A01338802

def calcularIMC(masa, estatura):
    imc = masa / estatura ** 2

    return imc

def main ():
    masa = float (input("Teclea tu peso en kilogramos: "))
    estatura = float (input("Teclea tu estatura en metros: "))
    if masa >= 0 and estatura >= 1:
        imc = calcularIMC(masa, estatura)
        if imc < 18.5:
            print("Tu IMC es: ", imc)
            print("Estado: Bajo de peso")
        elif imc >= 18.5 and imc <= 25:
            print("Tu IMC es: ", imc)
            print("Estado: Peso normal")
        else:
            print("Tu IMC es: ", imc)
            print("Estado: Sobrepeso")
    else:
        print("Error: datos inválidos.")



main()