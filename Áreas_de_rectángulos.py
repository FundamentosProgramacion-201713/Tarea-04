#Pedro Cortés Soberanes A01374919
#Función: calcular area y perimetro de dos rectangulos, decir cual area es mayor y dibujarlos

import turtle

#Calcular perimetro
def calcularPerimetro(base,altura):
    perimetro = (base*2)+(altura*2)
    return perimetro

#Calcular Area
def calcularArea(base,altura):
    area = base*altura
    return area

#Dubijar Rectangulos
def dibujarRectangulos (base,altura):
    turtle.forward(base)
    turtle.lt(90)
    turtle.forward(altura)
    turtle.lt(90)
    turtle.forward(base)
    turtle.lt(90)
    turtle.forward(altura)


def main():
    base1 = float(input("Teclea la base del rectángulo 1: "))
    altura1 = float(input("Teclea la altura del rectángulo 1: "))
    base2 = float(input("""
Teclea la base del rectángulo 2: """))
    altura2 = float(input("Teclea la altura del rectángulo 2: "))
    arectangulo1 = calcularArea(base1,altura1)
    arectangulo2 = calcularArea(base2,altura2)
    prectangulo1 = calcularPerimetro(base1, altura1)
    prectangulo2 = calcularPerimetro(base2, altura2)
    print(""" 
 -Área rectángulo 1:""", arectangulo1)
    print(" -Perimetro rectángulo 1:", prectangulo1)
    print(""" 
 -Área rectángulo 2:""", arectangulo2)
    print(" -Perimetro rectángulo 2:", prectangulo2)
    if arectangulo1==arectangulo2:
        print ("""
        - Las áreas son iguales -""")
    else:
        if arectangulo1>arectangulo2:
             print ("""
        - El área del Rectángulo 1 es mayor -""")
        else:
            print ("""
        - El área del Rectángulo 2 es mayor -""")
    turtle.color("red")
    dibujarRectangulos(base1,altura1)
    turtle.penup()
    turtle.goto(-150, 0)
    turtle.pendown()
    turtle.right(90)
    turtle.color("blue")
    dibujarRectangulos(base2, altura2)


main()

turtle.exitonclick()