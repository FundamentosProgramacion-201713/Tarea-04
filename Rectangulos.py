#encode: UTF-8
# Autor: David Ramírez Ríos; A01338802

import turtle

# Calcula el área de un rectángulo
def calcularArea (h, a):

    area = h * a
    return area

# Calcula el perímetro de un rectángulo
def calcularPerimetro (h, a):

    perimetro = 2 * h + 2 * a
    return perimetro




def main ():

    h1 = float (input("Escribe la altura del primer rectángulo:"))
    a1 = float (input("Escribe el largo del primer rectángulo:"))

    h2 = float (input("Escribe la altura del segundo rectángulo:"))
    a2 = float (input("Escribe el largo del segundo rectángulo:"))


    if h1 <= 0 or h2 <= 0 or a1 <= 0 or a2 <= 0:
        print("Error: datos inválidos. ")
    else:
        area1 = calcularArea(h1, a1)
        area2 = calcularArea(h2, a2)
        perimetro1 = calcularPerimetro(h1, a1)
        perimetro2 = calcularPerimetro(h2, a2)

        print("El área del primer rectángulo es de: ", area1)
        print("El perímetro del primer rectángulo es de: ", perimetro1)
        print("El área del segundo rectángulo es de: ",area2)
        print("El perímetro del segundo rectángulo es de: ",perimetro2)

        if area1 > area2:
            print("El primer rectángulo tiene mayor área.")
        elif area1 < area2:
            print("El segundo rectángulo tiene mayor área.")
        else:
            print("Ambas áreas son iguales.")

        turtle.color("red")
        turtle.forward(a1)
        turtle.left(90)
        turtle.forward(h1)
        turtle.left(90)
        turtle.forward(a1)
        turtle.left(90)
        turtle.forward(h1)
        turtle.left(90)
        turtle.penup()
        turtle.forward(a1 + 10)
        turtle.pendown()

        turtle.color("blue")
        turtle.forward(a2)
        turtle.left(90)
        turtle.forward(h2)
        turtle.left(90)
        turtle.forward(a2)
        turtle.left(90)
        turtle.forward(h2)
        turtle.left(90)

        turtle.exitonclick()





main()