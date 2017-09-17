# encoding: UTF-8
# viviana osorio nieto
# calcular el iMC

# calcular el imc
def calcularIMC (p,e):
    imc = p / (e ** 2)
    if e <= 0:
        imc = "error"
    else:
        if e < 0 and p < 0:
            imc = "error"

    return imc
#funcion principal
def main ():
    e = float(input("cual es tu estatura en metros?:"))
    p = float(input("cual es tu peso en kg"))
    imc= calcularIMC(p, e)
    if imc < 18.5:
        print ("bajo peso")
    else:
        if imc >=18.5 and imc <= 25:
            print ("peso normal")
        else:
            if imc> 25:
                print ("sobre peso")

main ()
