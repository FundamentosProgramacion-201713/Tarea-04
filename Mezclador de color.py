#encoding:UTF-8

#Autor: Carlos Pano Hernández
#Descripción: Este programa te dice el color resultante de la mezcla de dos colores primarios

def seleccionarColor(c1,c2):
    if c1=="rojo" and c2=="azul" or c1=="azul" and c2=="rojo":
        return ("Morado")
    elif c1=="rojo" and c2=="amarillo" or c1=="amarillo" and c2=="rojo":
        return ("Naranja")
    elif c1=="azul" and c2=="amarillo" or c1=="amarillo" and c2=="azul":
        return ("Verde")

#Funcion main:
def main():
    print("")
    c1=str(input("Introduce tu primer color:"))
    c1 = c1.lower()

    c2=str(input("Introduce tu segundo color:"))
    c2=c2.lower()
    print("-----------------------------------")
    cR = seleccionarColor(c1, c2)

    if c1=="rojo" and c2=="azul" or c1=="azul" and c2=="rojo":
        print("Combinando",c1, "y", c2, "obtienes:", cR)
    elif c1=="rojo" and c2=="amarillo" or c1=="amarillo" and c2=="rojo":
        print("Combinando", c1, "y", c2, "obtienes:", cR)
    elif c1=="azul" and c2=="amarillo" or c1=="amarillo" and c2=="azul":
        print("Combinando", c1, "y", c2, "obtienes:", cR)
    else:
        print("ERROR: Prueba con colores primarios.")

#Llamada a main
main()
