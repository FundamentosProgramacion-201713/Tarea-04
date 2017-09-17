#encoding: UTF-8

# Autor: Edgar Alexis González Amador, A01746540
# Descripcion: Programa que calcula el area y el perimtetro de dos rectangulod, los dibuja e indica el mayor.
import turtle

#Esta función, calcula el area de un rectangulo, a partir de los valores base y altura ingresados.
def calcularArea (base, altura):
    Area = base * altura
    return Area

#Esta función, permite calcular el perimetro de un rectangulo, al introducir su base y altura.
def calcularPerimetro (base, altura):
    Perimetro = (base * 2) + (altura * 2)
    return Perimetro

#Esta función, permite dibujar con turtle un cuadrado, a partir de su base y altura.
def dibujarRectangulo (base, altura):
    turtle.forward (base)
    turtle.left (90)
    turtle.forward (altura)
    turtle.left (90)
    turtle.forward (base)
    turtle.left (90)
    turtle.forward (altura)
    turtle.left (90)
    turtle.forward(base)

#Esta función, nos permite determinar, mediante una cunción "if", cual es el area mayor de dos ingresadas.
def compararAreas (area1, area2):
    resultadoComparacion = "Las areas son iguales"
    if area1 > area2:
        resultadoComparacion = "El area del rectangulo 1, es mayor"
    elif area2 > area1:
        resultadoComparacion = "El area del rectangulo 2, es mayor"
    return resultadoComparacion

#Finalmente, esta es la función main, la cual realiza la solicitud de los valores de entrada: base y altura; y utiliza estos valores en ls funciones declaradas anteriormente
#La función, tambien imprime en pantalla los resultados obtenidos y diibuja los rectangulos.
def main():
    #Solicitud de valores: base y altura, de ambos rectangulos
    print("Las unidades introducidas se leen en pixeles.")
    print("RECTANGULO 1")
    print("")
    baseRec1 = int(input("Base: "))
    alturaRec1 = int(input("Altura: "))
    print("")
    print("RECTANGULO 2")
    print("")
    baseRec2 = int(input("Base: "))
    alturaRec2 = int(input("Altura: "))

    #Uso de las funciones creadas anteriormmente
    areaRec1 = calcularArea (baseRec1, alturaRec1)
    areaRec2 = calcularArea (baseRec2, alturaRec2)
    perimetroRec1 = calcularPerimetro (baseRec1, alturaRec1)
    perimetroRec2 = calcularPerimetro (baseRec2, alturaRec2)

    #Impresion de resultados
    print("El primer rectangulo tiene:")
    print(areaRec1, "m^2 de Area")
    print(perimetroRec1, "m de Perimetro")
    print("")
    print("El segundo rectangulo tiene:")
    print(areaRec2, "m^2 de Area")
    print(perimetroRec2, "m de Perimetro")
    print("")
    resultadoComparacion = compararAreas(areaRec1, areaRec2)
    print(resultadoComparacion)

    #Dibujo de rectangulos
        #Para separar los dibujos de ambos rectangulos, se colocaron algunas intrucciónes de turtle, que permitieran separarlos.
    turtle.penup()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.pendown()
    turtle.color("red")
    dibujarRectangulo(baseRec1, alturaRec1)
    turtle.penup()
    turtle.forward (200)
    turtle.pendown()
    turtle.color("blue")
    dibujarRectangulo(baseRec2, alturaRec2)
    turtle.exitonclick()

main()