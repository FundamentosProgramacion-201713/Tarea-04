# encoding-UTF-8
# AUTOR: José Antonio Vázquez Gabián
# Este programa agarra dos colores y te da su mezcla
def color(color, color2): #calcula el color resultante
    if (color == "rojo" or color == "amarillo" or color == "azul") and color == color2:
        return color
    elif (color == "azul" and color2 == "rojo") or (color == "rojo" and color2 == "azul"):
        return("Morado")
    elif (color == "amarillo" and color2 == "rojo") or (color == "rojo" and color2 == "amarillo"):
        return("Naranja")
    elif (color == "amarillo" and color2 == "azul") or (color == "azul" and color2 == "amarillo"):
        return("Verde")
    else:
        return("error")
def main(): #imprime los colores escritos y llama a la funcion anterior
    color1 = str(input("Escribe un color(amarillo, rojo, azul): "))
    color2 = str(input("Escribe otro color(amarillo, rojo, azul): "))
    color1 = color1.lower()
    color2 = color2.lower()
    print(color(color1, color2))
main()