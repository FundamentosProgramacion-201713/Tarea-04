# encoding: UTF-8
# Sebastian Morales Martin
# dibujo de dos rectángulos con turtle, y cálculo de sus areas y perimetros

import turtle

def main():
    basePrimera = int(input("Ingrese la medida para la base del primer rectángulo: "))
    alturaPrimera = int(input("Ingrese la altura del primer rectángulo: "))

    baseSegunda = int(input("Ingrese la base del segundo rectángulo: "))
    alturaSegunda = int(input("Ingrese la altura del segundo rectángulo"))

    area1 = calcularArea1(basePrimera, alturaPrimera)
    perimetro1 = calcularPerimetro1(basePrimera, alturaPrimera)
    area2 = calcularArea2(baseSegunda, alturaSegunda)
    perimetro2 = calcularPerimetro2(baseSegunda, alturaSegunda)

    print("area de primer rectángulo:", area1, "y perimetro:", perimetro1)
    print("area del segundo rectángulo:", area2, "y perimetro:", perimetro2)

    dibujarPrimerRectangulo(basePrimera, alturaPrimera)
    dibujarSegundoRectangulo(baseSegunda, alturaSegunda)

def dibujarPrimerRectangulo(base, altura):

    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)

def dibujarSegundoRectangulo(base, altura):

    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)

def calcularArea1(base, altura):
    area = base * altura
    return area

def calcularPerimetro1(base, altura):
    perimetro = (base*2)+(altura*2)
    return perimetro

def calcularArea2(base, altura):
    area = base * altura
    return area

def calcularPerimetro2(base, altura):
    perimetro = (base*2)+(altura*2)
    return perimetro

main()