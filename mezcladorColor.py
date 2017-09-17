#encoding: UTF-8
#Autor: Daniel Sahuer
#programa que calcula el color resultante al mezclar dos colores primarios


def calcularColorResultante(cA, cB): #Calcula el color resultante
    if cA == "rojo" and cB == "azul" or cA == "azul" and cB == "rojo":
        color = "morado"
    elif cA == "rojo" and cB == "amarillo" or cA == "amarillo" and cB == "rojo":
        color = "naranja"
    elif cA == "azul" and cB == "amarillo" or cA == "amarillo" and cB == "azul":
        color = "verde"
    else:
        color = "Error, escribe sólo colores primarios"
    return color #Regresa


def main():
    colorA = input("Escribe un color primario: ")
    colorB = input("Escribe otro color primario: ")

    cA = colorA.lower()
    cB = colorB.lower()

    colorResultante = calcularColorResultante(cA,cB)

    print ("\nEl color resultante de la mezcla de %s y %s es: %s" % (cA,cB, colorResultante))

main()