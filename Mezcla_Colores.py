#Autor: Maria Fernanda Torres Velazquez A01746537
#El programa lee 2 colores primarios e imprime el color resultante

#La funcion recibe 2 colores, los compara y regresa el color resultante de su mezcla
def mezclarColores(c1,c2):
    if (c1=="rojo" and c2=="azul") or (c1=="azul" and c2=="rojo"):
        m=("MORADO")

    elif (c1=="azul" and c2=="amarillo") or (c1=="amarillo" and c2=="azul"):
        m=("VERDE")

    elif (c1=="amarillo" and c2=="rojo") or (c1=="rojo" and c2=="amarillo"):
        m= ("NARANJA")

    elif (c1==c2):
        m= ("EL COLOR SIGUE SIENDO EL MISMO")

    else:
        m="ERROR, LOS COLORES NO SON PRIMARIOS"

    return m
#Funcion principal
def main():
    print ("BIENVENIDO AL MEZCLADOR DE COLORES PRIMARIOS")
    c1=(str(input("Inroduce el color 1:")))
    c2=(str(input("Inroduce el color 2:")))
    c1=c1.lower()
    c2=c2.lower()

    mezcla= mezclarColores(c1,c2)
    print ("-------------------------------")
    print ("EL COLOR RESULTANTE ES: ",mezcla)

main()
