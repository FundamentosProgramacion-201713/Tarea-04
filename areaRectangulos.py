# encoding: UTF-8


# Autor: Iván Alejandro Dumas
# Descripción: Este programa pide las dimensiones de dos rectángulos, calcula las áreas y perimetros de ambos
# compara las áres y determina cual es mayor. Posteriormente dibuja ambos rectángulos con la tortuga de python


# Librerias
from turtle import *


# Función que calcula el áres de un rectángulo
def calcularArea(largo,ancho):
    area = largo*ancho
    return area

# Función que calcula el perímetro de un rectángulo
def calcularP(largo,ancho):
    pmtro = largo*2 + ancho*2
    return pmtro

#Función que dibuja un rectangulo del valor introducido
def dibujarRectangulo(largo,ancho):
    fd(largo)
    rt(90)
    fd(ancho)
    rt(90)
    fd (largo)
    rt(90)
    fd(ancho)
    rt(90) # Regresa a su dirección original

# Función principal
def main():
    largo1 = float(input("Largo del primer rectángulo : "))
    ancho1 = float(input("Ancho del primer rectángulo : "))
    largo2 = float(input("Largo del segundo rectángulo: "))
    ancho2 = float(input("Ancho del segundo rectángulo: "))
    area1 = calcularArea(largo1,ancho1)
    area2 = calcularArea(largo2,ancho2)
    pmtro1 = calcularP (largo1,ancho1)
    pmtro2 = calcularP(largo2,ancho2)
    print ("""
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

El área del primer rectángulo es de %g unidades cuadradas mientras que su perímetro es de %g unidades
Y el área del segundo rectángulo es de %g unidades cuadradas mientras que su perímetro es de %g unidades

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
""" % (area1,pmtro1,area2,pmtro2))
    if area1>area2:
        print ("El primer rectángulo de largo %g y ancho %g tiene mayor área que el segundo rectángulo de largo %g y ancho %g" % (largo1,ancho1,largo2,ancho2))
    elif area2 > area1:
        print("El segundo rectángulo de largo %g y ancho %g tiene mayor área que el primer rectángulo de largo %g y ancho %g" % (largo2, ancho2, largo1, ancho1))
    else:
        print ("El primer rectángulo de largo %g y ancho %g tiene igual área que el segundo rectángulo de largo %g y ancho %g" % (largo1, ancho1, largo2, ancho2) )
    print ("""
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

Ahora dibujaremos ambos rectángulos""")

    n = (largo1 * 1.3)
    penup()
    setpos(-n,50)
    pendown()
    pencolor("red")
    dibujarRectangulo(largo1,ancho1)
    penup()
    n = (largo1*1.3)
    setpos(n, 50)
    pendown()
    pencolor("blue")
    dibujarRectangulo(largo2,ancho2)
    exitonclick()


# Llamar a la función principal
main()