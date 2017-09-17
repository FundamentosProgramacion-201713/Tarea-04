#Autor: Maria Fernanda Torres Velazquez A01746537
#El programa lee	las	dimensiones	de	dos	rectángulos	y	que	calcule	e	imprima	el	perímetro	y	área	de	ambos,
# imprime el rectangulo con mayor area y dibuja ambos con las medias proporcinadas por el usuario

import turtle
#Calcula y devuelve el area del rectangulo despues de recibir sus medidas
def calcularAreaRectangulo (b,h):
    a= b*h

    return a

#Calcula y devuelve el perimetro del rectangulo despues de recibir sus medidas
def calcularPerimetroRectangulo (b,h):
    p = (b * 2) + (h *2)
    return p

#Compara el area de ambos rectangulos y regresa la mayor
def compararRectangulos (a1,a2):

    if a1>a2:
        g = ("Area mayor: rectangulo 1")

    elif a1<a2:
        g =("Area mayor: rectangulo 2")

    elif a1 == a2:
        g =("Las areas son iguales")

    return (g)

#Funcion que recibe los valores de area y altura y regresa el dibujo del triangulo 1
def dibujarRectangulo1 (h,b):
    import turtle
    wn = turtle.Screen()
    wn.bgcolor('black')
    dibujo= turtle.Turtle()
    dibujo.color('purple')
    dibujo.pensize(2)
    dibujo.forward(h)
    dibujo.left(90)
    dibujo.forward(b)
    dibujo.left(90)
    dibujo.forward(h)
    dibujo.left(90)
    dibujo.forward(b)
    dibujo.left(90)

#Funcion que recibe los valores de area y altura y regresa el dibujo del triangulo 2
def dibujarRectangulo2(h, b):
    import turtle
    wn = turtle.Screen()
    wn.bgcolor('black')
    dibujo = turtle.Turtle()
    dibujo.color('pink')
    dibujo.pensize(2)
    dibujo.right(270)
    dibujo.forward(h)
    dibujo.left(90)
    dibujo.forward(b)
    dibujo.left(90)
    dibujo.forward(h)
    dibujo.left(90)
    dibujo.forward(b)
    dibujo.left(90)

#Funcion principal
def main():
    print ("Recangulo 1")
    print ("-----------")
    b1= (int(input(" Introduce la longitud de la base  : ")))
    h1 = (int(input("Introduce la longitud de la altura: ")))
    p1= calcularPerimetroRectangulo(b1,h1)
    a1= calcularAreaRectangulo (b1,h1)


    print ("")
    print("")
    print ("Recangulo 2")
    print ("-----------")
    b2 = (int(input("Introduce la longitud de la base  : ")))
    h2 = (int(input("Introduce la longitud de la altura: ")))
    p2 = calcularPerimetroRectangulo(b2, h2)
    a2 = calcularAreaRectangulo(b2, h2)

    print ("")
    print("")
    print("--------------------------------------")
    print(" El perimetro del rectangulo 1 es: ", p1)
    print(" El  area  del  rectangulo   1 es: ", a1)


    print("--------------------------------------")
    print(" El perimetro del rectangulo 2 es: ", p2)
    print(" El  area  del  rectangulo   2 es: ", a2)

    print("")
    print("")
    print("--------------------------------------")
    mayor= compararRectangulos(a1,a2)
    print (mayor)

    dibujarRectangulo1 (h1,b1)

    dibujarRectangulo2 (h2,b2)

    turtle.exitonclick()


main()




