#encoding: utf-8
#coded by: Jordan Gonzalez Bustamante
def mixColors(first, second):
    first = first.lower()
    second = second.lower()
    if (first == "rojo" or first == "azul" or first == "amarillo") and (second == "rojo" or second == "azul" or second == "amarillo"):
        if (first == "rojo" and second == "azul") or (second == "rojo" and first == "azul"):
            resultantColor = "Morado"
        elif (first == "rojo" and second == "amarillo") or (second == "rojo" and first == "amarillo"):
            resultantColor = "Naranja"
        elif (first == "azul" and second == "amarillo") or (second == "azul" and first == "amarillo"):
            resultantColor = "Verde"
        elif first == second:
            resultantColor = "Colores iguales"
    else:
        resultantColor = "un error, no se pueden procesar dicha información."


    return resultantColor

def main():
    print(""""
    Según la tabla, usa la lógica de mezcla para 
    obtener el color que quieras según las mezclar.
    Ejemplo:
    ---------------------------------------------------
    | COLOR 1 | COLOR 2 | COLOR RESULTANTE            |
    ---------------------------------------------------
    | ROJO    | AZUL    | MORADO                      |
    | ROJO    | AMARILLO| NARANJA                     |
    | AZUL    | AMARILLO| VERDE                       |
    ---------------------------------------------------
    
    """)
    firstColor = input("Ingresa el primer color a mezclar : ")
    secondColor = input("Ahora el segundo color a mezclar  : ")
    mixedColor = mixColors(firstColor, secondColor)
    print("El color resultante es %s" % mixedColor)


main()