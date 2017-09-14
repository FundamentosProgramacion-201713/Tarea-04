#encoding UTF-8
#Autor: Jaime Orlando López Ramos, A01374696

#Descripción: Un programa que calcule el color resultante de mezclar 2 colores primarios


# Una función que determine el color que resulte de la mezlcla
def determinarColor(color1, color2):
    if (color1 == "azul" or color2 == "azul") and (color1=="rojo" or color2=="rojo")and (color1 != color2):
        resultante = "morado"
    elif (color1 == "azul" or color2 == "azul") and (color1=="amarillo" or color2=="amarillo")and (color1 != color2):
        resultante = "verde"
    elif (color1 == "amarillo" or color2 == "amarillo") and (color1=="rojo" or color2=="rojo")and (color1 != color2):
        resultante = "naranja"
    elif color1 == color2:
        resultante = color1
    else:
        resultante= "Error en datos introducidos"
    return resultante

# Función principal
def main():
    color1= input("Introduzca el primer color primario: ")
    color1= color1.lower()
    color2= input("Introduzca el segundo color primario: ")
    color2 = color2.lower()
    resultante = determinarColor(color1, color2)
    print("Su resultante:", resultante)


main()
