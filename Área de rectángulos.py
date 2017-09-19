#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Mátricula: A01376152
#Descripción: Calcular el área y el perímetro de dos rectangulos

import turtle

#Calcular el área de los rectangulos.

def calcularA(altura, base):
    area=altura*base
    return area

#Calcular el perímetro de los rectangulos

def calcularP(altura, base):
    perimetro=(2*altura)+(2*base)
    return perimetro

#Dibuja los rectangulos con la tortuga

def dibujarRec(altura, base):
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    return turtle

#Comparación entre las areas y mención de cual es mayor

def compararA(area1, area2):
     if area1==area2:
         comparacion="Los rectángulos son iguales."
     elif area1>area2:
         comparacion="El rectángulo A es más grande que el rectángulo B."
     else:
         comparacion="El rectángulo B es más grande que el rectángulo A."
     return comparacion

#Función principal

def main():
     altura= float(input("Inserte la altura del rectángulo A: "))
     base= float(input("Inserte la base del rectángulo A: "))
     altura1 = float(input("Inserte la altura del rectángulo B: "))
     base1 = float(input("Inserte la base del rectángulo B: "))
     turtle.color("blue")
     dibujarRec(altura,base)
     turtle.color("red")
     dibujarRec(altura1, base1)
     print("")
     print("El área del rectángulo A es: %.2f" %calcularA(altura, base))
     print("El perímetro del rectángulo A es: %.2f" %calcularP(altura, base))
     print("El área del rectángulo B es: %.2f" %calcularA(altura1, base1))
     print("El perímetro del rectángulo B es: %.2f" %calcularP(altura1, base1))
     print("")
     print(compararA(calcularA(altura, base), calcularA(altura1, base1)))
     turtle.exitonclick()

main()