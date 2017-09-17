#enconding: UTF-8
#Alejandro Chávez Campos, A01374974
#Este programa calcula el perimetro, area de dos rectangulos y los dibuja.
import turtle

def calcularArea(ancho, largo): #Calcula el área
    area=ancho*largo
    return area


def calcularPerimetro(ancho, largo): #Calcula el perímetro
    perimetro=(2*ancho)+(2*largo)
    return perimetro


def calcularRelacionEntreAreas(area1, area2):#Calcula la relación entre las áreas
    if area1==area2 :
        relacionEntreAreas= "El area del rectángulo 1 es igual a la del rectángulo 2"
        return relacionEntreAreas
    elif area1>area2:
            relacionEntreAreas= "El area del rectángulo 1 es mayor a la del rectángulo 2"
            return relacionEntreAreas
    else:
        relacionEntreAreas="El área del rectángulo 2 es mayor a la del rectángulo 1"
        return relacionEntreAreas


def dibujarRectángulo(largo, ancho,pencolor):#Dibuja los rectángulos
    turtle.pencolor(pencolor)
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(largo)
    turtle.left(90)
    turtle.forward(ancho)
    turtle.left(90)
    turtle.forward(largo)
    turtle.left(90)


def main(): #Programa principal
    print ("Rectángulo 1")
    ancho =float(input("Dame el ancho: "))
    largo= float (input("Dame el largo: "))
    area1= calcularArea(ancho,largo)
    perimetro1= calcularPerimetro(ancho,largo)
    pencolor="red"
    dibujarRectángulo(largo, ancho,pencolor)

    print ()
    print ("Rectángulo 2")

    ancho = float(input("Dame el ancho: "))
    largo=float(input("Dame el largo: "))
    pencolor="green"
    dibujarRectángulo(largo,ancho, pencolor)

    area2= calcularArea(ancho, largo)
    perimetro2=calcularPerimetro(ancho, largo)
    print ("El área del rectángulo 1 es :",area1)
    print ("El área del rectángulo 2 es :",area2)
    print ("El perímetro del rectángulo 1 es :",perimetro1)
    print ("El perímetro del rectángulo 2 es: ",perimetro2)
    relacionEntreAreas= calcularRelacionEntreAreas (area1,area2)
    print (relacionEntreAreas)
    turtle.exitonclick()



main ()
