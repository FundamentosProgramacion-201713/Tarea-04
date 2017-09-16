#Autor: Mónica Monserrat Palacios Rodríguez
#UTF-8
#Calcular el área y perímetro del rectángulo, calcular el área mayor y dibujar ambos rectángulos.

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


def dibujarRectangulo(base, altura):#Se dibuja el rectángulo con la tortuga
    turtle.right(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)

def main():#Función main
    b1 = float(input("Teclee la base del rectángulo uno: ", ))#Leer los valores y asignarlos a variables
    b2 = float(input("Teclee la base del rectángulo dos: ", ))
    h1 = float(input("Teclee la altura del rectángulo uno: ", ))
    h2 = float(input("Teclee la altura del rectángulo dos: ", ))

    areauno = calcularAreaRectangulo(b1,h1)#Lllamar a las funciones para los valores ya leídos
    areados = calcularAreaRectangulo(b2,h2)
    perimetrouno = calcularPerimetroRectangulo(b1,h1)
    perimetrodos = calcularPerimetroRectangulo(b2, h2)

    print("El área del rectángulo uno es: ", areauno)#Imprimir los resultados
    print("El área del rectángulo dos es: ", areados)
    print("-------------------------------------------")
    print("El perímetro del rectángulo uno es: ", perimetrouno)
    print("El perímetro del rectángulo dos es: ", perimetrodos)
    print("-------------------------------------------")
    print("El área mayor es el del rectángulo de:", calcularAreaMayor(areauno, areados))

    turtle.goto(0,0)#Llamar a la función turtle para que dibuje los rectángulos
    turtle.color("red")
    dibujarRectangulo(b1,h1)

    turtle.color("green")
    dibujarRectangulo(b2,h2)#Dinuja el rectángulo dos

    turtle.exitonclick()
main()