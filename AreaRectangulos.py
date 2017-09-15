#Autor: Joaquin Rios Corvera A01375441
#Encoding: UTF-8

#Este programa imprime el perímetro y área de 2 rectangulos, los dibuja y compara sus áreas

import turtle

#Esta función calcula el área de los rectángulos
def calcularArea(base, altura):
    area = base * altura
    return area

#Esta función calcula el perímetro de los rectángulos
def calcularPerimetro(base, altura):
    perimetro = 2 * base + 2 * altura
    return perimetro

#Esta función compara las áreas de ambos rectángulos
def compararArea(area1, area2):
    if area1<area2:
        resultado = "El segundo rectángulo tiene un área mayor."
    elif area1>area2:
        resultado = "El primer rectángulo tiene un área mayor."
    else:
        resultado = "Ambos rectángulos tienen áreas iguales."
    return resultado

#Esta función dibuja ambos rectángulos
def dibujarRectangulos(base1, altura1, base2, altura2):
    t = turtle.Turtle()

    #Primer rectángulo
    t.forward(base1)
    t.left(90)
    t.forward(altura1)
    t.left(90)
    t.forward(base1)
    t.left(90)
    t.forward(altura1)

    #Crear separación entre rectángulos
    t.penup()
    t.left(90)
    t.forward(base1 + 10)
    t.pendown()

    #Segundo rectángulo
    t.fillcolor("red")
    t.pencolor("red")
    t.forward(base2)
    t.left(90)
    t.forward(altura2)
    t.left(90)
    t.forward(base2)
    t.left(90)
    t.forward(altura2)

    turtle.exitonclick()

def main():
    base1 = float(input("Teclea la base del primer rectángulo: "))
    altura1 = float(input("Teclea la altura del primer rectángulo: "))
    base2 = float(input("Teclea la base del segundo rectángulo: "))
    altura2 = float(input("Teclea la altura del segundo rectángulo: "))

    print("")
    perimetro1 = calcularPerimetro(base1, altura1)
    perimetro2 = calcularPerimetro(base2, altura2)
    area1 = calcularArea(base1, altura1)
    area2 = calcularArea(base2, altura2)
    resultado = compararArea(area1, area2)

    print("El perímetro del primer rectángulo es de %.2f" %perimetro1)
    print("El perímetro del segundo rectángulo es de %.2f" %perimetro2)
    print("")

    print("El área del primer rectángulo es de %.2f" %area1)
    print("El área del segundo rectángulo es de %.2f" %area2)
    print("")

    print(resultado)

    dibujarRectangulos(base1, altura1, base2, altura2)

main()