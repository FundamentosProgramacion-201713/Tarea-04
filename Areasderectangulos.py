#encoding: UTF-8
#Especificaciones del programa: Calcula el area y dimensiones de los rectangulos y los traza.
#Autor: Ernesto Ibhar Guevara Gomez
#Matricua: A01746121
import turtle
def dibujarRectangulo(lado1,base1,lado2,base2): #Dibuja los rectangulos con la tortuga
    turtle.shape("turtle")
    turtle.color("red")
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(lado1)
    turtle.left(90)
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(lado1)
    turtle.color("Blue")
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(lado2)
    turtle.left(90)
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(lado2)
    turtle.exitonclick()

def calculararea(l,b): #Calcula el area
    area=l*b
    return area
def calcularperimetro(l,b): #Calcula el perimetro
    perimetro=(2*l)+(2*b)
    return perimetro
def main():
    lado1=int(input("Introduzca el lado de su rectangulo numero 1: "))
    base1=int(input("Introduzca la base de su rectangulo numero 1: "))
    area1=calculararea(lado1,base1)
    perimetro1= calcularperimetro(lado1,base1)
    print("")
    lado2=int(input("Introduzca el lado de su rectangulo numero 2: "))
    base2=int(input("Introduzca la base de su rectangulo numero 2: "))
    area2=calculararea(lado2,base2)
    perimetro2=calcularperimetro(lado2,base2)
    print("El area de tu rectangulo con las medidas de %d x %d es de %dm^2. Su perimetro es de: %dm."%(lado1,base1,area1,perimetro1))
    print("El area de tu rectangulo con las medidas de %d x %d es de %dm^2. Su perimetro es de: %dm." % (lado2, base2, area2, perimetro2))
    if area1>area2:
        print("El area del rectangulo 1 es mayor a la del rectangulo 2.")
    elif area2>area1:
        print("El area del rectangulo 2 es mayor a la del rectangulo 1.")
    elif area1==area2:
        print("Las areas son iguales.")
    dibujarRectangulo(lado1,lado2,base1,base2)

main()


