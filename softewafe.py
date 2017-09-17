# encoding: UTF-8
# viviana osorio nieto
# calcular el descuento y regresar el total
# calcular el descuento
def calcularDescuento (a):
    if a < 0:
        d = print ("error")
    else:
        if a>= 10 and a<=19:
            b = (a*1500)
            d = (b*.2)
        else:
            if a >= 20 and a<=49:
                b = (a * 1500)
                d = (b * .3)
            else:
                if a >=50 and a<=99:
                    b = (a * 1500)
                    d = (b * .4)
                else:
                    if a>= 100:
                        b = (a * 1500)
                        d = (b * .5)
    return d
# calcula el total
def calcularTotal (a,d):
    t= (a*1500) - d
    return t
# funcion principal lee imprime datos.
def main ():
    a = int(input("cuantos paquetes compraste?:"))
    d = calcularDescuento (a)
    print("el descuento aplicado es de: ", d)
    t = calcularTotal (a,d)
    print ("el total a pagar es de: ",t)

main()