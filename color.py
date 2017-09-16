#Encoding: UTF-8
#Autor: Rodrigo Rivera Salinas
#Descripcion: A partir de 2 colores dados por el useario,imprimir el color que se forma entre ambos

def combinarColores(color1Min,color2Min):
    if color1Min == "rojo" and color2Min == "rojo": #si los colores son rojos, el programa regresa rojo
        return("Rojo")
    elif color1Min == "amarillo" and color2Min == "amarillo": #si los colores son amarillo, el programa regresa amarillo
        return("Amarillo")
    elif color1Min == "azul" and color2Min == "azul": #si los colores son azul , el programa regresa azul
        return("Azul")
    elif (color1Min == "rojo" and color2Min == "azul") or (color1Min == "azul" and color2Min == "rojo"): #si los colores son rojo y azul , el programa regresa Mordado
        return("Morado")
    elif (color1Min == "rojo" and color2Min == "amarillo") or (color1Min == "amarillo" and color2Min == "rojo"): #si los colores son rojo y amarillo, el programa regresa Naranja
        return("Naranja")
    elif (color1Min == "azul" and color2Min == "amarillo") or (color1Min == "amarillo" and color2Min == "azul"): #si los colores son azul y amarillo, el programa regresa Verde
        return("Verde")
    else:
        return("Colores no validos") #si no se pone los colores primarios te regresa Colores no validos

def main():
    print("Los colores validos son: Rojo, Azul y Amarillo") #Definir que colores puede usar
    color1 = input("Ingrese su primer color: ")  # pedir el primer color
    color2 = input("Ingrese su segundo color: ") #Pedir segundo color
    color1Min= color1.lower()       #.lower cambia a minusculas
    color2Min = color2.lower()
    print("Si se mezcla  " , color1Min, "y" , color2Min , "obtendra: ", combinarColores(color1Min,color2Min)) #imprimir la convinacion de los dos colores

main()