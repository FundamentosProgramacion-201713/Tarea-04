# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Cálculo del perímetro y área de dos rectángulos.

import turtle

# Calcular y guardar en la variable area el area de un rectángulo.
def calcularArea(base, altura):
    area = base * altura
    return area


# Calcular y guardar en la variable perimetro el perimetro de un rectángulo.
def calcularPerimetro(base, altura):
    perimetro = (2*base) + (2*altura)
    return perimetro


# Comparar ambas áreas y guardar la mayor en la variable mayor.
def compararAreas (area1, area2):
    if area1 > area2:
        mayor = area1
    else:
        mayor = area2


# Dibujar un rectángulo con la tortuga.
def dibujarRectangulo (base, altura):
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)


# Función principal:
def main():
    base1 = float(input("Teclea la base del primer rectángulo: "))
    altura1 = float(input("Teclea la altura del primer rectángulo: "))
    base2 = float(input("Teclea la base del segundo rectángulo: "))
    altura2 = float(input("Teclea la altura del segundo rectángulo: "))
    if base1 <= 0 or altura1 <= 0 or base2 <= 0 or altura2 <= 0:
        print ("Error, no insertes 0 ó números negativos. Inténtalo de nuevo.")
        return
    area1 = calcularArea(base1, altura1)
    area2 = calcularArea(base2, altura2)
    perimetro1 = calcularPerimetro(base1, altura1)
    perimetro2 = calcularPerimetro(base2, altura2)
    print ("El primer rectángulo tiene un área de %.2f y un perímetro de %.2f unidades." % (area1, perimetro1))
    print ("El segundo rectángulo tiene un área de %.2f y un perímetro de %.2f unidades." % (area2, perimetro2))
    if area1 == area2:
        print ("Ambas áreas son iguales.")
    else:
        mayor = compararAreas (area1, area2)
        print ("De ambos, es el", mayor, "el que tiene mayor área.")
    turtle.pencolor("red")
    dibujarRectangulo(base1, altura1)
    turtle.penup()
    turtle.forward(2*base1)
    turtle.pendown()
    turtle.pencolor("blue")
    dibujarRectangulo(base2, altura2)
    turtle.exitonclick()

# Ejecutar función principal.
main()
