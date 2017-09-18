#encoding: UTF-8
#Autor: Ana María López Soto
#Programa que recibe el peso y estatura e imprime el IMC y lo compara

#Calula el IMC
def calcularIMC(peso,estatura):
    if peso <= 0 or estatura <= 0:
       imc = "ERROR: El peso o la altura que ingreso es inválida"
    else:
       imc = peso / (estatura ** 2)
    return imc


#Funcion que determina si el peso es bajo, normal o alto
def determinarNivel(imc):
    if imc < 18.5:
      nivel =  "Se tiene bajo peso"
    elif imc >= 18.5 and imc <= 25:
      nivel =  "Su peso normal"
    else:
      nivel = "Se tienes sobrepeso"
    return nivel

#Lee el peso y altura, procesa e imprime resultados
def main():
    peso = float(input("Introduce tu peso en kilogramos: "))
    estatura = float(input("Introduce tu altura en metros: "))
    if peso <= 0 or estatura <= 0:
       print("ERROR. Inserte valores válidos.")
    else:
         imc = calcularIMC(peso, estatura)
         nivel = determinarNivel(imc)
         print("Tu Indice de Masa Corporal es de %.2f" %(imc),".", nivel)

main()

