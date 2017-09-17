#encoding: UTF-8

#Autor: Alberto López Reyes
#Descripción: Este programa imprime el color resultante de la mezcla de otros dos colores otorgados.

#Esta función regresa el color resultante de acuerdo a otros dos colores entregados.
def MezclarColores(strColor1, strColor2):
    if strColor1.upper() == "ROJO" and strColor2.lower() == "azul" or strColor1.upper() == "AZUL" and strColor2.lower() == "rojo":
        strColorResultante = "morado"

    elif strColor1.upper() == "ROJO" and strColor2.lower() == "amarillo" or strColor1.upper() == "AMARILLO" and strColor2.lower() == "rojo":
        strColorResultante = "naranja"

    elif strColor1.upper() == "AZUL" and strColor2.lower() == "amarillo" or strColor1.upper() == "AMARILLO" and strColor2.lower() == "azul":
        strColorResultante = "verde"

    elif strColor1.lower() == strColor2.lower():
        strColorResultante = str(strColor1.lower())

    else:
        print("""===========================""")
        print("""ERROR: LOS COLORES 'ROJO', 'AZUL' Y 'AMARILLO' SON SOLAMENTE ACEPTADOS.
EL PROGRAMA TERMINARÁ.""")
        exit()

    return strColorResultante

#Esta función recibe dos colores para otorgárselos a la función "Mezclar colores" que regresa un color resultante.
#Esta última se imprime.
def main():
    print("""""")
    print("""===========================""")
    print("Color 1")
    strColor1 = input("Teclea el color: ")
    print("""===========================""")
    print("Color 2")
    strColor2 = input("Teclea el color: ")

    strColorResultante = MezclarColores(strColor1, strColor2)

    print("""===========================""")
    print("El color resultante es "+strColorResultante+".")

main()