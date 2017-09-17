#encoding: UTF-8

#Autor: Alberto López Reyes
#Descripción: Este programa calcula e imprime el valor del área y el perímetro de dos rectángulos. Compara las dos
#áreas calculadas e imprime cuál es mayor. También dibuja los rectángulos. Todo esto basado en el ancho
#y el alto que los usuarios teclean sobre los rectángulos.

import turtle

#Esta función calcula el valor del perímetro del rectángulo 1 de acuerdo al ancho y el alto que se le otorga sobre la propia figura.
def CalcularPerimetroRectangulo1(intAncho1, intAlto1):
    intPerimetro1 = intAncho1 * 2 + intAlto1 * 2
    return intPerimetro1

#Esta función calcula el valor del área del rectángulo 1 de acuerdo al ancho y el alto que se le otorga sobre la propia figura.
def CalcularAreaRectangulo1(intAncho1, intAlto1):
    intArea1 = intAncho1 * intAlto1
    return intArea1

#Esta función calcula el valor del perímetro del rectángulo 2 de acuerdo al ancho y el alto que se le otorga sobre la propia figura.
def CalcularPerimetroRectangulo2(intAncho2, intAlto2):
    intPerimetro2 = intAncho2 * 2 + intAlto2 * 2
    return intPerimetro2

#Esta función calcula el valor del perímetro del área 2 de acuerdo al ancho y el alto que se le otorga sobre la propia figura.
def CalcularAreaRectangulo2(intAncho2, intAlto2):
    intArea2 = intAncho2 * intAlto2
    return intArea2

#Esta función compara el área de los dos rectángulos para determinar e imprimir cuál es mayor.
def CompararRectanglos(intArea1, intArea2):
    if intArea1 > intArea2:
        print("El rectángulo 1 tiene un área mayor.")

    elif intArea1 > intArea2:
        print("El rectángulo 2 tiene un área mayor.")

    else:
        print("Los dos rectángulos tienen igual área.")

#Esta función dibuja dos rectángulos de acuerdo al ancho y la altura respectivos y recibidos.
def  DibujarRectangulos(intAncho1, intAlto1, intAncho2, intAlto2):
    turtle.color("Blue")
    turtle.width(intAncho1/10)
    turtle.forward(intAncho1/2)
    turtle.left(90)
    turtle.forward(intAlto1)
    turtle.left(90)
    turtle.forward(intAncho1)
    turtle.left(90)
    turtle.forward(intAlto1)
    turtle.left(90)
    turtle.forward(intAncho1/2)

    turtle.color("Red")
    turtle.width(intAncho2/10)
    turtle.forward(intAncho2/2)
    turtle.left(90)
    turtle.forward(intAlto2)
    turtle.left(90)
    turtle.forward(intAncho2)
    turtle.left(90)
    turtle.forward(intAlto2)
    turtle.left(90)
    turtle.forward(intAncho2/2)

#Esta función recibe el ancho y el alto de dos rectángulos para otorgárselos a las funciones "CalcularPerimetroRectangulo1",
#"CalcularAreaRectangulo1", "CalcularPerimetroRectangulo2", "CalcularAreaRectangulo2", "Comparar Rectangulos" y "DibujarRectangulos" e
#imprimir el perímetro y el área resultantes de estas funciones.
def main():
    print("""""")
    print("""===========================""")
    print("""Rectángulo 1""")
    intAncho1 = int(input("El ancho del rectángulo es de: "))
    intAlto1 = int(input("El alto del rectángulo es de: "))

    intPerimetro1 = CalcularPerimetroRectangulo1(intAlto1, intAncho1)
    print("El perímetro del rectángulo es de:", intPerimetro1)
    intArea1 = CalcularAreaRectangulo1(intAlto1, intAncho1)
    print("El área del rectángulo es de:", intArea1)

    print("""===========================""")
    print("""Rectángulo 2""")
    intAncho2 = int(input("El ancho del rectángulo es de: "))
    intAlto2 = int(input("El alto del rectángulo es de: "))

    intPerimetro2 = CalcularPerimetroRectangulo2(intAlto2, intAncho2)
    print("El perímetro del rectángulo es de:", intPerimetro2)
    intArea2 = CalcularAreaRectangulo1(intAlto2, intAncho2)
    print("El área del rectángulo es de:", intArea2)

    print("""===========================""")
    CompararRectanglos(intArea1, intArea2)

    DibujarRectangulos(intAncho1, intAlto1, intAncho2, intAlto2)

main()
