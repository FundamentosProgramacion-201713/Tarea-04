#Autor: Mónica Monserrat Palacios Rodríguez
#UTF-8
#Calcular el índice de masa corporal.

def calcularIndice(masa, estatura): #Se calcula el IMC
    indice = masa/(estatura**2)
    return indice

 #La función main pide los valores para peso y estatura
def main():
    m=float(input("Ingresa tu peso en kilográmos: ", ))
    e=float(input("Ingresa tu estatura en metros: ", ))

    if m > 0 and e > 0:
        imc = calcularIndice(m, e)#Se llama a la función para calular el IMC

        if imc < 18.5: #Se asigna el valor dependiendo del IMC calulado
            print("Tu IMC es de:", "{0:.2f}".format(imc), "Tu peso es bajo")
        elif 18.5 <= imc <= 25:
            print("Tu IMC es de:", "{0:.2f}".format(imc), "Tu peso es normal.")
        elif imc > 25:
            print("Tu IMC es de:", "{0:.2f}".format(imc), "Tienes sobrepeso")


    if m <= 0 or e <= 0:  # Se crean restricciones para los valores
        print("ERROR, por favor teclee números positivos")

main()#Se llama a la función main