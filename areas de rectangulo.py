#encoding: UTF-8
#Autor Aaron Tonatiuh Villanueva Guzmán
#Este programa permite conocer el área y el perimetro de dos rectángulos así como cuál de los dos tiene un área mayor. Además, permite visualizar ambos rectángulos.

import turtle
  
#Esta función calcula el área de un rectángulo al multiplicar el ancho por el largo.
def calcularArea(ancho,largo):
  areafuncion=ancho*largo
  return(areafuncion)

#Esta función calcula el perimetro de un rectángulo al sumar el doble del ancho y del largo.
def calcularPerimetro(ancho,largo):
  perimetrofuncion=(2*ancho)+(2*largo)
  return(perimetrofuncion)

#Esta función determina cual de las dos áreas de los rectángulos es mayor.
def elegirareamayor(areaA,areaB):
  if areaA>areaB:
    mayor="El primer rectángulo tiene mayor área"
  elif areaA<areaB:
    mayor="El segundo rectángulo tiene mayor área"
  else: 
    mayor="Ambos rectángulos tienen la misma área"
  return(mayor)

#Esta función permite visualizar los rectángulos con ayuda de la tortuga. Además, no solo recibe los lados del rectángulo al poder darle un color de relleno.
def dibujarrectangulo(ancho,largo,color):
  turtle.pencolor("black")
  turtle.begin_fill()
  turtle.forward(largo)
  turtle.right(90)
  turtle.forward(ancho)
  turtle.right(90)
  turtle.forward(largo)
  turtle.right(90)
  turtle.forward(ancho)
  turtle.right(90)
  turtle.forward(largo)
  turtle.color(color)
  turtle.end_fill()

#Esta función permite separar ambos rectángulos para obtener una mejor visualización
def dibujarseparacion(espacio):
  turtle.penup()
  turtle.forward(espacio)
  turtle.pendown()
  
#Esta función lee ancho y largo de ambos rectángulos para poder llamar a las funciones necesarias. Además, imprime el resultado de las funciones con formato y comienza la visualización de los rectángulos. Maneja los datos principales.
def Main():
  anchoA=float(input("Ingrese el ancho del primer rectángulo"))
  largoA=float(input("Ingrese el largo del primer rectángulo"))
  anchoB=float(input("Ingrese el ancho del segundo rectángulo"))
  largoB=float(input("Ingrese el largo del segundo rectángulo"))
  areaA=calcularArea(anchoA,largoA)
  areaB=calcularArea(anchoB,largoB)
  perimetroA=calcularPerimetro(anchoA,largoA)
  perimetroB=calcularPerimetro(anchoB,largoB)
  rectangulomayor=elegirareamayor(areaA,areaB)
  print("El área del primer rectángulo es de %.2f unidades"% areaA)
  print("El área del segundo rectángulo es de %.2f unidades"% areaB)
  print("El perimtero del primer rectángulo es de %.2f unidades"% perimetroA)
  print("El perimetro del segundo rectángulo es de %.2f unidades"% perimetroB)
  print(rectangulomayor)
  dibujarrectangulo(anchoA,largoA,"red")
  dibujarseparacion(largoA)
  dibujarrectangulo(anchoB,largoB,"blue")
  
Main()
