#UTF-8
#Autor: Nazdira Abigail Cerda del Prado A01375428
#Este programa mezcla colores y le dice al usuario el color resultante

#Función que mezcla de colores
def mezclarColores(color3, color4):
    if ((color3=="rojo" and color4=="azul") or color3=="azul" and color4=="rojo"):
        return "morado"

    elif ((color3=="rojo" and color4=="amarillo") or (color3=="amarillo" and color4=="rojo")):
        return "naranja"

    else:
        if ((color3=="azul" and color4=="amarillo") or (color3=="amarillo" and color4=="azul")):
            return "verde"

def main():
    color1 = str(input("Ingrese color 1 (rojo, azul o amarillo):")) #Pide color 1
    color3=color1.lower() #Convierte el color ingresado a minúsculas
    color2 = str(input("Ingrese color 2 (rojo, azul o amarillo):")) #Pide color 2
    color4=color2.lower() #Convierte el color ingresado a minúsculas
    if (color3=="rojo" or color3=="azul" or color3=="amarillo" and color4=="amarillo" or color4=="azul" or color4=="rojo"):
        colorfinal=(mezclarColores(color3,color4))
        print("La mezcla del color", color3, "y el color", color4, "da como resultado el color", colorfinal)
    else:
        print("Error, favor de ingresar únicamente rojo, azul o amarillo.")
main()