# encoding: UTF-8
# Author: Viviana Osorio Nieto

#poner valores a lo ingresado
def calcularColor (c1,c2):
    if c1 == "rojo" or "ROJO":
        color1 = r
    else:
        if c1 == "amarilo" or "AMARILO":
            color1 = am
        else:
            if c1 == "azul" or "AZUL":
                color1 = a

    if c2 == "rojo" or "ROJO":
        color2 = r
    else:
        if c2 == "amarilo" or "AMARILO":
            color2 = am
        else:
            if c2 == "azul" or "AZUL":
                color2 = a

    return color1, color2

r = "rojo"
a = "azul"
am = "amarillo"
m = "morado"
n = "naranja"
v = "verde"
# calcular la mexcla de valores
def CalcularResultado (color1, color2):
    if color1 == r and color2 == a or color1 == a and color2 == r:
        c = m
    else:
        if color1 == r and color2 == am or color1 == am and color2== r:
            c = n
        else:
            if color1 == a and color2== am or color1 ==am and color2 == a:
                c = v
            else:
                if color1 == r and color2 == r:
                    c = r
                else:
                    if color1 == a and color2 == a:
                        c = a
                    else:
                        if color1 == am and color2 == am:
                            c = am
    return c


# funcion principal, leer imprimir valores
def main ():
    c1 = (input("cual es el primer color:"))
    c2 = (input("cual es el segundo color (rojo, amarilo, azul):"))
    color1, color2 = calcularColor(c1, c2)

    c = CalcularResultado(color1,color2)

    print("el color resultante es:", c)

main()
