#Autor: Joaquin Rios Corvera A01375441
#Encoding: UTF-8

#Este programa pide altura y peso y calcula el IMC de una persona

#Esta función calcula el IMC de una persona (también detecta si alguno de los valores es negativo para imprimir el error
def calcularIMC(peso, estatura):
    imc = peso/estatura**2
    return imc

#Esta función calcula el estado de una persona (y marca error si los valores no son válidos)
def calcularEstado(imc):
    if imc < 18.5:
        estado = "Tienes bajo peso."
    elif imc <= 25:
        estado = "Tienes peso normal."
    else:
        estado = "Tienes sobrepeso."
    return estado
def main():
    peso = float(input("Tecela tu peso en kilogramos: "))
    estatura = float(input("Teclea tu estatura en metros: "))

    if estatura == 0:
        print("La estatura no puede ser 0m.")
    elif peso < 0 or estatura < 0:
        print("No puede haber valores negativos")
    else:
        imc = calcularIMC(peso, estatura)
        estado = calcularEstado(imc)
        print("Tu IMC es de: %.1f" %imc)
        print(estado)

main()