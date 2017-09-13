#encoding:UTF-8

#Autor: Carlos Pano Hernández
#Descripción: Calcular área y dimensiones de dos rectángulos, así como trazarlos.

#Tortuga
import turtle

    #Rectángulo
def dibujarRectangulo(l,b):
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(b)

#CalcularArea
def calcularArea (l,b):
    area=l*b
    return area

#Calcular perímetro
def calcularPerimetro(l,b):
    perimetro=(2*l)+(2*b)
    return perimetro

#Funcion Main:
def main():

        #Rectángulo 1:
    l1=int(input("Introduzca el lado de su PRIMER rectángulo:"))
    b1=int(input("Introduzca la base de su PRIMER rectángulo:"))
    ar1=calcularArea(l1,b1)
    pr1=calcularPerimetro(l1,b1)

        #Rectágulo 2:
    print("")
    l2=int(input("Introduzca el lado de su segundo rectángulo:"))
    b2=int(input("Introduzca la base de su segundo rectángulo:"))
    ar2=calcularArea(l2,b2)
    pr2=calcularPerimetro(l2,b2)

    #Información
    print("-----------------------------------------------------------------------------------------------------------")
    print("El área de tu rectángulo con las medidas de %d X %d es de: %dm^2. Su perímetro es de: %dm." %(l1,b1,ar1,pr1))
    print("El área de tu rectángulo con las medidas de %d X %d es de: %dm^2. Su perímetro es de: %dm." % (
        l2, b2, ar2, pr2))
    print("-----------------------------------------------------------------------------------------------------------")

    #Compración:
    if ar1>ar2:
        print("El rectángulo 1 tiene MAYOR área.")
    elif ar2>ar1:
        print("El rectángulo 2 tiene mayor área.")
    elif ar1==ar2:
            print("AMBOS rectángulos tienen la misma área.")

    #Tortuga:
    turtle.goto(0,0)
    turtle.color("Green")
    dibujarRectangulo(l1,b2)

    turtle.penup()
    turtle.goto((b2+10),0)
    turtle.pendown()

    turtle.color("Blue")
    dibujarRectangulo(l2,b2)

    turtle.exitonclick()

#LlamadaMain:
main()
