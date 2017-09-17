#Autor: Gabriela Mariel Vargas Franco
#encoding:UTF-8
#Leer dos colores primarios(rojo,amarillo,azul) y que imprima el color resultante al mezclarlos
def mezclarColores(color1,color2):
#Compara la combinacion de colores para sacar un color nuevo
    if (color1=="rojo" and color2=="azul") or (color1=="azul" and color2=="rojo"):
        mezclarColores="morado"
    elif (color1=="rojo" and color2=="amarillo") or (color1=="amarillo" and color2=="rojo"):
        mezclarColores="naranja"
    elif (color1=="azul" and color2=="amarillo") or (color1=="amarillo" and color2=="azul"):
        mezclarColores="verde"
    else:
        mezclarColores="Error"
#Regresa la variable mezclarColores
    return mezclarColores
def main():
#La funcion lower hara que el usuario pueda usar mayusculas o minusculas
    color1=str.lower(input("Leer color 1:"))
    color2=str.lower(input("Leer color 2:"))
    mC=mezclarColores(color1,color2)
#Imprime el color resultante
    print("Color resultante:", mC)


main()
