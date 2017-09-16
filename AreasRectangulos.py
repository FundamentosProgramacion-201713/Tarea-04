#encoding: UTF-8
#Autor: Javier Martínez Hernández A01375496
#Descripción: Se comparan los rectangulos dados por el usuario y se dibujaran
import turtle


def calcularArea(base, altura): #calcula el area del rectangulo
    return (base*altura)


def calcularPerimetro(base, altura):  #Calcula el perimetro del rectangulo
    return(2*base)*(2*altura)


def dibujarRectangulo(base, altura):  #Dibuja los rectangulos con lo metido por el usuario
    turtle.shape("arrow")
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.color("red")




def main():
    base1=float(input("Ingresa la base del primer rectangulo: "))
    altura1=float(input("Ingresa la altura del primer rectangulo: "))
    base2=float(input("Ingresa la base del segundo rectangulo: "))
    altura2=float(input("Ingresa la altura del segundo rectangulo: "))
    area1=calcularArea(base1,altura1)
    area2=calcularArea(base2,altura2)
    perimetro1=calcularPerimetro(base1,altura1)
    perimetro2=calcularPerimetro(base2,altura2)
    dibujarRectangulo(base1,altura1)
    dibujarRectangulo(base2, altura2)
    turtle.exitonclick()
    if area1==area2:
        print("Las area son iguales %.2f"%area1)
    elif area1>area2:
        print("El area del primer rectangulo es mayor %.2f" % area1)
    else:
        print("El area del segundo rectangulo es mayor %.2f"%area2)
main()