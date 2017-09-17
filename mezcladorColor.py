#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
"""
Este programa 'mezcla' dos colores primarios dados por el usuario e imprime el color resultante de la combinación.
"""


#Aquí se 'mezclan' los dos colores primarios. Si se introduce el mismo color, se indica que las dos entradas son idénticas.
def determinarColorResultante(strColor1, strColor2):
    if strColor1 == "rojo" and strColor2 == "azul" or strColor1 == "azul" and strColor2 == "rojo" :
        return ("morado")
    if strColor1 == "rojo" and strColor2 == "amarillo" or strColor1 == "amarillo" and strColor2 == "rojo" :
        return ("naranja")
    if strColor1 == "azul" and strColor2 == "amarillo" or strColor1 == "amarillo" and strColor2 == "azul" :
        return ("verde")
    elif strColor2 == strColor1 :
        return ("Son el mismo color")


#Pedimos al usuario los colores. Imprimimos la combinación o mensaje de error.
def main():
    color1 = input("Escribe un color primario (azul, rojo o amarillo): ")
    color2 = input("Escribe otro color primario (azul, rojo o amarillo): ")
    strColor1 = color1.lower()
    strColor2 = color2.lower()

    if strColor1 != "azul" and strColor1 != "rojo" and strColor1 != "amarillo" and strColor2 != "azul" and strColor2 != "rojo" and strColor2 != "amarillo" :
        print("Por favor, escribe un color primario: azul, rojo o amarillo.")
    else:
        colorResultante = determinarColorResultante(strColor1, strColor2)
        print ("La combinación entre los dos colores es: ", colorResultante)


main()
