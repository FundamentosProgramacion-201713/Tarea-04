#Javier Pascal Flores
#encoding: UTF-8

#Esta funcion es la que hace el color resultante de la mezcla
def mezclar_Color(color_1, color_2):
    if color_1 == "rojo" and color_2 == "azul":
        color_resultante = 'Morado'
    elif color_1 == "azul" and color_2 == "rojo":
        color_resultante = 'Morado'
    elif color_1 == "amarillo" and color_2 == "rojo":
        color_resultante = 'Naranja'
    elif color_1 == "rojo" and color_2 == "amarillo":
        color_resultante = 'Naranja'
    elif color_1 == "azul" and color_2 == "amarillo":
        color_resultante = "Verde"
    elif color_1 == "amarillo" and color_2 == "azul":
        color_resultante = "Verde"
    else:
        color_resultante = "Ingresaste un color no válido"
    return color_resultante
#Aqui el programa lee e imprime los colores, ademas hace lowercase las entradas
def main():
    color_entrada = (input("Dame un color primario para mezclar (Amarillo, Rojo y Azul): "))
    color_1=color_entrada.lower()
    color_entrada_2 = (input("Dame un color primario para mezclar (Amarillo, Rojo y Azul): "))
    color_2=color_entrada_2.lower()
    color_resultante=mezclar_Color(color_1, color_2)
    print("El color resultante es:", color_resultante)
main()