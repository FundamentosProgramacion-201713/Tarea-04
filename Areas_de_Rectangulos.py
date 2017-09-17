#encoding: UTF-8
#Raul Ortiz Mateos A01375407
#Escribir un programa que  calcule las areas y los perimetros de los 2 rectangulos

import turtle


def calcularAreaRectangulos(base,altura):
    area = base * altura
    return area

def cakcularPerimetroRectangulo(base,altura):
    perimetro= (base*2)+(altura*2)
    return perimetro

def compararAmabasAreas(area1,area2):

    if area1>area2:
        return ("el area del rectangulo 1 es mayor que la del rectangulo 2")
    elif area1<area2:
        return ("el area del rectangulo 1 es menor que la del rectangulo 2")
    elif area1==area2:
        return ("el area del rectangulo 1 y 2 son iguales")

def dibujarRectangulo1(base1,altura1):
    turtle.color("green")
    turtle.begin_fill()
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(altura1)
    turtle.left(90)
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(altura1)
    turtle.end_fill()

def dibujarRectangulo2(base2,altura2):
    turtle.color("red")
    turtle.begin_fill()
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(altura2)
    turtle.left(90)
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(altura2)
    turtle.end_fill()

def main():
    print("se van a calcular 2 areas diferentes o iguales y en cada seccion se te va a pedir la base y la altura de los respectivos triangulos")
    print("Dame los datos de tu primer rectangulo")
    base1=float((input("cual es la base de tu rectangulo? ")))
    altura1=float(input("cual es la altura de tu rectangulo? "))
    area1 = calcularAreaRectangulos(base1,altura1)
    perimetro1=cakcularPerimetroRectangulo(base1,altura1)
    print("el area de tu primer rectangulo es de:",area1)
    print("el perimetro de tu primer rectangulo es de:",perimetro1)

    print("dame la altura de tu segundo rectangulo")
    base2=float((input("cual es la base de tu rectangulo? ")))
    altura2=float((input("cual es la altura de tu rectangulo? ")))
    area2 = calcularAreaRectangulos(base2,altura2)
    perimetro2 = cakcularPerimetroRectangulo(base2,altura2)
    print("el area de tu primer rectangulo es de:",area2)
    print("el perimetro de tu primer rectangulo es de:", perimetro2)

    comparacion=compararAmabasAreas(area1,area2)
    print(comparacion)

    dibujarRectangulo1(base1,altura1)
    dibujarRectangulo2(base2,altura2)
    turtle.exitonclick()

main()
