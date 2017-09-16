#encoding UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: Este programa lee las dimensiones de 2 rectángulos e imprime el area y el perimetro de ambos.
import turtle

#Esta función calcula el área a paritr de los lados que recibe como parámetro
def calculararea(l1, l2):
    area = l1*l2
    return area

#Esta función calcula el perimetro a partir de los lados que recibe como parámetro
def calcularperimetro(l3, l4):
    perimetro= 2*l3+2*l4
    return perimetro

#Esta función compara las áreas de los rectángulos que recibe como parámetro
def compararareas(area1, area2):
    if area1==area2:
        return 'Ambos rectángulos tienen la misma área'
    elif area1>area2:
        return 'El primer rectángulo tiene mayor área'
    return 'El segundo rectángulo tiene mayor área'

#Esta función dibuja con la tortuga ambos rectángulos a partir de los lados que recibe como parámetro.
def dibujarectangulo(l1, l2,l3,l4):
    turtle.color('Red')
    turtle.forward(l1)
    turtle.left(90)
    turtle.forward(l2)
    turtle.left(90)
    turtle.forward(l1)
    turtle.left(90)
    turtle.forward(l2)
    turtle.left(90)
    turtle.penup()
    turtle.forward(l1+50)
    turtle.pendown()
    turtle.color('Blue')
    turtle.forward(l1)
    turtle.left(90)
    turtle.forward(l2)
    turtle.left(90)
    turtle.forward(l1)
    turtle.left(90)
    turtle.forward(l2)
    turtle.left(90)
    turtle.exitonclick()
# La función main lee los lados de los rectángulos y llama a las funciones anteriores para calcular su perimetro y su área para
#  después compararlas, dibujar los rectángulos obtenidos e imprimir las áreas, perimetros, si un rectángulo tiene mayor área
#  o si ambas son iguales.
def main():
    l1=int(input('Ingresa la base del primer rectángulo: '))
    l2 = int(input('Ingresa la altura del primer rectángulo: '))
    l3=int(input('Ingresa la base del segundo rectángulo: '))
    l4 = int(input('Ingresa la altura del segundo rectángulo: '))
    area1= calculararea(l1,l2)
    area2= calculararea(l3,l4)
    perimetro1= calcularperimetro(l1,l2)
    perimetro2= calcularperimetro(l3,l4)
    masgrande= compararareas(area1,area2)
    print(masgrande)
    print('El rectángulo 1 tiene un área de %.2f u^2 y un perimetro de %.2f u' %(area1,perimetro1))
    print('El rectángulo 2 (Azul) tiene un área de %.2f u^2 y un perimetro de %.2f u' % (area2, perimetro2))
    dibujarectangulo(l1,l2,l3,l4)

main()