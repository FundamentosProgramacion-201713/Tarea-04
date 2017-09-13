# encoding UTF-8
# Autor: Jaime Orlando López Ramos, A01374696

# Descripción: Un programa que lea las dimensiones de dos rectángulos y regrese el área y perímetro; aparte dibuje ambos
# rectángulos en la tortuga

import turtle

def calcularArea(b, h):
    area = b * h
    return area

def calcularPerimetro(b, h):
    perimetro = (2 * b) + (2 * h)
    return perimetro

def dibujarRectangulo(b, h):
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(h)
    turtle.left(90)
    turtle.forward(b)
    turtle .left(90)
    turtle.forward(h)
    turtle.left(90)

def main():
    b1 = float(input("Ingrese la base del primer rectángulo: "))
    h1 = float(input("Ingresa la altura del primer rectángulo: "))
    b2 = float(input("Ingrese la base del segundo rectángulo: "))
    h2 = float(input("Ingresa la altura del segundo rectángulo: "))
    if b1 > 0 and b2 > 0 and h1 > 0 and h2 > 0:
        ar1 = calcularArea(b1, h1)
        pr1 = calcularPerimetro(b1, h1)
        ar2 = calcularArea(b2, h2)
        pr2 = calcularPerimetro(b2, h2)
        print("El área de su primer rectángulo es de %.2f unidades cuadradas. El perimetro de su primer rectángulo es de %.2f" % (ar1, pr1))
        print("El área de su segundo rectángulo es de %.2f unidades cuadradas. El perimetro de su segundo rectángulo es de %.2f" % (ar2, pr2))
        turtle.pencolor("blue")
        dibujarRectangulo(b1, h1)
        turtle.penup()
        turtle.forward(2 * b1)
        turtle.pendown()
        turtle.pencolor("red")
        dibujarRectangulo(b2, h2)
        turtle.exitonclick()
    else:
        print("Uno o más de sus valores no son válidos")

main()
