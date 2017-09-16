#encoding: utf-8
#coded by: Jordan Gonzalez Bustamante
#Este programa lee dimensiones de dos rectángulos y calcula perímetro, área y además los dibuja con la tortuga.

from turtle import *
#Esta función calcula el área de los rectángulos
def calculateRectangleArea(largeOne, heightOne, largeTwo, heightTwo):
    areaOne = largeOne * heightOne
    areaTwo = largeTwo * heightTwo
    higher = "del primer rectángulo es mayor"
    if areaTwo > areaOne:
        higher = "del segundo rectángulo es mayor"
    elif areaTwo == areaOne:
        higher = "de ambos rectangulos es igual"
    return (areaOne, areaTwo, higher)
#Y esta otra calcula el perímetro
def calculateRectanglePerimeter(largeOne, heightOne, largeTwo, heightTwo):
    perimeterOne = (largeOne * 2) + (heightOne * 2)
    perimeterTwo = (largeTwo * 2) + (heightTwo * 2)
    return (perimeterOne, perimeterTwo)
#Con los valores dados, esta hace posible la graficación.
def drawRectangle(largeOne, heightOne, largeTwo, heightTwo):
    color("red")
    for i in range(2):
        fd(largeOne)
        right(90)
        fd(heightOne)
        right(90)
    up()
    separation = largeOne * 2
    fd(separation)
    down()
    color("blue")
    for i in range(2):
        fd(largeTwo)
        right(90)
        fd(heightTwo)
        right(90)
    exitonclick()
#Como función principal, llama a las anteriores, y pide los valores para que éstas funcionen.
def main():
    print("Por favor, teclea el largo y ancho de dos rectángulos.")
    largeOne = float(input("Rectángulo 1 : Largo : "))
    heightOne = float(input("Rectángulo 1 : Ancho : "))
    largeTwo = float(input("Rectángulo 2 : Largo : "))
    heightTwo = float(input("Rectángulo 2 : Ancho : "))
    areaOne, areaTwo, higher = calculateRectangleArea(largeOne, heightOne, largeTwo, heightTwo)
    perimeterOne, perimeterTwo = calculateRectanglePerimeter(largeOne, heightOne, largeTwo, heightTwo)
    drawRectangle(largeOne, heightOne, largeTwo, heightTwo)
    print("--------------------------------------------------")
    print("Área rectángulo      1 : %.2f " % areaOne)
    print("Área rectángulo      2 : %.2f " % areaTwo)
    print("--------------------------------------------------")
    print("El área " + higher)
    print("--------------------------------------------------")
    print("Perímetro rectángulo 1 : %.2f " % perimeterOne)
    print("Perímetro rectángulo 2 : %.2f " % perimeterTwo)

    
main()