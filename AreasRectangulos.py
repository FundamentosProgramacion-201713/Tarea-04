#encoding: UTF-8
# Autor: Dora Gabriela Lizárraga González - A01229599
# Este programa lee las dimensiones de dos rectángulos, con ellas calcula sus medidas.
# Ya que calcule sus medidas, con estas dibuja ambos rectángulos.

import turtle

# Esta función lee los valores correspondientes de base y altura y con ellos calcula el área del rectángulo.
def calcularArea (baseX,alturaY):
    area = baseX*alturaY
    return area

# Esta función lee los valores correspondientes de base y altura y con ellos calcula el perímetro del rectángulo.
def calcularPerimetro (baseX,alturaY):
    perimetro = (2*baseX)+(2*alturaY)
    return perimetro

# Esta función compara las áreas de ambos rectángulos e indica cuál es mayor o si son iguales.
def compararAreas (area1,area2):
    if area1 > area2:
        areaMayor = "El rectángulo 1 tiene una área mayor que el rectángulo 2."
    elif area2 > area1:
        areaMayor = "El rectángulo 2 tiene una área mayor que el rectángulo 1."
    else:
        areaMayor = "El área de ambos rectángulos es igual."
    return areaMayor

# Esta función lee los valores de base y altura y dibuja el rectángulo en turtle.
def dibujarRectangulo(baseX,alturaY):
    turtle.fd(baseX)
    turtle.left(90)
    turtle.fd(alturaY)
    turtle.left(90)
    turtle.fd(baseX)
    turtle.left(90)
    turtle.fd(alturaY)
    turtle.left(90)

# Esta función lee los valores de las variables, ejecuta las otras funciones e imprime el resultado.
def main():
    print("Introduzca los valores de dos rectángulos para calcular sus medidas.")
    base1 = int(input("Ingrese el valor de la base del primer rectángulo: "))
    altura1 = int(input("Ingrese el valor de la altura del primer rectángulo: "))
    base2 = int(input("Ingrese el valor de la base del segundo rectángulo: "))
    altura2 = int(input("Ingrese el valor de la altura del segundo rectángulo: "))
    baseX = base1
    alturaY = altura1
    area1 = calcularArea(baseX,alturaY)
    perimetro1 = calcularPerimetro(baseX,alturaY)
    baseX = base2
    alturaY = altura2
    area2 = calcularArea(baseX,alturaY)
    perimetro2 = calcularPerimetro(baseX, alturaY)
    print()
    print("--------------------------------")
    print()
    print("Rectángulo 1:")
    print("El área del primer rectángulo vale: ",area1)
    print("El perímetro del primer rectángulo vale: ",perimetro1)
    print()
    print("Rectángulo 2:")
    print("El área del segundo rectángulo vale: ",area2)
    print("El perímetro del regundo rectángulo vale: ",perimetro2)
    print()
    print("--------------------------------")
    print()
    areaMayor = compararAreas(area1,area2)
    print(areaMayor)
    baseX = base1
    alturaY = altura1
    turtle.color("purple")
    dibujarRectangulo(baseX,alturaY)
    baseX = base2
    alturaY = altura2
    turtle.color("orange")
    dibujarRectangulo(baseX, alturaY)
    turtle.exitonclick()

main()