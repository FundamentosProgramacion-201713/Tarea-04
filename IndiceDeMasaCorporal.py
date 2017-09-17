#encoding: UTF-8
#Autor: Ángel Guillermo Ortiz González
#Matrícula: A01745998
#Descripción: Lee altura y masa de una persona, calcula el Índice de Masa Corporal (IMC) e indica el estado del IMC.

#calcula el IMC
def calcularIMC(masa, altura):
    IMC = masa / (altura ** 2)
    return IMC

def main():
    masa = float(input("Inserte su masa en kilogramos: "))
    altura = float(input("Inserte su altura en metros: "))
    print("------------------------------------------")
    if masa <= 0 or altura <= 0:
        print("ERROR. Inserte valores válidos.")
    else:
        IMC = calcularIMC(masa, altura)
        print("Su índice de masa corporal (IMC) es: %.2f" % (IMC))
        if IMC > 18.5 and IMC < 25:
            print("Su estado es normal.")
        elif IMC >= 25:
            print("Su estado es sobrepeso. Consulte a su médico.")
        elif IMC <= 18.5:
            print("Su estado es bajo peso. Consulte a su médico.")

main()