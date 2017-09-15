#encoding:UTF-8
#Autor: José Antonio Gómez Mora
#Lee dos colores primarios (azul, rojo, amarillo) e imprime el color resultante.



#Calcula el color resultante de la mezcla de dos colores primarios con los párametros color 1 y color 2.
def mezclarColores(a, b):

    if (a=="rojo" and b=="azul")or(a=="azul" and b=="rojo"):
        return "Morado"
    elif a=="rojo" and b=="rojo":
        return "Rojo"
    if (a=="azul" and b=="amarillo")or(a=="amarillo" and b=="azul"):
        return "Verde"
    elif a=="azul" and b=="azul":
        return "Azul"
    if (a=="amarillo" and b=="rojo")or(a=="rojo" and b=="amarillo" ):
        return "Naranja"
    return "Amarillo"


def main():
    color1=input("Escribe el primer color: ")
    color1=color1.lower()
    color2 = input("Escribe el primer color: ")
    color2=color2.lower()

    if (color1=="rojo" or color1=="azul" or color1=="amarillo") and (color2=="rojo" or color2=="azul" or color2=="amarillo"):
        colorResultante=mezclarColores(color1,color2)
        print("El resultado de mezclar %s y %s es %s."%(color1,color2,colorResultante.lower()))
    else:
        print("Error. Escribe un color primario. (Rojo, Azul, Amarillo)")



main()

