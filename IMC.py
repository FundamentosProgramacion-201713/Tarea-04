#Pedro Cortés Soberanes A01374919
#Función: Calcular IMC y calcular estado

#Calcular IMC
def calcularIMC (peso,estatura):
    imc = (peso)/((estatura)*(estatura))

    return imc

#Calcular estado con base en el IMC
def calcularEstado (imc):
    if imc<18.5:
        x = ("Bajo Peso")
    if imc>=18.5 and imc<=25:
        x = ("Peso Normal")
    if imc>25:
        x = ("Sobrepeso")
    return x


def main():
    pesoKg = float(input("Teclea tu peso en kilogramos: "))
    estaturaM = float(input("Teclea tu estatura en metros: "))
    imc = calcularIMC(pesoKg,estaturaM)
    print(" -Tu IMC es de: %.2f " % imc)
    estado = calcularEstado(imc)
    print(" -Tu estado es de: " ,estado)


main()