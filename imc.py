#encoding:UTF-8
#Autor: José Antonio Gómez Mora
#Lee el peso de una persona en kg y estatura en metros, e imprime el IMC

#calcula el IMC con los parámetros de peso y estatura.
def calcularIMC(peso, estatura):
    imc=peso/estatura**2
    return imc

#calcula el estado del IMC con el parámetro imc
def calcularEstado(imc):
    if imc<18.5:
        return "Bajo peso"
    elif imc>=18.5 and imc<25:
        return "Peso normal"
    else:
        return "Sobrepeso"


def main():
    peso=float(input("Ingresa tu peso en kg: "))
    estatura=float(input("Ingresa tu estatura en metros: "))
    if estatura>0 and peso>=0:
        imc=calcularIMC(peso,estatura)
        estado=calcularEstado(imc)

        print("IMC: %.2f"%imc)
        print("Estado: %s"%estado)
#condiciones para que el imc pueda ser calculado
    elif estatura==0 and peso<0:
        print("Debes escribir números positivos y la estatura debe ser mayor que 0")
    elif estatura<0 and peso<0:
        print("Escribe números positivos")

    elif estatura==0 or estatura<0:
        print("La estatura debe ser mayor que 0.")


main()


