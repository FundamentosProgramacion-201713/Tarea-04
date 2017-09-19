#Encoding UTF-8
#Anaid Fernanda Labat González, A01746289
#Calcular y comparar el área y perímetro de dos rectángulos y dibujarlos utilizando turtle 

import turtle
def calcularAreaRectangulo(base, altura): #Se calcula el area de cualquier rectángulo
    area = base*altura
    return area
def calcularPerimetroRectangulo(base, altura):#Se caclula el perímetro de cualquier rectángulo
    perimetro = (2*base)+(2*altura)
    return perimetro
def calcularAreaMayor(areauno, areados):#Se calcula el área mayor entre las áreas ya obtenidas
    areaMayor = areauno
    if areauno<areados:
        areaMayor = areados
    else:
        areaMayor = "Ambas áreas valen lo mismo"
    return areaMayor

def dibujarRectangulo(base, altura):
    turtle.right(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)

#Ingresar medidas del triángulo
def main():
    b1 = float(input("Teclee la base del rectángulo uno: ", ))
    b2 = float(input("Teclee la base del rectángulo dos: ", ))
    h1 = float(input("Teclee la altura del rectángulo uno: ", ))
    h2 = float(input("Teclee la altura del rectángulo dos: ", ))

#Calcular área y perímetro e indicar que rectángulo es mayor
    areaUno = calcularAreaRectangulo(b1,h1)
    areaDos = calcularAreaRectangulo(b2,h2)
    perimetroUno = calcularPerimetroRectangulo(b1,h1)
    perimetroDos = calcularPerimetroRectangulo(b2, h2)
    print("El área del rectángulo uno es: ", areaUno)
    print("El área del rectángulo dos es: ", areaDos)
    print("-------------------------------------------")
    print("El perímetro del rectángulo uno es: ", perimetroUno)
    print("El perímetro del rectángulo dos es: ", perimetroDos)
    print("-------------------------------------------")
    print("El área mayor es el del rectángulo de:", calcularAreaMayor(areaUno, areaDos))


#Dibujar los rectángulos
    turtle.goto(0,0)
    turtle.color("red")
    dibujarRectangulo(b1,h1)
    turtle.color("green")
    dibujarRectangulo(b2,h2)
    turtle.exitonclick()

main()