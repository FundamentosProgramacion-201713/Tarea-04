#AUTOR: GABRIELA MARIEL VARGAS FRANCO A01745775
#endoding: UTF-8
#Leer un número entre 1 y 10 e imprima el número en Romano correspondiente
#Calcula y guarda en la varibale CalcularRomano
c="IV"
cin="V"
nu="IX"
d="X"
def calcularRomano(numero):
#Comparación de numeros
    if numero>=1 and numero<=3:
        calcularRomano=(numero*"I")
    elif numero==4:
        calcularRomano=c
    elif numero==5:
        calcularRomano=cin
    elif numero>=6 and numero<=8:
        calcularRomano=(cin)+((numero-5)*"I")
    elif numero==9:
        calcularRomano=nu
    elif numero==10:
        calcularRomano=d
    else:
        calcularRomano="Error"
#Regresa calcularRomano
    return calcularRomano


def main():
    numero=int(input("Leer numero decimal: "))
    cR=calcularRomano(numero)
#Imprime el numero romano correspondiente
    print("Numero en romano:", cR)

main()




