#encoding: UTF-8
#Autor: Rodrigo Rivera Salinas
#Descripción: Comparar rectangulos dados por el usuario y hacerlos
import turtle  #importar a la tortuga
def dibujarRectangulo(base, altura):     #Dada la altura y la base de los rectangulos se dubujaran
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.left(90)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(altura)
    turtle.color("blue")

def calcularA(base, altura):  #sacar el Area dependiendo de los datos dados
    return (base*altura)

def calcularPeri(base, altura):  #sacar el perimetro dependiendo de los datos dados
    return(2*base)*(2*altura)

def main():
    baseUno=float(input("Dar base del primer rectangulo "))  #pedir base uno
    alturaUno=float(input("Dar altura del primer rectangulo ")) #pedir altura 1
    baseDos=float(input("Dar base del segundo rectangulo "))  #pedir base dos
    alturaDos=float(input("Dar altura del segundo rectangulo ")) #pedir añtura dos
    areaUno=calcularA(baseUno,alturaUno)   #calcular area uno
    periUno = calcularPeri(baseUno, alturaUno) #calcular perimetro uno
    areaDos=calcularA(baseDos,alturaDos) #calcular area dos
    periDos=calcularPeri(baseDos,alturaDos) #calcular perimetro 2
    dibujarRectangulo(baseUno,alturaUno) #dibujar rectangulo con los datos uno
    dibujarRectangulo(baseDos, alturaDos) #dibujar rectangulo con los datos dos
    turtle.exitonclick() #salir del recuadro donde se dubujaron los rectangulos
    if areaUno==areaDos: #si las areas son iguales
        print("Las area son iguales %.2f"%areaUno)
    elif areaUno>areaDos: # si el area uno es mayor a la dos
        print("El area del primer rectangulo es:  %.2f" % areaUno, "y es mayor al segundo ")
    else: #si el area dos es mayor a la uno
        print("El area del segundo es:  %.2f"%areaDos, "y es mayor al primero ")
main()