#encoding: UTF-8
# Autor: Dora Gabriela Lizárraga González - A01229599
# Este programa lee dos colores primarios e imprime el color resultante

# Esta función evalúa ambos colores y regresa la mezcla resultante
def mezclarColores (color1,color2):
    if color1 == color2:
        if color1 == "rojo":
            colorFinal = "rojo."
        elif color1 == "azul":
            colorFinal = "azul."
        else:
            colorFinal = "amarillo."
    elif (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
        colorFinal = "morado"
    elif (color1 == "rojo" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "rojo"):
        colorFinal = "naranja"
    else:
        colorFinal = "verde"
    return colorFinal

# Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado.
def main():
    print("Escriba dos colores primarios para conocer el color resultante al mezclarlos.")
    print()
    color1 = str(input("Introduzca el primer color: "))
    color2 = str(input("Introduzca el segundo color: "))
    color1 = color1.lower()
    color2 = color2.lower()
    print("--------------------------------")
    if (color1 == "rojo" or color1 == "amarillo" or color1 == "azul") and (color2 == "rojo" or color2 == "amarillo" or color2 == "azul"):
        colorFinal = mezclarColores(color1, color2)
        print("La mezcla entre", color1, "y", color2, "da", colorFinal)
    else:
        print("Ha introducido algún dato inválido.")

main()



