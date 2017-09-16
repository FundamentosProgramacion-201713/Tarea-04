#Autor: Jose Heinz Moller Santos
#Este programa te dibuja los rectangulos que tu desees y te dice cual triangulo tiene mayor area
import turtle
#calcular el perimetro de primer rectangulo
def calcularPerimetro1(dimension1,dimension2):
    perimetro = (2*dimension1) + (2*dimension2)
    return perimetro
#calcular el area del primer rectangulo
def calcularAreaDelRectangulo1(dimension1,dimension2):
    area = dimension2 * dimension1
    return area
#calcular el perimetro del segundo rectangulo
def calcularPerimetro2(dimension1A, dimension2A):
    perimetro2 = (2*dimension2A) + (2*dimension1A)
    return perimetro2
#calcular el area del segundo rectangulo
def calcularAreaDelRectangulo2(dimension1A,dimension2A):
    area2 = dimension1A * dimension2A
    return area2
#dibujar los rectangulos
def dibujarRectangulos(dimension1,dimension2, dimension1A,dimension2A):
    turtle.color("red")
    turtle.left(90)
    turtle.forward(dimension1)
    turtle.left(90)
    turtle.forward(dimension2)
    turtle.left(90)
    turtle.forward(dimension1)
    turtle.left(90)
    turtle.forward(dimension2)
    turtle.penup()
    turtle.color("blue")
    turtle.goto((dimension1A+30), 0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(dimension1A)
    turtle.left(90)
    turtle.forward(dimension2A)
    turtle.left(90)
    turtle.forward(dimension1A)
    turtle.left(90)
    turtle.forward(dimension2A)
    turtle.exitonclick()

def main():
    dimension1 = float(input("Primera Dimensión del rectangulo 1: "))
    dimension2 = float(input("Segunda Dimensión del rectangulo 1: "))

    print("                                                 ")

    dimension1A = float(input("Primera Dimensión del rectangulo 2: "))
    dimension2A = float(input("Segunda Dimensión del rectangulo 2: "))

    perimetro1 = float(calcularPerimetro1(dimension1,dimension2))
    perimetro2 = float(calcularPerimetro2(dimension1A,dimension2A))

    area1 = float(calcularAreaDelRectangulo1(dimension1,dimension2))
    area2 = float(calcularAreaDelRectangulo2(dimension1A,dimension2A))

    print ("El area del rectangulo 1 es: ",area1)
    print ("El area del recctangulo 2 es: ",area2)
    print("                                       ")
    print ("El perimetro del rectangulo 1 es: ",perimetro1)
    print ("El perimetro del rectangulo 2 es: ", perimetro2)
    print ("                                           ")
    if area1 == area2:
        print("Los dos rectangulos tienen areas iguales")
    elif area1>area2:
        print("El rectangulos con area más grande es el 1")
    else:
        print ("El rectangulo con area más grande es el 2")
    dibujarRectangulos(dimension1,dimension2, dimension1A,dimension2A)
main()