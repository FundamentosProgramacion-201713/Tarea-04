#encoding: UTF-8
#Gerardo Arturo Valderrama Quiroz
#A01374994
#Programa que calcula el area y el perimetro de dos rectángulos, compara el area, y los dibuja
import turtle

#Funcion que calcula el area
def calcularArea(lado, ancho):
    area = lado * ancho
    return area

#Función que calcula el perimetro
def calcularPerimetro(lado, ancho):
    perimetro = 2*lado + 2*ancho
    return perimetro

#Funcion que compara el area de los rectangilos
def compararRectangulo(area1, area2):
    if area1 > area2:
        return "El area del rectangulo 1 es mayor que la del rectangulo 2"
    elif area2 > area1:
        return "El area del rectangulo 2 es mayor que la del rectangulo 1"
    else:
        return "El area del rectangulo 1 es igual que la del rectangulo 2"

#Funcion que dibuja ambos retangulos usando turtle.py
def dibujarRectangulos(largo1,ancho1,largo2,ancho2):
    turtle.penup()
    turtle.setpos(-100,0)
    turtle.pendown()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.forward(largo1)
    turtle.left(90)
    turtle.forward(ancho1)
    turtle.left(90)
    turtle.forward(largo1)
    turtle.left(90)
    turtle.forward(ancho1)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(largo1+30)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.forward(largo2)
    turtle.left(90)
    turtle.forward(ancho2)
    turtle.left(90)
    turtle.forward(largo2)
    turtle.left(90)
    turtle.forward(ancho2)
    turtle.left(90)
    turtle.end_fill()
    turtle.exitonclick()

#Funcion principal main que lee, procesa e imprime datos
def main():
    print("Rectangulo 1")
    largo1 = float(input("Da la medida del largo: "))
    ancho1 = float(input("Da la medida del ancho: "))
    print("Rectangulo 2")
    largo2 = float(input("Da la medida del largo: "))
    ancho2 = float(input("Da la medida del ancho: "))
    print("El perímetro del rectángulo 1 es de: %.2f" % calcularPerimetro(largo1, ancho1))
    print("El area del rectángulo 1 es de: %.2f" % calcularArea(largo1,ancho1))
    print("El perímetro del rectángulo 2 es de: %.2f" % calcularPerimetro(largo2, ancho2))
    print("El area del rectángulo 2 es de: %.2f" % calcularArea(largo2, ancho2))
    print(compararRectangulo(calcularArea(largo1,ancho1),calcularArea(largo2,ancho2)))
    dibujarRectangulos(largo1,ancho1,largo2,ancho2)

main()