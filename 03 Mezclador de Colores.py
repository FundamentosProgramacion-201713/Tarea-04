#encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Programa que imprime el color resultante de la mezcla de dos colores.

#Esta función convierte la cadena ingresada en una cadena de letras minusculas y las compara para determinar si el color es rojo, amarillo o azul
def igualarNombres(nombreColor):
    nombreColor = nombreColor.lower()
    if nombreColor == "rojo":
        color = 1
    elif nombreColor == "amarillo":
        color = 2
    elif nombreColor == "azul":
        color = 3
    else:
        color = 0
    return color

#Esta función regresa una cadena del color equivalente al resultante de los dos colores ingresados
def mezclarColor(color1, color2):
    if color1 == 1 and color2 == 1:
        colorFinal = "Rojo"
    elif color1 == 2 and color2 == 2:
        colorFinal = "Amarillo"
    elif color1 == 3 and color2 == 3:
        colorFinal = "Azul"
    elif color1 == 1 and color2 == 2:
        colorFinal = "Naranja"
    elif color1 == 2 and color2 == 1:
        colorFinal = "Naranja"
    elif color1 == 1 and color2 == 3:
        colorFinal = "Morado"
    elif color1 == 3 and color2 == 1:
        colorFinal = "Morado"
    elif color1 == 2 and color2 == 3:
        colorFinal = "Verde"
    elif color1 == 3 and color2 == 2:
        colorFinal = "Verde"
    return colorFinal

#Esta función es la función principal del programa, en la que captura los datos e imprime el resultado.
def main():
    print("Introduce dos de algunos de estos colores:")
    print("Rojo")
    print("Amarillo")
    print("Azul")
    print("")
    color1 = str(input("Color 1: "))
    color2 = str(input("Color 2: "))
    #En esta parte del programa se convierten los colores ingresados a los valores 1, 2 y 3
    valorColor1 = igualarNombres (color1)
    valorColor2 = igualarNombres (color2)
    #En esta parte del programa se evalua si las cadenas ingresadas coinciden con alguno de los colores
    if valorColor1 != 0 or valorColor2 != 0:
        colorFinal = mezclarColor(valorColor1, valorColor2)
        print("El color resultante de la combinación de ", color1, " y ", color2, " es: ",colorFinal)
    else:
        print("Escribiste mal alguno de los dos colores")

main()