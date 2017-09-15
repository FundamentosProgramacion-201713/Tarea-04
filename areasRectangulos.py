#UTF-8
#Autor: Natalia Meraz Tostado          A01745008
#Descripción: calculas el perimetro y area de dos rectángulos

def calcularPerimetro(base1, altura1):              #Calcula el perimetro de los rectángulos con base y altura
    perimetro1 = (2 * base1) + (2 * altura1)
    return perimetro1

def calcularArea(base1, altura1):                   #Calcula el area de los rectángulos con la base y altura
    area1 = base1 * altura1
    return area1

def calcularMayorArea(area1, area2):                #Compara los valores de las areas para ver cual es el de mayor área
    if area1>area2:
        return area1
    else:
        return area2


import turtle
def dibujarRectangulo(base1, altura1, base2, altura2):  #dibuja los dos rectángulos tomando en cuenta sus medidas
    turtle.shape("turtle")
    turtle.color("red")
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(altura1)
    turtle.left(90)
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(altura1)
    turtle.left(90)
    turtle.color("blue")
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(altura2)
    turtle.left(90)
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(altura2)
    turtle.left(90)
    turtle.exitonclick()

def main():
    base1 = int(input("Base del primer rectángulo: "))
    altura1 = int(input("Altura del primer rectángulo: "))
    base2 = int(input("Base del segundo rectángulo: "))
    altura2 = int(input("Altura del segundo rectángulo: "))
    perimetro1 = calcularPerimetro(base1, altura1)
    area1 = calcularArea(base1, altura1)
    perimetro2 = calcularPerimetro(base2, altura2)
    area2 = calcularArea(base2, altura2)
    print("Perimetro primer rectángulo: ", perimetro1)
    print("Área primer rectángulo: ", area1)
    print("Perimetro segungo rectángulo: ", perimetro2)
    print("Área segundo rectángulo: ", area2)
    print("El rectángulo de mayor área es: ", calcularMayorArea(area1, area2))
    dibujarRectangulo(base1, altura1, base2, altura2)
main()