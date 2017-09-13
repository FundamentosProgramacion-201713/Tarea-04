#coding: UTF-8
#Autor Aaron Tonatiuh Villanueva Guzmán
#Este programa calcula el Índice de Masa Corporal (IMC) del usuario

#Esta función calcula el Índice de Masa Corporal a partir de los datos de entrada. Utiliza la operación preestablecida. 
def calcularIMC(peso,altura):
  imcfuncion=peso / (altura**2)
  return (imcfuncion)

#Esta función lee el peso y la altura del usuario y decide si debe o no procesar el Índice de Masa Corporal. Sí decide procesarlo, va a imprimir el IMC y determinar el estado del usuario a partir de la tabla provista.
def Main():
  pesokg=float(input("Ingrese su peso en kg"))
  alturam=float(input("Ingrese su altura en m"))
  if alturam<=0 or pesokg<=0:
    print("error")
  else:
    imc=calcularIMC(pesokg,alturam)
    print("Su Índice de Masa Corporal es de: %.2f"%imc)
    if imc<=18.5:
      estado="bajo peso"
    elif imc<=25:
      estado="peso normal"
    elif imc>25:
      estado="sobrepeso"
    print("Usted tiene",estado)
  
Main()
