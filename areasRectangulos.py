# encoding: UTF-8
# Sebastian Morales Martin
# dibujo de dos rectángulos con turtle, y cálculo de sus areas y perimetros

import turtle

def main(): #compila las demás funciones, les da el valor que ingresa el usuario y regresa el area, perimetro y un dibujo de los rectangulos
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

def dibujarPrimerRectangulo(base, altura): #dibuja el primer rectángulo en color rojo
    turtle.color(red)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)

def dibujarSegundoRectangulo(base, altura): #dibuja el segundo rectangulo en color verde
    turtle.color(green)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)

def calcularArea1(base, altura): #calcula el area del primer rectangulo
    area = base * altura
    return area

def calcularPerimetro1(base, altura): #calcula el perimetro del primer rectangulo
    perimetro = (base*2)+(altura*2)
    return perimetro

def calcularArea2(base, altura): #calcula el area del segundo rectangulo
    area = base * altura
    return area

def calcularPerimetro2(base, altura): #calcula el perimetro del segundo triangulo
    perimetro = (base*2)+(altura*2)
    return perimetro

main()