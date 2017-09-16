#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785

import turtle

#Función para validar los datos de entrada del usuario
def validarRectangulo(b, h):
    return b > 0 and h > 0

#Función para calcular el perímetro de un rectángulo
def calcularPerimetro(b, h):
    perimetro = 2 * b + 2 * h
    return perimetro
#Función para calcular el área de un rectángulo
def calcularArea(b, h):
    area = b * h
    return area

#Función para dibujar un rectángulo
def dibujarRectangulo(b, h, t, color):
    t.color(color)
    t.fillcolor(color)

    t.begin_fill()
    t.forward(b)
    t.left(90)

    t.forward(h)
    t.left(90)

    t.forward(b)
    t.left(90)


    t.forward(h)
    t.left(90)
    t.end_fill()


    t.penup()
    t.forward(b * 2)
    t.pendown()

#Función para dibujar ordenadamente los dos rectángulos
def dibujarRectangulos(bA, hA, bB, hB):
    t = turtle.Turtle()
    dibujarRectangulo(bA, hA, t, "red")
    dibujarRectangulo(bB, hB, t, "blue")
    turtle.exitonclick()



def main():
    baseA = float(input("Escriba la base del rectángulo A: "))
    alturaA = float(input("Escriba la altura del rectángulo A: "))

    validacionA = validarRectangulo(baseA, alturaA)

    baseB = float(input("\nEscriba la base del rectángulo B: "))
    alturaB = float(input("Escriba la altura del rectángulo B: "))

    validacionB = validarRectangulo(baseB, alturaB)


    if validacionA and validacionB:
        perimetroA = calcularPerimetro(baseA, alturaA)
        perimetroB = calcularPerimetro(baseB, alturaB)

        areaA = calcularArea(baseA, alturaA)
        areaB = calcularArea(baseB, alturaB)

        print("\nPerímetro del rectángulo A: ", perimetroA)
        print("Perímetro del rectángulo B: ", perimetroB)

        print("\nÁrea del rectángulo A: ", areaA)
        print("Área del rectángulo B: ", areaB)

        if areaA > areaB:
            print("\nEl rectángulo A tiene una área mayor")

        elif areaB > areaA:
            print("\nEl rectángulo B tiene una área mayor")

        else:
            print("\nLos rectángulos A y B tienen un área igual")

        dibujarRectangulos(baseA, alturaA, baseB, alturaB)

    else:
        print("Ha introducido datos inválidos")

main()