# encode UTF-8
# Autor: Luis Enrique Neri Pérez
# Descripción: 	Programa que lee el peso y la estatura e imprime el IMC

def calcularIMC(estatura, peso): #Función que calcula el IMC
    imc = float( peso / (estatura)**2 )
    return imc


def seleccionarEstatus(imc): #Función que selecciona el estatus de salud
    if  imc < 18.5:
        return "bajo peso"
    elif 18.5 <= imc <= 25:
        return "peso normal"
    elif imc > 25:
        return "sobrepeso"
    else:
        pass


def main(): #Funcion principal
    print("ÍNDICE DE MASA CORPORAL")
    print("---------------------------------------------")
    estatura = float(input("Ingresa tu estatura en metros: "))
    peso = float(input("Ingresa tu peso en kilogramos: "))
    if estatura > 0 and peso >= 0:
        imc = float(calcularIMC(estatura, peso))
        estatusIMC = seleccionarEstatus(imc)
        print("------------------")
        print("Tu IMC es de: %.2f kg/m²" % imc)
        print("Tu estatus es de", estatusIMC)
    else:
        print("ERROR: La estatura debe ser mayor a cero y no puedes escribir números negativos.")


main()