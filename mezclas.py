#Encoding UTF-8
#Anaid Fernanda Labat González, A01746289
#Mezclar colores primarios

def mezclarColores(color1, color2): #Se caclula la mezcla de dos colores
    if color1 == "rojo" and color2 == "azul" or color1 == "azul" and color2 == "rojo":
        mezcla = "Morado"
    elif color1 == "rojo" and color2 == "amarillo" or color1 == "amarillo" and color2 == "rojo":
        mezcla = "Naranja"
    elif color1 == "azul" and color2 == "amarillo" or color1 == "amarillo" and color2 == "azul":
        mezcla = "Verde"
    elif color1 == color2:
        mezcla = color1
    return mezcla

#Se solicitan colores a mezclar y se imprime el resultado, si no son colores primarios se imprime error
def main():
    primercolor=str(input("Escribe el primer color a mezclar: ", ))
    priercolor=primercolor.lower()
    segundocolor=str(input("Escribe el segundo color a mezclar: ", ))
    segundocolor=segundocolor.lower()
    if primercolor == "rojo" and segundocolor == "azul" or primercolor == "azul" and segundocolor == "rojo":
        resultado = mezclarColores(primercolor, segundocolor)
        print("El resultado de mezclar", primercolor, "y", segundocolor, "es: ", resultado)
    elif primercolor == "rojo" and segundocolor == "amarillo" or primercolor == "amarillo" and segundocolor == "rojo":
        resultado = mezclarColores(primercolor, segundocolor)
        print("El resultado de mezclar", primercolor, "y", segundocolor, "es: ", resultado)
    elif primercolor == "azul" and segundocolor == "amarillo" or primercolor == "amarillo" and segundocolor == "azul":
        resultado = mezclarColores(primercolor, segundocolor)
        print("El resultado de mezclar", primercolor, "y", segundocolor, "es: ", resultado)
    elif primercolor == segundocolor:
        resultado = mezclarColores(primercolor, segundocolor)
    else:
        print("ERROR, por favor prueba con los colores primarios")
main()

