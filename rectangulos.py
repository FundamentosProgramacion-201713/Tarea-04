#UTF-8
#Autor: Nazdira Abigail Cerda del Prado A01375428
#Este programa recibe las dimensiones de dos rectángulos, calcula e imprime el perímetro y área de ambos, y además
#dibuja los rectángulos con diferente color

#Para importar tortuga
import turtle

#Para calcular area1
def calcularAreauno(x,y):
    area=x*y
    return area

#Para calcular perimetro1
def calcularPerimuno(x,y):
    perimetro=(x*2)+(y*2)
    return perimetro

#Para calcular area2
def calcularAreados(a,b):
    area2=a*b
    return area2

#Para calcular perimetro2
def calcularPerimdos(a,b):
    perimetro2=(a*2)+(b*2)
    return perimetro2

#Para dibujar rectángulo 1
def dibujarRect1(x,y):
    import turtle  # Importar Turtle
    turtle.forward(x) #Avanzar "x" unidades
    turtle.left(90)  # Girar 90 grados
    turtle.forward(y) #Avanzar "y" unidades
    turtle.left(90)  # Girar 90 grados
    turtle.forward(x) #Avanzar "x" unidades
    turtle.left(90)  # Girar 90 grados
    turtle.forward(y) #Avanzar "y" unidades

#Para dibujar rectángulo 2
def dibujarRect2(a,b):
    import turtle  # Importar Turtle
    turtle.forward(a) #Avanzar "a" unidades
    turtle.left(90)  # Girar 90 grados
    turtle.forward(b) #Avanzar "b" unidades
    turtle.left(90)  # Girar 90 grados
    turtle.forward(a) #Avanzar "a" unidades
    turtle.left(90) # Girar 90 grados
    turtle.forward(b) #Avanzar "b" unidades

def main():
    #Preguntar valores de largo y ancho de rectángulo 1 y 2 respectivamente
    x=float(input("Dame el valor del largo del rectángulo 1:"))
    y=float(input("Dame el valor del ancho del rectángulo 1:"))
    a=float(input("Dame el valor del largo del rectángulo 2:"))
    b=float(input("Dame el valor del ancho del rectángulo 2:"))
    #Calcular ambas áreas
    area1=float(calcularAreauno(x,y))
    area2=float(calcularAreados(a,b))
    #Calcular ambos perímetros
    perimetro1=float(calcularPerimuno(x,y))
    perimetro2=float(calcularPerimdos(a,b))
    #Imprimir valor de perímetros y áreas
    print("El área del rectángulo 1 es de:",area1,"unidades cuadradas; y su perímetro es de", perimetro1,"unidades.")
    print("El área del rectángulo 2 es de:", area2, "unidades cuadradas; y su perímetro es de", perimetro2, "unidades.")

    #Comparar
    if area1>area2:   #Si el valor de área 1 es mayor a área dos entonces imprimir...
        print("El rectángulo 1 tiene mayor área")
    elif area2>area1:    #Si el valor de área 2 es mayor a área uno entonces imprimir...
        print("El rectánculo 2 tiene mayor área")
    else:
        if area2==area1: #Si las áreas son iguales entonces imprimir...
            print("Ambos rectángulos poseen la misma área")

    #Tortuga
    turtle.goto(0,0) #Colocar turtle en la coordenada 0,0
    turtle.color("Red") #Cambiar color de tortuga a rojo
    dibujarRect1(x,y)#Dibujar rectángulo 1
    turtle.penup() #Levantar pluma
    turtle.goto((x+15),0) #Cambiar coordenada de tortuga 15 unidades a la derecha del anterior
    turtle.pendown() #Bajar pluma
    turtle.color("Green")  #Cambiar color a verde
    dibujarRect2(a,b) #Dibujar rectángulo 2

    turtle.exitonclick() #Salir de pantalla en click


main()