#encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo A01374942
#Descripción: Calcular el area de dos rectangulos a partir de los datos ingresados por el usuario e imprimir cual tiene mayor area.
import turtle  #Importar la tortuga
def dibujarRectangulos(basea, baseb):     #Dibujar los rectangulos dados las bases por el usuario
    turtle.forward(basea)
    turtle.rt(90)
    turtle.forward(baseb)
    turtle.rt(90)
    turtle.forward(basea)
    turtle.rt(90)
    turtle.forward(baseb)
    turtle.color("green")

def calcularArea(basea, baseb):  #Obtener el area del rectangulo dependiendo los dados por el usuario
    area= (basea*baseb)
    return area

def calcularPerimetro(basea,baseb):  #Obtener el perimetro del rectangulo dependiendolos datos por el usuario
    perimetro=(2*basea)+(2*baseb)
    return perimetro

def main():
    basea1=float(input("Ingresa la base del primer rectangulo "))  #Pedimos al usuario la base1 del primer rectangulo
    baseb1=float(input("Ingresa la altura del primer rectangulo ")) #Pedimos al usuario la base2 del primer rectangulo
    basea2=float(input("Ingresa la base del segundo rectangulo "))  #Pedimos al usuario la base1 del segundo rectangulo
    baseb2=float(input("Ingresa la altura del segundo rectangulo ")) #Pedimos al usuario la base2 del segundo rectangulo
    area1=calcularArea(basea1,baseb1)   #Calculamos el area del primer rectangulo
    perimetro1 = calcularPerimetro(basea1, baseb1) #Calculamos el perimetro del primer rectangulo
    area2=calcularArea(basea2,baseb2) #Calculamos el area del segundo rectangulo
    perimetro2=calcularPerimetro(basea2,baseb2) #Calculamos el perimetro del segundo rectangulo
    dibujarRectangulos(basea1,baseb1) #Dibujamos el primer rectangulo
    dibujarRectangulos(basea2, baseb2) #Dibujamos el segundo rectangulo
    turtle.exitonclick() #Salimos del recuadro de dibujar los dos rectangulos para obtener lo siguiente
    if area1==area2: #Si las areas de los rectangulos son iguales
        print("El area de los 2 rectangulos son iguales %.2f" % area1,"cm^2")
    elif area1>area2: #Si el primer area es mayor al segundo
        print("El area del primer rectangulo es:  %.2f" % area1,"cm^2 y es mayor al segundo rectangulo ")
    else: #Si el segundo area es mayor al primero
        print("El area del segundo rectangulo es:  %.2f"%area2,"cm^2 y es mayor al primer rectangulo")
    if perimetro1==perimetro2: #Si los perimetros de los rectangulos son iguales
        print("El perimetro de los 2 rectangulos son iguales %.2f" % perimetro1,"cm")
    elif perimetro1>perimetro2:#Si el primer perimetro es mayor al segundo
        print("El perimetro del primer rectangulo es %.2f" %perimetro1,"cm y es mayor al segundo rectangulo")
    else:#Si el segundo perimetro es mayor al primero
        print("El perimetro del segundo rectangulo es %.2f" %perimetro1, "cm y es mayor al primer rectangulo")
main() #Llamamos a la funcion main para que realice lo que  tiene dentro de ella