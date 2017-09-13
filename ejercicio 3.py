# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
#convinar colores primarios
def color(color1, color2): #calcula el color resultante
    if (color1 == "rojo" or color1 == "amarillo" or color1 == "azul") and color1 == color2:
        return color1
    elif (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
        return("Morado")
    elif (color1 == "rojo" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "rojo"):
        return("Naranja")
    elif (color1 == "azul" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "azul"):
        return("Verde")
    else:
        return("error")
def main():
    color1 = str(input("Escribe un color: "))
    color2 = str(input("Escribe otro color: "))
    color1 = color1.lower()
    color2 = color2.lower()
    print(color(color1, color2))
main()