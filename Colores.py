#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que toma dos colores primarios y da el color resultante



def encontrarColor(color1, color2):             #Función que encuentra el color resultante
    if (color1=="rojo" or color2=="rojo") and (color1=="azul" or color2=="azul"):
        color3="4"
        return color3
    elif (color1=="rojo" or color2=="rojo") and (color1=="amarillo" or color2=="amarillo"):
        color3="Naranja"
        return color3
    elif (color1=="azul" or color2=="azul") and (color1=="amarillo" or color2=="amarillo"):
        color3="Verde"
        return color3
    else:
        color3="Error"
        return color3



def main():
    color1=input("Introducir color 1: ")
    color1=color1.lower()
    color2=input("Introducir color 2: ")
    color2=color2.lower()
    colorResultante= encontrarColor(color1, color2)
    print("El color resultante es: ", colorResultante)

main()