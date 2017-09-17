#encoding: UTF-8
#Autor: Luis Fernando Figueroa Rendon, A01746139
#El programa recibe dos colores primarios e imprime la mezcla.

#Esta funcion mezclara dos colores primarios dando la mezcla entre si.
def mezclarColores(color1, color2):
    if (((color1 or color1) == "rojo") and ((color2 or color2) == "azul")) or (((color1 or color1) == "azul") and ((color2 or color2) == "rojo")):
        mezcla = "Morado."
    elif (((color1 or color1) == "rojo") and ((color2 or color2) == "amarillo")) or (((color1 or color1) == "amarillo") and ((color2 or color2) == "rojo")):
        mezcla = "Naranja."
    elif (((color1 or color1) == "amarillo") and ((color2 or color2) == "azul")) or (((color1 or color1) == "azul") and ((color2 or color2) == "amarillo")):
        mezcla = "Verde."
    elif (((color1 or color1) == "amarillo") and ((color2 or color2) == "amarillo")):
        mezcla = "Amarillo."
    elif (((color1 or color1) == "rojo") and ((color2 or color2) == "rojo")):
        mezcla = "Rojo."
    elif (((color1 or color1) == "azul") and ((color2 or color2) == "azul")):
        mezcla = "Azul."
    else:
        mezcla="Error: Colores invalidos."
    return mezcla

def main():
    print("")
    print("Ingresa solo colores primarios: Rojo, azul y amarillo.")
    print("")
    primercolor= input("Ingresa un color: ")
    primercolor1=primercolor.lower()
    segundocolor= input("Ingresa otro color: ")
    segundocolor2=segundocolor.lower()
    print("El color que resulta de mezclar", primercolor, "y", segundocolor,"es: ", mezclarColores(primercolor1,segundocolor2) )

main()

