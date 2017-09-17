#encoding: UTF-8
#autor: Juan Sebastian Lozano Derbez
#Rectangulos
import turtle

def tortol(x1,y1,x2,y2):
# noinspection PyUnresolvedReferences
    turtle.forward(x1)
#noinspection PyUnresolvedReferences
    turtle.left(90)
#noinspection PyUnresolvedReferences
    turtle.forward(y1)
#noinspection PyUnresolvedReferences
    turtle.left(90)
#noinspection PyUnresolvedReferences
    turtle.forward(x1)
#noinspection PyUnresolvedReferences
    turtle.left(90)
#noinspection PyUnresolvedReferences
    turtle.forward(y1)
#noinspection PyUnresolvedReferences
    turtle.penup()
#noinspection PyUnresolvedReferences
    turtle.forward(100)
#noinspection PyUnresolvedReferences
    turtle.pendown()
# noinspection PyUnresolvedReferences
    turtle.forward(x2)
#noinspection PyUnresolvedReferences
    turtle.left(90)
#noinspection PyUnresolvedReferences
    turtle.forward(y2)
#noinspection PyUnresolvedReferences
    turtle.left(90)
#noinspection PyUnresolvedReferences
    turtle.forward(x2)
#noinspection PyUnresolvedReferences
    turtle.left(90)
#noinspection PyUnresolvedReferences
    turtle.forward(y2)
#noinspection PyUnresolvedReferences
    turtle.left(90)


def area1(x1,y1):
    a1 = x1 * y1
    return a1

def area2(x2,y2):
    a2 = x2 * y2
    return a2

def compara(areauno,areados):
    if areauno > areados:
        return 1
    elif areauno < areados:
        return 2
    elif areauno == areados:
        return 3

def main():
    x1 = float(input("Escribe el ancho del rectangulo 1: "))
    y1 = float(input("Escribe el largo del rectangulo 1: "))
    x2 = float(input("Escribe el ancho del rectangulo 2: "))
    y2 = float(input("Escribe el largo del rectangulo 2: "))

    areauno = area1(x1,y1)
    areados = area2(x2,y2)

    print("El area 1 es: ", areauno)
    print("El area 2 es: ", areados)

    mayor = compara(areauno,areados)
    if mayor == 1:
        print("El area mayor es el Area 1")
    elif mayor == 2:
        print("El area mayor es el Area 2")
    elif mayor == 3:
        print("Las areas son iguales")

    tortol(x1,y1,x2,y2)
# noinspection PyUnresolvedReferences
    turtle.exitonclick()

main()