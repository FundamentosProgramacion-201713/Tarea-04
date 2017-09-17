#encoding: UTF-8
#autor: Juan Sebastian Lozano Derbez
#IMC

def calculos(kg,m):
    IMC = kg/m**2
    if IMC <= 18.5:
        return "Bajo peso"
    elif IMC >= 18.5 and IMC <=25:
        return "Peso normal"
    elif IMC >= 25:
        return "Sobrepeso"

def main():
    kg = float(input("Masa (kg): "))
    m = float(input("Altura (m): "))

    print(calculos(kg,m))

main()
