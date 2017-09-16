#encoding: UTF-8
#Autor: Irving Fuentes Aguilera
#Descripción: Programa que calcula el área y el perímetro de dos rectángulos los compara y dibuja

import turtle


def calcularPerimetro(anchoR1, largoR1):        #Función que calcula el perímetro del rectángulo
    perimetro=(2*anchoR1)+(2*largoR1)

    return perimetro


def calcularArea(baseR1, alturaR1):             #Función que calcula el área del rectángulo
    area=(baseR1*alturaR1)

    return area


def dibujarRectangulos(baseR1, baseR2, alturaR1, alturaR2):     #Función que dibuja los rectángulos
    turtle.forward(baseR1)
    turtle.left(90)
    turtle.forward(alturaR1)
    turtle.left(90)
    turtle.forward(baseR1)
    turtle.left(90)
    turtle.forward(alturaR1)
    turtle.left(270)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.color("Red")
    turtle.forward(baseR1)
    turtle.left(90)
    turtle.forward(alturaR1)
    turtle.left(90)
    turtle.forward(baseR1)
    turtle.left(90)
    turtle.forward(alturaR1)


def calcularRelacion(area1, area2):         #Función que calcula la relación entre los rectángulos
    if area1==area2:
        relacion="El área es igual"
        return relacion
    elif area1>area2:
        relacion="El área 1 es más grande"
        return relacion
    else:
        relacion="El área 2 es más grande"
        return relacion


def main():
    print("Rectángulo 1")
    baseR1=float(input("Introducir base: "))
    alturaR1=float(input("Introducir altura: "))
    print("Rectángulo 2")
    baseR2=float(input("Introducir base: "))
    alturaR2=float(input("Introducir altura: "))
    perimetro1=calcularPerimetro(baseR1,alturaR1)
    perimetro2=calcularPerimetro(baseR2,alturaR2)
    area1=calcularArea(baseR1,alturaR1)
    area2=calcularArea(baseR2,alturaR2)
    equivalencia=calcularRelacion(area1,area2)
    print("Rectángulo 1")
    print("El perímetro es: ", perimetro1)
    print("El área es: ", area1)
    print("Rectángulo 2")
    print("El perímetro es: ",perimetro2)
    print("El área es: ",area2)
    print(equivalencia)
    dibujarRectangulos(baseR1,baseR2,alturaR1,alturaR2)
    turtle.exitonclick()

main()