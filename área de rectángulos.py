# encoding: UTF-8
#autor: Eduardo Gallegos Solís
#Programa que calcula el área de un rectángulo

import turtle

#calcula el área de los rectángulos
def calcularArea (largo, ancho):
    area = largo * ancho
    return area

# Calcula el perimetro de los rectángulos
def calcularPerimetro(largo, ancho):
    perimetro = (2*largo + 2*ancho)
    return perimetro

# Compara las áreas calculadas para determinar la mayor
def calcularAreaMayor(area1, area2):
    if area1>area2:
        mayor = ("El rectángulo con mayor área es el 1")
    elif area2 > area1:
        mayor = ("El rectánculo con mayor área es el 2")
    else:
        mayor = ("Las áreas son iguales")
    return mayor

# Dibuja los rectángulos con las medidas dadas
def dibujarRectangulo(largo, ancho):
    turtle.shape("turtle")
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(largo)
    turtle.left(90)
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(largo)
    turtle.left(90)

def main():
    largo1 = float(input("Largo del rectángulo 1: "))
    ancho1 = float(input("Ancho del rectángulo 1: "))
    largo2 = float(input("Largo del rectángulo 2: "))
    ancho2 = float(input("Ancho del rectángulo 2: "))
    area1 = calcularArea(largo1, ancho1)
    area2 = calcularArea(largo2, ancho2)
    perimetro1 = calcularPerimetro(largo1, ancho1)
    perimetro2 = calcularPerimetro(largo2, ancho2)
    areaMayor = calcularAreaMayor(area1, area2)
    print("El área del rectangulo 1 es:", area1)
    print("El área del rectángulo 2 es:", area2)
    print("El perímetro del rectángulo 1 es:", perimetro1)
    print("El perímetro del rectángulo 2 es:", perimetro2)
    print(areaMayor)
    turtle.pencolor("green")
    dibujarRectangulo(largo1, ancho1)
    turtle.pencolor("red")
    dibujarRectangulo(largo2, ancho2)
    turtle.exitonclick()

main()