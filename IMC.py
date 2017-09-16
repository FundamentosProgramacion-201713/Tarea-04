#Autor: Jose Heinz Moller Santos
#Descripción: Este programa es para calcular el IMC de las personas.

#calcular IMC:
def calcularElIMC(peso,estatura):
 indiceMasa=peso/(estatura**2)
 return indiceMasa

def main():
 peso=float(input("Introduzca su peso en kg:"))
 estatura=float(input("Introduzca su estatura en metros:"))

 if peso or estatura <= 0:
     print("ERROR")

 print("           ")

 IMC=float(calcularElIMC(peso,estatura))

 if IMC<18.5:
     print("Estas de bajo peso")
 elif 25>=IMC>=18.5:
     print("Estas normal")
 elif IMC>25:
     print("Visite medico, estas obeso")
main()