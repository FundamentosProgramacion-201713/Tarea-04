# encoding: UTF-8
# Autor: Viviana Osorio Nieto
# calcular el perimetro con los lados especificasos
def calcularPerimetro (l1,l2,b1,b2):
    p1 = 2*l1 + 2*b1
    p2 = 2*l2 + 2*b2

    return p1,p2
# calcular el area de los dos rectangulos
def calcularArea (l1,l2,b1,b2):
    a1 = l1*b1
    a2 = l2*b2

    return a1,a2
# cual de los dos rectangulos es mas grande
def calcularMayor (a1,a2):
    if a1 == a2:
        g = print("ambos tringulos tienen la misma area")
    else:
        if a1 > a2:
            g = print("el mas grande es el primer rectangulo")
        else:
             if a2 > a1:
                g = print("el mas grande es el segundo rectangulo")
    return g
# dibujar los rectangulos
def dibujarRectangulo (l1,l2,b1,b2):
    from turtle import (forward, left, color, penup, pendown, exitonclick)
    color ("blue")
    forward(b1)
    left(90)
    forward(l1)
    left(90)
    forward(b1)
    left(90)
    forward(l1)
    left(90)
    penup()
    pendown(-20,-20)
    color("red")
    forward(b2)
    left(90)
    forward(l2)
    left(90)
    forward(b2)
    left(90)
    forward(l2)
    left(90)
    exitonclick()
# funcion principal, leer imprimir datos
def main ():
    l1 = int(input("cual es el lado del primer rectangulo?"))
    b1 = int(input("cual es la base del primer rectangulo?"))
    l2 = int(input("cual es el lado del segundo rectangulo?"))
    b2 = int(input("cual es la base del segundo rectangulo?"))

    p1,p2 = calcularPerimetro (l1,l2,b1,b2)
    a1,a2 = calcularArea (l1,l2,b1,b2)
    calcularMayor (a1,a2)

    print("el perimetro del primer rectangulo: ", p1, "el perimetro del segundo rectangulo es:", p2)
    print("el area del primer rectangulo es: ", a1, "el area del segundo rescatngulo es: ", a2)
    dibujarRectangulo(l1,l2,b1,b2)

main()