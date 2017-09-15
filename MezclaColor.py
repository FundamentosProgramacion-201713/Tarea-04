#Autor: Joaquin Rios Corvera A01375441
#Encoding: UTF-8

#Este programa mezcla los dos colores que ingrese el usuario

#Esta función convierte los strings a mayúsculas
def convertirMayuscula(color):
    color = color.upper()
    return color

#Esta función mezcla los colores y regresa el resultado
def mezclarcolores(color1, color2):
    if (color1 != "ROJO" and color1 != "AZUL" and color1 != "AMARILLO"):
        resultado = color1 + " no es un color válido."
    elif (color2 != "ROJO" and color2 != "AZUL" and color2 != "AMARILLO"):
        resultado = color2 + " no es un color válido."
    elif (color1 == "AZUL" or color2 == "AZUL") and (color1 == "ROJO" or color2 == "ROJO"):
        resultado = "MORADO"
    elif (color1 == "AZUL" or color2 == "AZUL") and (color1 == "AMARILLO" or color2 == "AMARILLO"):
        resultado = "VERDE"
    elif (color1 == "AMARILLO" or color2 == "AMARILLO") and (color1 == "ROJO" or color2 == "ROJO"):
        resultado = "NARANJA"
    else:
        resultado = color1
    return resultado

def main():
    color1 = str(input("Teclea tu primer color primario: "))
    color2 = str(input("Teclea tu segundo color primario: "))

    color1 = convertirMayuscula(color1)
    color2 = convertirMayuscula(color2)

    mezcla = mezclarcolores(color1, color2)

    print(mezcla)

main()