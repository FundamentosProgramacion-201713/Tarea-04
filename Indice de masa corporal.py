#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139
#Este programa recibe el peso en kg y la altura en metros para calcular el IMC.

#Esta funcion calcula el Indice de Masa Corporal.
def calcularIMC(peso, altura):
    imc=peso/(altura**2)
    return imc

#El IMC se analiza y se clasifica a el individuo en un estado.
def calcularEstado(imc):
    if imc<18.5:
        estado="Bajo de peso."
    elif imc>=18.5 and imc<=25:
        estado="Peso normal."
    else:
        estado="Sobrepeso."
    return estado

def main():
    peso=float(input("Ingrese el peso en kilogramos: "))
    altura=float(input("Ingrese la altura en metros: "))
   #Se evalua si los datos datos al peso y altura son correctos.
    if (peso<=0) and (altura<=0):
        print("Error: Valor de la altura y el peso invalidos.")
    elif peso<=0:
        print("Error: Valor del peso invalido.")
    elif altura<=0:
        print("Error: Valor de la altura invalido.")
    else:
        print("Tu indice de masa corporal es: %.2f" % calcularIMC(peso, altura))
        print("Tu estado es: ", calcularEstado(calcularIMC(peso,altura)))

main()