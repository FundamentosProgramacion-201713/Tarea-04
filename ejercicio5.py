# Autor: LuisMiguel Baqueiro
# Matricula: 1745997
#calcula el indice de masa corporal
def calcularIMC(masa, estatura):
    total = masa / (estatura ** 2)
    return total
def main():
    masa = int(input("Escribe tu peso:"))
    estatura = float(input("Escribe tu estatura: "))
    if estatura > 0 and masa > 0:
        imc = calcularIMC(masa, estatura)
        if imc <= 18.5 and imc > 0:
            print("Bajo peso")
            print(imc)
        elif imc >= 18.5 and imc <= 25:
            print("Peso normal")
            print(imc)
        else:
            print("Sobrepeso")
            print(imc)
    else:
        print("Error")
main()