#encoding UTF-8
#Omar Israel Galván García A01745810
#Este programa lee las dimensiones de dos rectángulos, imprime su área y perímetro.

import turtle

def calcularArea(altura,base):          #Calcula el área del rectángulo
    area =  altura * base
    return area

def calcularPerimetro(altura,base):   #Calcula el perímetro del  rectángulo
    perimetro = (altura * 2) + (base * 2)
    return perimetro

def dibujarRectangulo(alturaUno,baseUno,alturaDos,baseDos):             #Dibuja los rectángulos con las medidas dadas.
    turtle.bgcolor("lightblue")
    turtle.color("red")
    turtle.penup()
    turtle.goto(-200,0)
    turtle.pendown()
    turtle.pensize(2)
    turtle.forward (baseUno)
    turtle.left (90)
    turtle.forward (alturaUno)
    turtle.left(90)
    turtle.forward (baseUno)
    turtle.left(90)
    turtle.forward (alturaUno)

    turtle.color("blue")
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-200,-50)
    turtle.pendown()
    turtle.forward(alturaDos)
    turtle.left(90)
    turtle.forward(baseDos)
    turtle.left(90)
    turtle.forward(alturaDos)
    turtle.left(90)
    turtle.forward(baseDos)
    turtle.penup()
    turtle.goto(0,0)

    turtle.exitonclick()


def main ():                        #La función principal lee los  lados de los dos rectángulos
    alturaUno = float(input("Ingrese la altura del primer rectángulo: "))
    baseUno = float(input("Ingrese la base del primer rectángulo: "))
    alturaDos = float(input("Ingrese la altura del segundo rectángulo: "))
    baseDos = float(input("Ingrese la base del segundo rectángulo: "))


    areaUno = calcularArea(alturaUno,baseUno)
    areaDos = calcularArea(alturaDos,baseDos)
    perimetroUno = calcularPerimetro(alturaUno,baseUno)
    perimetroDos = calcularPerimetro(alturaDos,baseDos)
    print("----------------------------------------")
    print("El área del primer rectángulo es: ",areaUno)
    print("El perímetro del primer rectángulo es: ", perimetroUno)
    print("El área del segundo rectángulo es: ",areaDos)
    print("El perímetro del segundo rectámgulo es: ",perimetroDos)

    dibujarRectangulo(alturaUno, baseUno,alturaDos,baseDos)

    if areaUno == areaDos:
        print("Las áreas de los rectángulos son iguales")
    elif areaUno > areaDos:
        print("El área del primer rectángulo es mayor")
    else:
        print("El área del segundo rectángulo es mayor")



main()