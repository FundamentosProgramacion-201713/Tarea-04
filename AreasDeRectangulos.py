#encoding: UTF-8
#Autor: Ángel Guillermo Ortiz González
#Matrícula: A01745998
#Descripción: Lee las dimensiones de dos rectángulos, calcula e imprime el perímetro y área de ambos.

import turtle

#calcula el área de un rectángulo
def calcularArea(largo,ancho):
    area = largo * ancho
    return area

#calcula el perímetro de un rectángulo
def calcularPerimetro(largo,ancho):
    perimetro = largo * 2 + ancho * 2
    return perimetro

#dibuja un rectángulo
def dibujarRectangulo(largo,ancho):
    turtle.forward(largo)
    turtle.left(90)
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(largo)
    turtle.left(90)
    turtle.forward(ancho)
    turtle.left(90)

def main():
    largo1 = float(input("Inserte el largo del primer rectángulo: "))
    ancho1 = float(input("Inserte el ancho del primer rectángulo: "))
    largo2 = float(input("Inserte el largo del segundo rectángulo: "))
    ancho2 = float(input("Inserte el ancho del segundo rectángulo: "))

    area1 = calcularArea(largo1,ancho1)
    area2 = calcularArea(largo2,ancho2)

    perimetro1 = calcularPerimetro(largo1,ancho1)
    perimetro2 = calcularPerimetro(largo2, ancho2)

    print("------------------------------------------")
    if largo1 <= 0 or largo2 <= 0 or ancho1 <= 0 or ancho2 <=0:
        print("ERROR. Inserte valores válidos.")
    else:
        print("El área del primer rectángulo es de %.2f unidades cuadradas." % (area1))
        print("El perímetro del primer rectángulo es de %.2f unidades." % (perimetro1))
        print("------------------------------------------")
        print("El área del segundo rectángulo es de %.2f unidades cuadradas." % (area2))
        print("El perímetro del segundo rectángulo es de %.2f unidades." % (perimetro2))
        print("------------------------------------------")
        if area1 > area2:
            print("El área del primer rectángulo es mayor que el área del segundo rectángulo.")
        elif area2 > area1:
            print("El área del segundo rectángulo es mayor que el área del primer rectángulo.")
        else:
            print("Las áreas de los dos rectángulos son iguales.")
        turtle.shape("turtle")
        turtle.color("red")
        dibujarRectangulo(largo1, ancho1)
        turtle.color("green")
        dibujarRectangulo(largo2, ancho2)
        turtle.exitonclick()

main()