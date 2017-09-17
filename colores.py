#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez, A01375808.
#El usuario teclea dos colores primarios y se entrega la combinación de estos.

def combinarColores(color1, color2): #Verificamos la combinación creada y la devolvemos.
    if (color1 == "rojo" or color2 == "rojo") and (color2 == "azul" or color1 == "azul"):
        color_resultante1 = "MORADO"
        return color_resultante1
    elif (color1 == "rojo" or color2 == "rojo") and (color1 == "amarillo" or color2 == "amarillo"):
        color_resultante2 = "NARANJA"
        return color_resultante2
    elif (color1 == "azul" or color2 == "azul") and (color1 == "amarillo" or color2 == "amarillo"):
        color_resultante3 = "VERDE"
        return color_resultante3


def main (): #Programa Principal.

    color1 = input("Teclea cuál de los tres colores primarios (rojo, amarillo o azul), quieres combinar: ")
    color1 = color1.lower()

    color2 = input("Teclea con que otro color primario (rojo, amarillo o azul) vas a combinar: ")
    color2 = color2.lower()

    if (color1 == "rojo" or color1 == "amarillo" or color1 == "azul") and (color2 == "rojo" or color2 == "amarillo" or color2 == "azul"):
        color_resultante = combinarColores(color1, color2)
        print("El color resultante es:", color_resultante)
    else:
        print("ERROR, debes teclear las letras de algún color primerio")

main()
