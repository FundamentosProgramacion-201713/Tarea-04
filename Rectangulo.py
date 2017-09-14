#Javier Pascal A01375925
import turtle

def Calcular_Area(base_1, altura_1, base_2, altura_2): #Aqui calculamos el area de los rectangulos con su base y altura
    area_1=base_1*altura_1
    area_2=base_2*altura_2
    return area_1, area_2
def Calcular_Perimetro(base_1, altura_1, base_2, altura_2):#Aqui calculamos el perimetro de los rectangulos con su base y altura
    perimetro_1=(2*base_1)+(2*altura_1)
    perimetro_2 = (2 * base_2) + (2 * altura_2)
    return perimetro_1,perimetro_2
def dibujar_Rectangulos(base_1, altura_1, base_2, altura_2): #En esta parte la tortuga dibuja los rectangulos
    turtle.bgcolor("black")
    turtle.setpos(100, 0)
    turtle.pencolor("red")
    turtle.fd(base_1)
    turtle.lt(90)
    turtle.fd(altura_1)
    turtle.lt(90)
    turtle.fd(base_1)
    turtle.lt(90)
    turtle.fd(altura_1)
    turtle.lt(90)
    turtle.penup()
    turtle.setpos(-100, 0)
    turtle.pencolor("blue")
    turtle.pendown()
    turtle.fd(base_2)
    turtle.rt(90)
    turtle.fd(altura_2)
    turtle.rt(90)
    turtle.fd(base_2)
    turtle.rt(90)
    turtle.fd(altura_2)
    turtle.rt(90)

def main(): #Aqui leemos los lados del rectangulo y llamamos a las demas funciones para al final imprimir los valores de las funciones y dibujar
    altura_1= int(input("Dame la altura del primer rectangulo: "))
    base_1 = int(input("Dame la base del primer rectangulo: "))
    altura_2 = int(input("Dame la altura del segundo rectangulo: "))
    base_2 = int(input("Dame la base del segundo rectangulo: "))
    area_1, area_2=Calcular_Area(base_1,altura_1,base_2,altura_2)
    perimetro_1,perimetro_2=Calcular_Perimetro(base_1, altura_1, base_2, altura_2)
    print("El area del rectangulo uno es: ", area_1)
    print("El area del rectangulo dos es: ", area_2)
    print("El perimetro del rectangulo uno es: ", perimetro_1)
    print("El perimetro del rectangulo dos es: ", perimetro_2)
    if area_1>area_2:
        print("El area mayor es la del rectangulo uno: ", area_1)
    if area_1==area_2:
        print("Las areas son iguales")
    else:
        print("El area mayor es la del rectangulo dos: ", area_2)
    if perimetro_1>perimetro_2:
        print("El area mayor es la del rectangulo uno: ", perimetro_1)
    if perimetro_1==perimetro_2:
        print("Los perimetros son iguales")
    else:
        print("El permietro mayor es la del rectangulo dos: ", perimetro_2)
    draw = input('Quieres que dibuje los rectangulos? (Si, No) ')
    if draw == "Si" or "si":
        dibujar_Rectangulos(base_1, altura_1, base_2, altura_2)
    else:
        print("ni queria ")


main()
turtle.done()


