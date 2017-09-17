# encoding: UTF-8


# Autor: Iván Alejandro Dumas
# Descripción: Este programa pide dos colores primarios y determina la mezcla, o si son colores iguales o si no son validos


# Esta función se encarga de determinar la mezcla de los colores, si son iguales y si no son primarios o validos
def mezclarColores(color,color2):
    if (color == "AMARILLO" and color2 == "ROJO") or (color2 == "AMARILLO" and color == "ROJO"):
        mezcla = "NARANJA"
    elif (color == "AMARILLO" and color2 == "AZUL") or (color2 == "AMARILLO" and color == "AZUL") :
        mezcla = "VERDE"
    elif (color == "ROJO" and color2 == "AZUL") or (color2 == "ROJO" and color == "AZUL"):
        mezcla = "MORADO"
    elif color == color2 == "AMARILLO" or color == color2 == "ROJO" or color == color2 == "AZUL":
        mezcla = "iguales"
    else:
        mezcla = "invalido"
    return mezcla

# Función principal
def main():
    color = input("Escribe un color primario : ")
    color2 = input("Esribe otro color primario: ")
    color = color.upper()
    color2 = color2.upper()
    mezcla = mezclarColores(color,color2)
    print ("""
––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
""")
    if mezcla == "iguales":
        print ("Los colores son iguales")
    elif mezcla == "invalido":
        print ("ERROR: Los colores ingresados son invalidos")
    else:
        print("La mezcla de color primario: %s y color primario: %s, dan por resultado: %s" % (color,color2,mezcla))


# Llamar a la función principal
main()