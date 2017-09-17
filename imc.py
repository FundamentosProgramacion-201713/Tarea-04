#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
"""
Este programa calcula el IMC del usuario y, a partir de éste, indica si el usuario está en su peso normal, tiene peso
bajo o tiene sobrepeso.
"""

#La función calcula el IMC con el peso y la estatura, y devuelve el valor el IMC
def calcularIMC(w, h):
    imc = w / h**2
    return imc


#Pedimos al usuario sus datos, hacemos el cálculo del IMC e indicamos qué se puede concluir a partir de éste
# respecto al peso
def main():
    w = float(input("Introduzca su peso en kilogramos: "))
    h = float(input("Introduzca su estatura en metros: "))
    if w <= 0 or h <= 0 :
        print("Por favor, introduce un número válido") #mensaje de error para valores incorrectos

    imc = calcularIMC(w, h)         #Llamamos a la función que calcula el IMC
    print("Su IMC es: %.2f" % (imc))

    if imc <= 18.50 :
        print("Su peso es bajo.")
    elif imc > 25.00 :
        print("Tiene Ud. sobrepeso.")
    else :
        print("Su peso es normal.") #Qué puede concluir el usuario sobre su peso, dado su IMC


main()