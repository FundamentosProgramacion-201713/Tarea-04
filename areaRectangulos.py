#encoding: UTF-8
#Autor: Daniel Sahuer
#Dibuja dos rectángulos de acuerdo a las dimensiones que el usuario escribe y calcula el área y el perímetro de cada uno. Además, menciona que rectángulo tiene mayor área, o si son iguales.


from math import *
import turtle

def dibujarRectanguloA(altura, base): #Dibuja el rectángulo 1
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)


def dibujarRectanguloB(altura, base): #Dibuja el rectángulo 2
    turtle.penup()
    turtle.goto(-300,0)
    turtle.pendown()
    turtle.color("Red")
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)


def calcularAreaA(altura, base): #Calcula el área del rectángulo 1
    area = altura * base
    return area #regresa


def calcularAreaB(altura, base): #Calcula el área del rectángulo 2
    area = altura * base
    return area #regresa


def calcularPerimetroA(altura, base): #Calcula el perímetro del rectángulo 1
    perimetro = (altura * 2) + (base * 2)
    return perimetro #regresa


def calcularPerimetroB(altura, base): #Calcula el perímetro del rectángulo 2
    perimetro = (altura * 2) + (base * 2)
    return perimetro #regresa


def main():
    BaseA = float(input("Escribe la base del primer rectángulo: "))
    AlturaA = float(input("Escribe la altura del primer rectángulo: "))
    BaseB = float(input("\nEscribe la base del segundo rectángulo: "))
    AlturaB = float(input("Escribe la altura del segundo rectángulo: "))

    dibujarRectanguloA(AlturaA,BaseA)
    dibujarRectanguloB(AlturaB,BaseB)

    areaA = calcularAreaA(AlturaA,BaseA)
    areaB = calcularAreaB(AlturaB,BaseB)
    
    perimetroA = calcularPerimetroA(AlturaA,BaseA)
    perimetroB = calcularPerimetroB(AlturaB,BaseB)

    print ("\nEl área del primer rectángulo es: %.2f\nEl perímetro del primer rectángulo es: %.2f\n\nEl área del segundo rectángulo es: %.2f\nEl perímetro del segundo rectángulo es: %.2f\n" % (areaA,perimetroA,areaB,perimetroB))

    if areaA > areaB:
        print("El primer rectángulo tiene un área mayor")
    elif areaA < areaB:
        print("El segundo rectángulo tiene un área mayor")
    else:
        print("Las áreas de los rectángulos son iguales")

    turtle.exitonclick()

main()