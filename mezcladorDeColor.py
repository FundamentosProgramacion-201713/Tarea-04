#UTF-8
#Autor: Natalia Meraz Tostado          A01745008
#Descripción: lee dos colores e imprime la mezcla

def mezclarColores(color1, color2):             #combina los colores para ver cual color se forma
    if (color1=="rojo" or color1=="azul") and (color2=="rojo" or color2=="azul"):
        return "morado"
    elif (color1=="rojo" or color1=="amarillo") and (color2=="rojo" or color2=="amarillo"):
        return "naranja"
    elif (color1=="amarillo" or color1=="azul") and (color2=="amarillo" or color2=="azul"):
        return "verde"
    return "Error"

def main():
    color1 = str.lower(input("Primer color primario: "))
    color2 = str.lower(input("Segundo color primario: "))
    print("El color resultante es:", mezclarColores(color1, color2))

main()
