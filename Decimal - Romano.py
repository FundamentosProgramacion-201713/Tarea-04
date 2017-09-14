#encoding:UTF-8

#Autor: Carlos Pano Hernández
#Descripción: Convertir números decimales a romanos (sólo y sólo si 1<=d<=10)

#Funcion de convertir
def convertirRomano(n):

    #Para 1, 2 y 3:
    if n==1 or n==2 or n==3:
        return("I" * n)

    #Para 4:
    elif n==4:
        return("IV")

    #Para 5:
    elif n==5:
        return("V")

    #Para 6, 7 y 8:
    elif n==6 or n==7 or n==8:
        return("V" + ("I" * (n-5)))

    #Para 9:
    elif n== 9:
        return("IX")

    #Para 10:
    elif n==10:
        return("X")

#Funcion main:
def main():

    d= int(input("Escribir el número que desea convertir a romano: "))
    print("-------------------------------------")

    if d >= 1 and d <= 10:
        r=convertirRomano(d)

        print("Tu número %d en Romano es:" %(d),r)

    else:
        print("ERROR: PRUEBA NÚMEROS ENTRE 1 Y  10")

#Llamada a main
main()