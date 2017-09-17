# Autor: Saul Rodrigo Toral Luna
# Matrícula: A01745007

# El usuario ingresa  dimensiones de dos rectángulos
# Y el programa   calculará  e imprimirá el perímetro y área de estos
# Además dibujará con la tortuga de python los rectangulos correspondidentes de acuerdo a los datos

#Importar turtle para dibujar
import turtle

# Función que dibuja los rectangulos correspondientes
def dibujarRectangulos(base1, altura1, base2, altura2):
    turtle.shape("turtle")
    turtle.color("green")
    turtle.width("4")
    turtle.speed(7)
    turtle.fd(base1)
    turtle.lt(90)
    turtle.fd(altura1)
    turtle.lt(90)
    turtle.fd(base1)
    turtle.lt(90)
    turtle.fd(altura1)
    turtle.lt(90)
# Dibujar el segundo rectangulo con diferentes especifiaciones
    turtle.shape("turtle")
    turtle.color("blue")
    turtle.width("4")
    turtle.speed(7)
    turtle.fd(base2)
    turtle.lt(90)
    turtle.fd(altura2)
    turtle.lt(90)
    turtle.fd(base2)
    turtle.lt(90)
    turtle.fd(altura2)
    turtle.lt(90)

# La función calcula el perímetro de los rectangulos de acuerdo a los datos ingresados para cada uno.
def calcularPerimetro(base, altura):
    if base >= 0 and altura>=0:
        perimetro = (base*2) + (altura*2)
    else:
        perimetro = "Con los datos proporcionados no se puede calcular el perímetro"
    return perimetro


# La función calcula el área de los rectangulos de acuerdo a los datos ingresados para cada uno.
def calcularArea(base, altura):
    if base >= 0 and altura>=0:
        area = base * altura
    else:
        area = "Con los datos proporcionados no se puede calcular el área"
    return area


# Función principal que llama a las demás e imprime datos
def main():
# Ingresa los datos del Primer rectangulo
    print("")
    base_Rectangulo_1 = float(input("Ingresa la base del Primer rectangulo: "))
    altura_Rectangulo_1 = float(input("Ingresa la altura del Primer rectangulo: "))
    print("---------------------------------------")
# Imprimir el perimetro y area del primer rectangulo
    perimetro_Rectangulo_1 = calcularPerimetro(base_Rectangulo_1, altura_Rectangulo_1)
    area_Rectangulo_1 = calcularArea(base_Rectangulo_1, altura_Rectangulo_1)
    print("Perímetro del Primer Rectangulo:  %.2f m" % perimetro_Rectangulo_1 )
    print("Área del Primer Rectangulo:  %.2f m2" % area_Rectangulo_1)
    print("---------------------------------------")
# Ingresa los datos del segundo rectangulo
    base_Rectangulo_2 = float(input("Ingresa la base del Segundo rectangulo: "))
    altura_Rectangulo_2 = float(input("Ingresa la altura del Segundo rectangulo: "))
    print("---------------------------------------")
# Imprimir el perimetro y area del primer rectangulo
    perimetro_Rectangulo_2 = calcularPerimetro(base_Rectangulo_2, altura_Rectangulo_2)
    area_Rectangulo_2 = calcularArea(base_Rectangulo_2, altura_Rectangulo_2)
    print("Perímetro del Segundo Rectangulo:  %.2f m" % perimetro_Rectangulo_2)
    print("Área del Segundo Rectangulo: %.2f m2" % area_Rectangulo_2)
#Calcular que rectangulo tiene mayor área o si ambos tienen la misma área
    print("_______________________________________")
    if area_Rectangulo_1 > area_Rectangulo_2:
        print("El Rectangulo 1 tiene mayor área que el segundo")
    elif area_Rectangulo_2 > area_Rectangulo_1:
        print("El Rectangulo 2 tiene mayor área que el primero")
    else:
        print("Ambos tienen la misma área")
    dibujarRectangulos(base_Rectangulo_1,altura_Rectangulo_1,base_Rectangulo_2,altura_Rectangulo_2)
    turtle.exitonclick()
main()
