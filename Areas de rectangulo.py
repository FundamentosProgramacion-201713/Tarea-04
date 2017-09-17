#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139
#Calcular el area y el perimetro de dos rectangulos y determinar cual es mayor o si son iguales.

import turtle

#Esta funcion calcula el area de los rectangulos.
def calcularArea(altura, base):
    area=altura*base
    return area

#Esta funcion calcula el perimetro de los rectangulos
def calcularPerimetro(altura, base):
    perimetro=(2*altura)+(2*base)
    return perimetro

#Esta funcion dibuja los rectangulos con la tortuga.
def dibujarRectangulos(altura, base):
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    return turtle

#Funcion que compara las areas y determina cual es mayor.
def compararAreas(area1, area2):
    if area1==area2:
        comparacion="Los rectangulos son iguales."
    elif area1>area2:
        comparacion="El rectangulo A es mas grande que el rectangulo B."
    else:
        comparacion="El rectangulo B es mas grande que el rectangulo A."
    return comparacion

def main():
    altura= float(input("La altura del rectangulo A: "))
    base= float(input("La base del rectangulo A: "))
    altura1 = float(input("La altura del rectangulo B: "))
    base1 = float(input("La base del rectangulo B: "))
    turtle.color("blue")
    dibujarRectangulos(altura,base)
    turtle.color("red")
    dibujarRectangulos(altura1, base1)
    print("")
    print("El area del rectangulo A: %.2f" %calcularArea(altura, base))
    print("El perimetro del rectangulo A: %.2f" %calcularPerimetro(altura, base))
    print("El area del rectangulo B: %.2f" %calcularArea(altura1, base1))
    print("El perimetro del rectangulo B: %.2f" %calcularPerimetro(altura1, base1))
    print("")
    print(compararAreas(calcularArea(altura, base), calcularArea(altura1, base1)))
    turtle.exitonclick()

main()