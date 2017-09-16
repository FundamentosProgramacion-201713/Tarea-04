#encode: UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: programa que lee los lados de 2 rectángulos y entrega el perimetro y el área.

import turtle


def main():
    largo1 = int(input("Teclea el largo del rectángulo 1: "))
    ancho1 = int(input("Teclea el ancho del rectángulo 1: "))
    perimetro1 = calcularPerimetro(largo1, ancho1)
    area1 = calcularArea (largo1, ancho1)
    print("El perimetro del rectángulo 1 es %d cm" % (perimetro1))
    print("El área del rectángulo 1 es %d cm**2" % (area1))
    largo2 = int(input("Teclea el largo del rectángulo 2: "))
    ancho2 = int(input("Teclea el ancho del rectángulo 2: "))
    perimetro2 = calcularPerimetro(largo2, ancho2)
    area2 = calcularArea(largo2, ancho2)
    print("El perimetro del rectángulo 2 es %d cm"% (perimetro2))
    print("El área del rectángulo 2 es %d cm**2"% (area2))
    mayor = compararArea(area1, area2)
    print(mayor)
    dibujarRectangulos(largo1, ancho1, largo2, ancho2)



# Calcula el perimetro de un rectángulo
def calcularPerimetro(largo, ancho):
    perimetro = (largo * 2)+(ancho * 2)
    return perimetro

# Calcula el área de un rectángulo
def calcularArea(largo, ancho):
    area = largo * ancho
    return area

# Compara el área de 2 rectángulos
def compararArea (area1, area2):
    if area1 > area2:
        return "El área del rectángulo 1 es mayor"
    elif area1 == area2:
        return "Los rectángulos tienen la misma área "
    else:
        return "El área del rectángulo 2 es mayor"


# Dibuja dos rectángulos de 2 colores diferentes
def dibujarRectangulos(largo1, ancho1, largo2, ancho2):
    turtle.pencolor("blue")
    turtle.forward(largo1)
    turtle.left(90)
    turtle.forward(ancho1)
    turtle.left(90)
    turtle.forward(largo1)
    turtle.left(90)
    turtle.forward(ancho1)
    turtle.pencolor("red")
    turtle.left(90)
    turtle.forward(largo2)
    turtle.left(90)
    turtle.forward(ancho2)
    turtle.left(90)
    turtle.forward(largo2)
    turtle.left(90)
    turtle.forward(ancho2)
    turtle.exitonclick()

main()