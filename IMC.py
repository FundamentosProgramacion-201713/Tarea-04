# encoding UTF-8
# Autor: Jaime Orlando López Ramos, A01374696

# Descripción: Un programa que lea la estatura y peso del usuario para poder calcular su IMC y determinar si tiene bajo
# peso normal o sobrepeso


# Función que calcula IMC
def calcularImc(peso, estatura):
    imc = (peso) / (estatura)**2
    return imc


# Función que determine lo que indica el IMC de la persona
def determinarEstado(imc):
    if imc < 0:
        estado = "error"
    else:
        if imc < 18.5:
            estado = "Bajo peso"
        elif 18.5 <= imc <= 25:
            estado = "peso normal"
        elif imc > 25:
            estado = "sobrepeso"
    return estado


#Función principal
def main():
    peso= float(input("Ingrese su peso en Kg.: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    imc = calcularImc(peso, estatura)
    estado = determinarEstado(imc)
    print("Su imc es de %.2f" % imc)
    print("su estado actual es:", estado)

main()
