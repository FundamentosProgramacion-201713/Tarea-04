#Javier Pascal Flores
#encoding: UTF-8
def mezclar_Color(color_1, color_2): #Aqui es donde definimos la mezcla
    if (color_1 == "Rojo" or "rojo") and (color_2 == "azul" or "Azul"):
        color_resultante = 'Morado'
    elif color_1 == "azul" or "Azul" and color_2 == "Rojo" or "rojo": #Invertimos por si el orden esta al reves
        color_resultante = "Morado"
    elif color_1 == "Rojo" or "rojo" and color_2 == "amarillo" or "Amarillo":
        color_resultante = "Naranja"
    elif color_1 == "amarillo" or "Amarillo" and color_2 == "Rojo" or "rojo": #Invertimos por si el orden esta al reves
        color_resultante = "Naranja"
    elif color_1 == "Azul" or "azul" and color_2 == "amarillo" or "Amarillo":
        color_resultante = "Verde"
    elif color_1 == "amarillo" or "Amarillo" and color_2 == "Azul" or "azul" : #Invertimos por si el orden esta al reves
        color_resultante = "Verde"
    else:
        color_resultante = "Ingresaste un color no válido"
    return color_resultante


def main(): #Aqui el programa lee e imprime los colores
    color_1 = str(input("Dame un color primario para mezclar (Amarillo, Rojo y Azul): "))
    color_2 = str(input("Dame un color primario para mezclar (Amarillo, Rojo y Azul): "))
    color_resultante=mezclar_Color(color_1, color_2)
    print("El color resultante es:", color_resultante)
main()