#encoding: UTF-8
#Autor :Eduardo Roberto Müller Romero, A01745219
import turtle
def main():
    largo1 = float(input("¿Cuánto mide el largo del rectángulo 1? "))
    ancho1 = float(input("¿Cuánto mide el ancho del rectángulo1? "))
    largo2 = float(input("¿CUánto mide el largo del rectángulo2? "))
    ancho2 = float(input("¿Cuánto mide el ancho del rectángulo2? "))
    dibujarrectangulo(largo1, ancho1)
    dibujarrectangulo(largo2, ancho2)
    perimetro1 = calcularperimetro(largo1, ancho1)
    perimetro2 = calcularperimetro2(largo2, ancho2)
    area1 = calculararea1(largo1, ancho1)
    area2 = calculararea2(largo2, ancho2)
    decidir1 = compararmedidas1(perimetro2, perimetro1)
    decidir2 = compararmedidas2(area1, area2)
    print("Perímetro del rectángulo 1:", perimetro1)
    print("Perímetro del rectángulo 2:", perimetro2)
    print("Ärea del rectángulo 1:", area1)
    print("ÁRea del rectángulo 2:", area2)
    print(decidir1, "y", decidir2)


def calcularperimetro(largo1, ancho1):
    perimetro = (largo1 * 2) + (ancho1 * 2)
    return perimetro

def calcularperimetro2(largo2, ancho2):
    perimetro2 = (largo2 * 2) + (ancho2 * 2)
    return perimetro2
def calculararea1 (largo1, ancho1):
    area1 = largo1 * ancho1
    return area1
def calculararea2(largo2, ancho2):
    area2 = largo2 * ancho2
    return area2

def compararmedidas2(area1, area2):
    if area1 < area2 :
        return "El área del rectángulo 2 es mayor"
    elif area1 > area2 :
        return"El área del rectángulo 1 es mayor"
    elif area2 == area1 :
        return "AMbas áreas son iguales"

def compararmedidas1(perimetro2, perimetro1):
    if perimetro1 < perimetro2 :
        return "El perímetro del rectángulo 2 es mayor"
    elif perimetro2 < perimetro1 :
        return "El perímetro del rectángulo 1 es mayor"
    elif perimetro1 == perimetro2 :
        return "Ambos perímetros son iguales"


def dibujarrectangulo(largo1, ancho1):
    turtle.forward(largo1)
    turtle.left(90)
    turtle.forward(ancho1)
    turtle.left(90)
    turtle.forward(largo1)
    turtle.left(90)
    turtle.forward(ancho1)

def dibujarrectangulo(largo2, ancho2):
    turtle.forward(largo2)
    turtle.left(90)
    turtle.forward(ancho2)
    turtle.left(90)
    turtle.forward(largo2)
    turtle.left(90)
    turtle.forward(ancho2)
main()