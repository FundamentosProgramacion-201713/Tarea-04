#Autor: Mónica Monserrat Palacios Rodríguez
#UTF-8
#Calcular la mezcla de dos colores

def mezclarColorRojo(color1, color2): #Se caclula la mezcla de dos colores
    if color1 == "rojo" and color2 == "azul" or color1 == "azul" and color2 == "rojo":
        mezcla = "Morado"

    elif color1 == "rojo" and color2 == "amarillo" or color1 == "amarillo" and color2 == "rojo":
        mezcla = "Naranja"

    elif color1 == "azul" and color2 == "amarillo" or color1 == "amarillo" and color2 == "azul":
        mezcla = "Verde"
    elif color1 == color2:
        mezcla = color1

    return mezcla

def main(): #Se piden los daros y se imprimen los resultados dependiendo del color

    coloruno=str(input("Escribe el primer color a mezclar: ", ))
    coloruno=coloruno.lower()#se cambian las cadenas a minúsculas para que concuerden con los valores de las variables.

    colordos=str(input("Escribe el segundo color a mezclar: ", ))
    colordos=colordos.lower()

    if coloruno == "rojo" and colordos == "azul" or coloruno == "azul" and colordos == "rojo":
        resultado = mezclarColorRojo(coloruno, colordos) #Se llama a la función para calcular la combinación
        print("El resultado de mezclar", coloruno, "y", colordos, "es: ", resultado)

    elif coloruno == "rojo" and colordos == "amarillo" or coloruno == "amarillo" and colordos == "rojo":
        resultado = mezclarColorRojo(coloruno, colordos) #Se llama a la función para calcular la combinación
        print("El resultado de mezclar", coloruno, "y", colordos, "es: ", resultado)

    elif coloruno == "azul" and colordos == "amarillo" or coloruno == "amarillo" and colordos == "azul":
        resultado = mezclarColorRojo(coloruno, colordos) #Se llama a la función para calcular la combinación
        print("El resultado de mezclar", coloruno, "y", colordos, "es: ", resultado)
    elif coloruno == colordos:
        resultado = mezclarColorRojo(coloruno, colordos) #Se llama a la función para calcular la combinación
        print("El resultado de mezclar", coloruno, "y", colordos, "es: ", resultado)
    else:
        print("ERROR, por favor prueba con los colores primarios") #Se marcan errores al no teclear colores primarios

main()


