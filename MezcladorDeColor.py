#encoding: UTF-8
#Autor: Ángel Guillermo Ortiz González
#Matrícula: A01745998
#Descripción: Lee dos colores primarios e imprime el color secundario resultante de la mezcla de éstos.

#mezcla dos colores primarios y regresa el color secundario que se crea
def mezclarColores(p1,p2):
    if p1 == "rojo" and p2 == "azul":
        mezcla = "morado"
    elif p1 == "rojo" and p2 == "amarillo":
        mezcla = "anaranjado"
    elif p1 == "azul" and p2 == "rojo":
        mezcla = "morado"
    elif p1 == "azul" and p2 == "amarillo":
        mezcla = "verde"
    elif p1 == "amarillo" and p2 == "rojo":
        mezcla = "anaranjado"
    elif p1 == "amarillo" and p2 == "azul":
        mezcla = "verde"
    elif p1 == p2:
        mezcla = p1
    else:
        mezcla = "not"
    return mezcla

def main():
    a = str(input("Tecleé el primer color primario: "))
    b = str(input("Tecleé el segundo color primario: "))
    primario1 = a.lower()
    primario2 = b.lower()
    print("------------------------------------------")
    mezcla = mezclarColores(primario1, primario2)
    if mezcla == "not":
        print("ERROR. Inserte sólo colores primarios.")
    else:
        print("El color que se crea es el", mezcla)

main()
