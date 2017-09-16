#Encoding: UTF-8
#Autor: Luis Daniel Rivera Salinas  A01374997
#Descripción: Al ingresar la altura y base de un cuadrado, regrese el area y base de cada uno, compara areas, dice cual es la menor y los dibuja

import turtle
def area1(base,altura): #area de rectangulo 1
    areaR1 = base*altura
    return (areaR1)

def area2(base2,altura2): #area rectangulo 2
    areaR2 = base2*altura2
    return (areaR2)

def perimetro1(base,altura): #perimetro rectangulo 1
    perimetro1 = (2*base)+(2*altura)
    return(perimetro1)

def perimetro2(base2,altura2): #perimetro rectangulo 2
    perimetro2 = (2*base2)+(2*altura2)
    return(perimetro2)

def dibujarRectangulo(base,altura,base2,altura2): #Dibuja los rectangulos
    turtle.pencolor("blue")
    turtle.shape("turtle")
    turtle.fd(base)
    turtle.lt(90)
    turtle.fd(altura)
    turtle.lt(90)
    turtle.fd(base)
    turtle.lt(90)
    turtle.fd(altura)

    turtle.pencolor("green")
    turtle.fd(altura2)
    turtle.lt(90)
    turtle.fd(base2)
    turtle.lt(90)
    turtle.fd(altura2)
    turtle.lt(90)
    turtle.fd(base2)

def main(): #Ingresa los valores de los rectangulos 1 y 2 (que son base y altura, y llama a las otras funciones)
    altura = float(input("Ingrese la altura del rectangulo #1: "))
    base = float(input("Ingrese la  del rectangulo #1: "))
    altura2 =float(input("Ingrese la altura del rectangulo #2: "))
    base2= float(input("Ingrese la base del rectangulo #2: "))
    Area1 = area1(base, altura)
    Area2 = area2(base2, altura2)
    if Area1 == Area2:
        print("Las area son iguales ")
    elif Area1 > Area2:
        print("El area del rectangulo #1 es mayor que el area del rectangulo #2")
    else:
        print("El area del rectangulo #1 es mayor que el area del rectangulo #2")
    dibujarRectangulo(base,altura,base2,altura2)
    turtle.exitonclick()

main()



