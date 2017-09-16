# encoding: UTF-8
#autor: Eduardo Gallegos Solís
#Indica el color resultante de la mezcla de dos de los tres colores primarios (rojo, amarillo, azul)

#Compara los colores recibidos para dar el color resultante
def calcularColor(color1Min, color2Min):
    if (color1Min == "rojo" and color2Min == "azul") or (color1Min== "azul" and color2Min == "rojo"):
        colorResutante = ("El color resultante es el Morado")
    elif (color1Min == "rojo" and color2Min == "amarillo") or (color1Min== "amarillo" and color2Min == "rojo"):
        colorResutante = ("El color resultante es el Naranja")
    elif (color1Min == "amarillo" and color2Min == "azul") or (color1Min== "azul" and color2Min == "amarillo"):
        colorResutante = ("El color resultante es el Verde")
    return  colorResutante

def main():
    color1 = str(input("Cuál es el primer color?"))
    color2 = str(input("Cuál es el segundo color?"))
    color1Min = color1.lower()
    color2Min = color2.lower()
    if color1Min != ("rojo") and color1Min !=("amarillo") and color1Min != ("azul"):
        print("Error")
    elif color2Min != ("rojo") and color2Min !=("amarillo") and color2Min != ("azul"):
        print("Error")
    else:
        colorResultante = calcularColor(color1Min, color2Min)
        print(colorResultante)

main()