#encoding: UTF-8
#Autor Aaron Tonatiuh Villanueva Guzmán
import turtle
  
def calcularArea(ancho,largo):
  areafuncion=ancho*largo
  return(areafuncion)

def calcularPerimetro(ancho,largo):
  perimetrofuncion=(2*ancho)+(2*largo)
  return(perimetrofuncion)

def diferenciaareas(areaA,areaB):
  if areaA<areaB:
    mayor="El primer rectángulo tiene mayor área"
  elif areaA>areaB:
    mayor="El segundo rectángulo tiene mayor área"
  else: 
    mayor="Ambos rectángulos tienen la misma área"
  return(mayor)

def dibujarrectangulo(ancho,largo):
  turtle.begin_fill()
  turtle.forward(ancho)
  turtle.right(90)
  turtle.forward(largo)
  turtle.right(90)
  turtle.forward(ancho)
  turtle.right(90)
  turtle.forward(largo)
  turtle.color("green")
  turtle.end_fill()
  
def Main():
  anchoA=float(input("Ingrese el ancho del primer rectángulo"))
  largoA=float(input("Ingrese el largo del primer rectángulo"))
  anchoB=float(input("Ingrese el ancho del segundo rectángulo"))
  largoB=float(input("Ingrese el largo del segundo rectángulo"))
  areaA=calcularArea(anchoA,largoA)
  areaB=calcularArea(anchoB,largoB)
  perimetroA=calcularPerimetro(anchoA,largoA)
  perimetroB=calcularPerimetro(anchoB,largoB)
  rectangulomayor=diferenciaareas(areaA,areaB)
  dibujarrectangulo(anchoA,anchoB)

Main()

