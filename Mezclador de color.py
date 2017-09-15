#encoding: UTF-8
#Especificaciones del programa: El usuario ingresa dos colores y el programa imprime la mezcla de los colores
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
def mezcladecolores(color1,color2): #Funcion que hace todas las combinaciones
    if(color1=="rojo" or color1=="azul") and (color2=="rojo"or color2=="azul"):
        return "Morado"
    elif(color1=="rojo" or color1=="amarillo") and (color2=="rojo" or color2=="amarillo"):
        return "Naranja"
    elif(color1=="amarillo" or color1=="azul")and (color2=="amarillo" or color2=="azul"):
        return "Verde"
    return "Error prueba con colores primarios"
def main():
    color1=str.lower(input("Color 1: "))
    color2=str.lower(input("Color 2: "))
    print("La mezcla de esos colores es: ", mezcladecolores(color1,color2))
main()
