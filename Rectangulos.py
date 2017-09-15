#encoding:UTF-8
#Autor: José Antonio Gómez Mora
#El usuario ingresa las dimensiones de dos rectángulos, el programa regresa el área, perímetro de cada rectángulo, indica cual tiene mayor área y dibuja los rectángulos.

import turtle

#calcula el área de un rectángulo con los parámetros largo y ancho.
def calcularArea(largo, ancho):
    area=largo*ancho
    return area

#calcula el perímetro de un rectángulo con los parámetros largo y ancho.
def calcularPerimetro(largo, ancho):
    perimetro=largo*2+ancho*2
    return perimetro

#dibuja el primer rectángulo con los parámetros turtle, ancho del primer rectángulo y largo del segundo rectángulo.
def dibujarRectangulo1(t,ancho, largo):
    t.penup()
    t.goto(-largo,0)
    t.pendown()
    t.fillcolor("red")
    t.begin_fill()
    t.forward(largo)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(largo)
    t.left(90)
    t.forward(ancho)
    t.end_fill()


#dibuja el segundo rectángulo con los parámetros turtle, ancho del segundo rectángulo y largo del segundo rectángulo.
def dibujarRectangulo2(t,ancho, largo):
    t.penup()
    t.goto(largo,0)
    t.pendown()
    t.fillcolor("blue")
    t.begin_fill()
    t.forward(largo)
    t.left(90)
    t.forward(ancho)
    t.left(90)
    t.forward(largo)
    t.left(90)
    t.forward(ancho)
    t.end_fill()


#función main
def main():

    largoR1=float(input("Ingresa el largo del primer rectángulo: "))
    anchoR1=float(input("Ingresa el ancho del segundo rectángulo: "))

    largoR2=float(input("Ingresa el largo del segundo rectángulo: "))
    anchoR2=float(input("Ingresa el ancho del segundo rectángulo: "))

    #si las medidas de los rectángulos son mayores que 0, calcula area y perimetro de cada rectangulo
    if largoR1>0 and largoR2>0 and anchoR1>0 and anchoR2>0:

        areaR1=calcularArea(largoR1,anchoR1)
        areaR2=calcularArea(largoR2,anchoR2)

        perimetroR1=calcularPerimetro(largoR1,anchoR1)
        perimetroR2=calcularPerimetro(largoR2,anchoR2)

        print("""
        Rectángulo 1 (Rojo):
        Area= %.2f
        Perímetro= %.2f""" % (areaR1, perimetroR1))

        print("""
        Rectángulo 2 (Azul):
        Area= %.2f
        Perímetro= %.2f
        """ % (areaR2, perimetroR2))

        print("------------------------------------------------------------")

        if areaR1 > areaR2:
            print("El rectángulo 1 tiene un área más grande que el rectángulo 2")

        elif areaR1 < areaR2:
            print("El rectángulo 1 tiene un área más grande que el rectángulo 2")

        else:
            print("Los rectángulos tienen áreas iguales")


#si el numero es negativo, imprime mensaje de error.
    else:
        print("Error. Escribe números positivos")


    dibujarRectangulo1(turtle,anchoR1, largoR1)



    dibujarRectangulo2(turtle,largoR2,anchoR2)
    turtle.exitonclick()


main()