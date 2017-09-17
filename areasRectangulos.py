#encoding: UTF-8

#Autor: Roberto Téllez Perezyera
"""
Este programa calcula el perímetro y área de dos rectángulos, cuyas dimensiones son dadas por el usuario.
Después, indica cuál es de mayor área o si éstas son iguales, y dibuja los rectángulos.
"""


import turtle


#Calcular el perímetro del rectángulo 1
def calcularPerimetro1(base1, altura1):
    p = 2*base1 + 2*altura1
    return p


#Calcular el perímetro del rectángulo 2
def calcularPerimetro2(base2, altura2):
    p = 2*base2 + 2*altura2
    return p


#Calcular el área del rectángulo 1
def calcularArea1(base1, altura1):
    a = base1 * altura1
    return a


#Calcular el área del rectángulo 2
def calcularArea2(base2, altura2):
    a = base2 * altura2
    return a

#Dibujar los dos rectángulos, con diferente color
def dibujarRects(base1, altura1, base2, altura2):
    turtle.pencolor("red") #Rectángulo 1
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(altura1)
    turtle.left(90)
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(altura1)
    turtle.penup()
    turtle.forward(150)
    turtle.pencolor("blue") #Rectángulo 2
    turtle.pendown()
    turtle.left(90)
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(altura2)
    turtle.left(90)
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(altura2)


#Leer los datos que de el usuario, hacer los cálculos, regresar perímetro, área y dibujar los rectángulos
def main():
    print ("Rectángulo 1:")
    base1 = float(input("base: "))
    altura1 = float(input("altura: "))
    print ("---------------")
    print ("Rectángulo 2:")
    base2 = float(input("base: "))
    altura2 = float(input("altura: "))

    perimetro1 = calcularPerimetro1(base1, altura1)
    perimetro2 = calcularPerimetro2(base2, altura2)
    area1 = calcularArea1(base1, altura1)
    area2 = calcularArea2(base2, altura2)

    print("Rectángulo 1:")
    print("- Perímetro: ", perimetro1, "unidades")
    print("- Área: ", area1, "unidades")
    print("---------------")
    print("Rectángulo 2:")
    print("- Perímetro: ", perimetro2, "unidades")
    print("- Área: ", area2, "unidades")


    print("")
    print("---------------")

    if area1 < area2 :
        print("El área del rectángulo 2 es mayor que el área del rectángulo 1.")
    elif area1 == area2 :
        print("Las áreas de éstos rectángulos son iguales")
    else :
        print("El área del rectángulo 1 es mayor que el área del rectángulo 2.")

    dibujarRects(base1, altura1, base2, altura2)
    turtle.exitonclick()


main()
