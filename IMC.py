#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Mátricula: A01376152
#Descripción: Calcula el Índice de Masa Corporal (IMC)


#calcula el IMC

def calcularIMC(masa, altura):
    IMC = masa / (altura ** 2)
    return IMC


#Función principal

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
            print("Está en estado normal.")
        elif IMC >= 25:
            print("Lamentamos informale que tiene sobrepeso. Consulte a su médico.")
        elif IMC <= 18.5:
            print("Usted esta bajo de peso. Consulte a su médico.")

main()