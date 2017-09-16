#Encoding: UTF-8
#Autor: Luis Daniel Rivera Salinas  A01374997
#Descripcion: Dados los 2 colores, imprimir el color que se forma con esos dos

def mezclarColores(color1Minusculas,color2Minusculas):  #Hace la combinacion de colores, y si los colores no son validos regresa mensaje de error
    if color1Minusculas == "rojo" and color2Minusculas == "rojo":
        return("Rojo")
    elif color1Minusculas == "amarillo" and color2Minusculas == "amarillo":
        return("Amarillo")
    elif color1Minusculas == "azul" and color2Minusculas == "azul":
        return("Azul")
    elif (color1Minusculas == "rojo" and color2Minusculas == "azul") or (color1Minusculas == "azul" and color2Minusculas == "rojo"):
        return("Morado")
    elif (color1Minusculas == "rojo" and color2Minusculas == "amarillo") or (color1Minusculas == "amarillo" and color2Minusculas == "rojo"):
        return("Naranja")
    elif (color1Minusculas == "azul" and color2Minusculas == "amarillo") or (color1Minusculas == "amarillo" and color2Minusculas == "azul"):
        return("Verde")
    else:
        return("Colores no validos")

def main():  #Al ingresar 2 colores primarios, llama a la funcion mezclar colores, e imprime el color resultante; si los colores estan en mayusculas o minisculas, los transforma a minusculas
    color1 = input("Ingrese su color primario #1: ")
    color2 = input("Ingrese su color primario #2: ")
    color1Minusculas = color1.lower()
    color2Minusculas = color2.lower()
    print("Su color al combinar " , color1Minusculas, "y" , color2Minusculas , "será: ", mezclarColores(color1Minusculas,color2Minusculas))

main()