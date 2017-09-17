#encoding: UTF-8
#Autor: Eduardo Roberto Müller Romero, A01745219
#Escribe un programa que lea dos colores e imprima el resultante

def main():
    color = input("color: ")
    color2 = input("color 2: ")

    combinar = combinarcolores(color, color2)
    print("Color Resultante: ", combinar)

def combinarcolores(color, color2):
    if color == ("rojo") and color2 == ("amarillo"):
        return "Naranja"
    elif color == ("rojo") and color2 == ("azul"):
        return "Morado"
    elif color == ("azul") and color2 == ("amarillo"):
        return "Verde"

main()