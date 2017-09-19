#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Mátricula: A01376152
#Descripción:  Imprime el color secundario resultante de la mezcla de dos números primarios.


#Hacer la mezcla de los colores

def mezclarColores(color,color2):
    if (color == "amarillo" and color2 == "rojo") or (color2 == "amarillo" and color == "rojo"):
        mezcla = "naranja"
    elif (color == "amarillo" and color2 == "azul") or (color2 == "amarillo" and color == "azul") :
        mezcla = "verde"
    elif (color == "rojo" and color2 == "azul") or (color2 == "rojo" and color == "azul"):
        mezcla = "morado"
    elif color == color2 == "amarillo" or color == color2 == "rojo" or color == color2 == "azul":
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
        print ("¡ERROR! Los colores ingresados son invalidos")
    else:
        print("La mezcla de color primario: %s y color primario: %s, dan por resultado: %s" % (color,color2,mezcla))



main()