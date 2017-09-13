# encode UTF-8
# Autor: Luis Enrique Neri Pérez
# Descripción: Un programa 	que	lea	las	dimensiones	de	dos rectángulos	y	que	calcule	e	imprima	el	perímetro	y	área de ambos
import turtle


def dibujarRectangulo(base1,altura1, base2, altura2): #Función que controla a la tortuga
    turtle.color("green")
    turtle.begin_fill()
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(altura1)
    turtle.left(90)
    turtle.forward(base1)
    turtle.left(90)
    turtle.forward(altura1)
    turtle.left(90)
    turtle.end_fill()
    turtle.color("blue")
    turtle.begin_fill()
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(altura2)
    turtle.left(90)
    turtle.forward(base2)
    turtle.left(90)
    turtle.forward(altura2)
    turtle.left(90)
    turtle.end_fill()

def calcularArea(base, altura): #Función que calcula el Área
    area = base * altura
    return area

def calcularPerimetro(base, altura): #Función que calcula el Perímetro
    perimetro = 2 * base + 2 * altura
    return perimetro


def comprobarAreas(area1, area2):#Función que establece la relación que tienen las ;areas de los dos rectangulos
    if area1 > area2:
        return ("El Rectángulo 1 (%.2f m²) tiene mayor área que el rectángulo 2 (%.2f m²)" % (area1,area2))
    elif area2 > area1:
        return ("El Rectángulo 2 (%.2f m²) tiene mayor área que el rectángulo 2 (%.2f m²)" % (area2, area1))
    else:
        return ("El Rectángulo 1 (%.2f m²) tiene la misma área que el rectángulo 2 (%.2f m²)" % (area1, area2))

def main(): #Función principal
    print("CALCULADORA ÁREA Y PERÍMETRO")
    print("-----------------------------------------")
    print("RECTÁNGULO 1")
    base1 = float(input("Ingrese la medida de la base: "))
    altura1 = float(input("Ingrese la medida de la altura: "))
    area1 = calcularArea(base1, altura1)
    perimetro1 = calcularPerimetro(base1,altura1)

    print("----------------")

    print("RECTÁNGULO 2")
    base2 = float(input("Ingrese la medida de la base: "))
    altura2 = float(input("Ingrese la medida de la altura: "))
    area2 = calcularArea(base2, altura2)
    perimetro2 = calcularPerimetro(base2, altura2)

    print("-----------------------------")
    print("RECTÁNGULO 1")
    print("EL Área es de:", area1, "m² y el Perímetro es de:", perimetro1, "m")
    print("")
    print("RECTÁNGULO 2")
    print("EL Área es de:", area2, "m² y el Perímetro es de:", perimetro2, "m")
    datoAdicional = comprobarAreas(area1,area2)
    print("-----------------------------")
    print(datoAdicional)


    dibujarRectangulo(base1,altura2,base2,altura2)
    turtle.exitonclick()


main()
