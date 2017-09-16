#encode: UTF-8
#Autor: Leonardo Castillejos Vite
#Descripción: Da el precio total del software comprado

def main():
    peso = float(input("Escriba su peso en kilogramos: "))
    altura = float(input("Escriba su estatura en metros: "))
    if peso > 0 and altura > 0:
        IMC = calcularIMC(peso, altura)
        print("Su IMC es de %.2f" %(IMC))
        estado = compararIMC(IMC)
        print(estado)
    else:
        print("Cantidad invalida")

# Calcula el IMC con el peso y la altura proporcionadas
def calcularIMC(peso, altura):
    IMC = peso / altura ** 2
    return IMC

#Compara el IMC para ver si el usuario tiene su peso ideal o no lo tiene
def compararIMC(IMC):
    if IMC < 18.5:
        return "Usted está en un peso bajo"
    elif IMC >= 18.5 and IMC <= 25:
        return "Usted tiene un peso normal"
    elif IMC > 25:
        return  "Usted tiene sobrepeso"

main()