#encode: UTF-8
# Autor: David Ramírez Ríos; A01338802


# Calcula la mezcla de dos colores primarios
def mezclarColores(color1, color2):

    longitud1 = len(color1)
    longitud2 = len(color2)
    longitudT = longitud2 + longitud1

    if longitudT == 16:
        colorR = "amarillo"
    elif color1 == color2:
        colorR = color2
    elif "az" in color1 or "az" in color2:
        if longitudT == 8:
            colorR = "morado"
        else:
            colorR = "verde"
    else:
        colorR = "naranja"


    return colorR


def main ():

    color1 = input("Teclea el primer color: ").lower()
    color2 = input("Teclea el segundo color: ").lower()

    if color1 != "rojo" and color1 != "azul" and color1 != "amarillo" and color2 != "rojo" and color2 != "azul" and color2 != "amarillo":
        print("Error: colores inválidos.")
    else:
        colorR = mezclarColores(color1, color2)
        print("La mezcla de " + color1 + " y " + color2 + " es ", colorR)

main ()