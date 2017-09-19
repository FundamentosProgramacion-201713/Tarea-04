#Encoding UTF-8
#Anaid Fernanda Labat González, A01746289
#Calcular el IMC de una persona e indicar si su peso es bajo, normal o sobrepeso 
def calcularIndice(masa, estatura):
    indice = masa/(estatura**2)
    return indice

#Ingresar peso y estatura
def main():
    m=float(input("Ingresa tu peso en kilográmos: ", ))
    e=float(input("Ingresa tu estatura en metros: ", ))
#Definir si la persona tiene un peso bajo, normal o sobrepeso
    if m > 0 and e > 0:
        imc = calcularIndice(m, e)
        if imc < 18.5:
            print("Tu IMC es de:", "{0:.2f}".format(imc), "Tu peso es bajo")
        elif 18.5 <= imc <= 25:
            print("Tu IMC es de:", "{0:.2f}".format(imc), "Tu peso es normal.")
        elif imc > 25:
            print("Tu IMC es de:", "{0:.2f}".format(imc), "Tienes sobrepeso")
#Marca un error en caso de que no se ingrese un número positivo
    if m <= 0 or e <= 0:
        print("ERROR, ingrese número positivos")



main()