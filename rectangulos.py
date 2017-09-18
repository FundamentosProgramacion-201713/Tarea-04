#encoding: UTF-8
#Autor: Neftalí Rodríguez Martínez, A01375808.
#Lee las dimensiones de 2 rectángulos, calcula su perímetro y área y además los dibuja.

import turtle #importamos la librería turtle para dibujar los rectángulos.

def calcularArea(ancho, largo): #Calcula el área del rectángulo
    area = ancho * largo
    return area


def calcularPerimetro(ancho, largo): #Calcula el perímetro del rectángulo
    perimetro = ancho * 2 + largo * 2
    return perimetro


def dibujarRectangulo(ancho, largo): #Dibuja el rectángulo.
    turtle.forward(largo)
    turtle.left(90)
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(largo)
    turtle.left(90)
    turtle.forward(ancho)
    turtle.left(90)



def main (): #Programa pricipal.

    ancho1 = float(input("Teclea el ancho del rectángulo 1: "))
    largo1 = float(input("Teclea el largo del rectángulo 1: "))
    print("\r")

    ancho2 = float(input("Teclea el ancho del rectángulo 2: "))
    largo2 = float(input("Teclea el largo del rectángulo 2: "))
    print("\r")

    area1 = calcularArea(ancho1, largo1)
    print("El área del rectángulo 1 es: %.2f" % area1)
    area2 = calcularArea(ancho2, largo2)
    print("El área del rectángulo 2 es: %.2f" % area2)
    print("\r")

    perimetro1 = calcularPerimetro(ancho1, largo1)
    print("El perímetro del rectángulo 1 es: %.2f" % perimetro1)
    perimetro2 = calcularPerimetro(ancho2, largo2)
    print("El perímetro del rectángulo 2 es: %.2f" % perimetro2)
    print("\r")

    if area1 > area2:
        print("El rectángulo 1 tiene mayor área")
    elif area1 == area2:
        print("Los rectángulos tienen la misma área")
    else:
        print("El rectángulo 2 tiene mayor área")
    print("\r")

    turtle.color("red")
    dibujarRectangulo(ancho1, largo1)

    turtle.color("pink")
    dibujarRectangulo(ancho2, largo2)
    turtle.exitonclick()

main()