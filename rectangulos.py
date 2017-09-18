#encoding:UTF-8
#Autor: Ana María López Soto
#Descripción: Calcula el perímetro y área de dos rectangulosm y los dibuja.

import turtle

#Esta función calcula el área del rectangulo.
def calcularArea(base,altura):
   area = base * altura
   return area

#Esta función calcula el perímetro del rectángulo.
def calcularPerimetro(base,altura):
    perimetro = 2* base + 2 * altura
    return perimetro


#Esta función dibuja el rectángulo con las primeras medidas ingresadas.
def dibujarRectangulo1(base,altura):
    turtle.color("blue")
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)


#Esta función dibuja el rectángulo con las segundas medidas ingresadas.
def dibujarRectangulo2(base,altura):
    turtle.color("green")
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)


#Esta función compara las áreas para saber si son iguales o cual es mayor.
def compararAreas(area1,area2):
    if area1 < area2:
        comparacion = str("El área del segundo rectángulo es mayor")
    elif area1 == area2:
        comparacion = str("Ambas áreas son iguales")
    else:
        comparacion: str("El área del primer rectángulo es mayor")
    return comparacion


#Esta función lee las medidas de ambos rectángulos e imprime los cálculos y dibujos correspondientes:
def main():
    base1 = float(input("Inserte la medida de la base del primer rectángulo: "))
    altura1 = float(input("Inserte la medida de la  altura del primer rectángulo: "))
    base2 = float(input("Inserte la medida de la base del segundo rectángulo: "))
    altura2 = float(input("Inserte la medida de la altura del segundo rectángulo: "))
    #Calculo de áreas:
    area1 = calcularArea(base1,altura1)
    area2 = calcularArea(base2,altura2)
    #Cálculo de perímetros:
    perimetro1 = calcularPerimetro(base1,altura1)
    perimetro2 = calcularPerimetro(base2,altura2)
    print("  ")
    print("El perímetro del primer rectángulo es de %.2f unidades" % (perimetro1))
    print("El área el primer rectángulo es de %.2f unidades cuadradas." % (area1))
    print(" ")
    print("El perímetro del segundo rectángulo es de %.2f unidades" % (perimetro2))
    print("El área el segundo rectángulo es de %.2f unidades cuadradas." % (area2))
    print(compararAreas(area1, area2))
    dibujarRectangulo1(base1,altura1)
    dibujarRectangulo2(base2, altura2)
    turtle.exitonclick()
    if base1 <= 0 or base2 <= 0 or altura1 <= 0  or altura2 <= 0:
        print("Error, inserte valores mayores a 0")


main()


