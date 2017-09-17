#AUTOR: GABRIELA MARIEL VARGAS FRANCO A01745775
#encoding: UTF-8
largo1=int(input("Largo rectangulo 1: "))
ancho1=int(input("Ancho rectangulo 1: "))
largo2=int(input("Largo rectangulo 2: "))
ancho2=int(input("Ancho rectangulo 2: "))

#Leer las dimensiones de un dos rectangulos y calcular su area y perimetro
#Calcula y guarda en la variable areaRect1
def areaRect1(largo1,ancho1):
    areaRect1=largo1*ancho1
    return areaRect1
#Calcula y guarda en la variable periRect1
def periRect1(largo1,ancho1):
    periRect1=(2*largo1)+(2*ancho1)
    return periRect1
#Calcula y guarda en la variable areaRect2

def areaRect2(largo2,ancho2):
    areaRect2=largo2*ancho2
    return areaRect2
#Calcula y guarda en la variable periRect2
def periRect2(largo2,ancho2):
    periRect2=(2*largo2)+(2*ancho2)
    return periRect2

def main():

    a=largo1
    a1=ancho1
    b=largo2
    b2=ancho2
    aR1=areaRect1(largo1,ancho1)
    aR2=areaRect2(largo2,ancho2)
    pR1=periRect1(largo1,ancho1)
    pR2=periRect2(largo2,ancho2)

    print("Area rectangulo 1:", aR1)
    print("Perimetro rectangulo 1:", pR1)
    print("Area rectangulo 2:", aR2)
    print("Perimetro rectangulo 2:",pR2)
#Comparacion para ver que rectangulo tiene mayor area o si son iguales
    if aR1>aR2:
        print("Rectangulo 1 tiene mayor area")
    elif aR2>aR1:
        print("Rectangulo 2 tiene mayor area")
    else:
        print("El area de los dos rectangulos son iguales")

from turtle import(forward,left,shape,color)
#Dibujar rectangulos
shape("turtle")
color("blue")

def dibujarRectangulo1(a,a1):

    forward(a)
    left(90)

    forward(a1)
    left(90)

    forward(a)
    left(90)

    forward(a1)
    left(90)
dibujarRectangulo1(largo1,ancho1)
left(45)
shape("turtle")
color("red")
def dibujarRectangulo2(b,b2):

    forward(b)
    left(90)
    forward(b2)
    left(90)
    forward(b)
    left(90)
    forward(b2)
    left(90)
dibujarRectangulo2(largo2,ancho2)
left(45)


main()

