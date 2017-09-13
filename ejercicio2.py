# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
#calcular el area de dos rectangulos
import turtle
def dibujarTriangulo(x, y, z, w): #dibuja el triangulo
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.pencolor("blue")
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(z)
    turtle.left(90)
    turtle.forward(w)
    turtle.left(90)
    turtle.forward(z)
    turtle.exitonclick()
def calcularPerimetro(x, y): #calcula el perimetro
    perimetro = (2 * x) + (2 * y)
    return perimetro
def calcularArea(x, y): #calcula el area
    area = x * y
    return area
def main():
    x1 = float(input("Altura del primer rectangulo: "))
    x2 = float(input("Base del primer rectangulo: "))
    print("")
    y1 = float(input("Altura del segundo rectangulo: "))
    y2 = float(input("Base del segundo rectangulo: "))
    print("")
    print("Área del primer rectangulo:", calcularArea(x1, x2))
    print("Perímetro del primer rectangulo: ", calcularPerimetro(x1, x2))
    print("")
    print("Área del segundo rectangulo:", calcularArea(y1, y2))
    print("Perímetro del segundo rectangulo: ", calcularPerimetro(y1, y2))
    if calcularArea(x1, x2) > calcularArea(y1, y2):
        print("el primer rectangulo es mayor")
    elif calcularArea(x1, x2) < calcularArea(y1, y2):
        print("El segundo rectangulo es mayor")
    else:
        print("su area es igual")
    dibujarTriangulo(x1, x2, y1, y2)
main()