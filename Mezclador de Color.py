# Autor: Saul Rodrigo Toral Luna
# Matrícula: A01745007

# El programa lee dos colores primarios (rojo, azul y amarillo)
# Imprimir el color resultante de la mezcla de los que escogió el usuario


# La función calcula la mezcla de los colores
def calcularMezcla(color, color_2):
    if (((color.lower() or color.upper()) == "rojo") and ((color_2.lower() or color_2.upper()) == "azul")) or (((color.lower() or color.upper()) == "azul") and ((color_2.lower() or color_2.upper()) == "rojo")):
        mezcla = "morado"
    elif (((color.lower() or color.upper()) == "rojo") and ((color_2.lower() or color_2.upper()) == "amarillo")) or (((color.lower() or color.upper()) == "amarillo") and ((color_2.lower() or color_2.upper()) == "rojo")):
        mezcla = "naranja"
    elif (((color.lower() or color.upper()) == "azul") and ((color_2.lower() or color_2.upper()) == "amarillo")) or (((color.lower() or color.upper()) == "amarillo") and ((color_2.lower() or color_2.upper()) == "azul")):
        mezcla = "verde"
    elif (((color.lower() or color.upper()) == "rojo") and ((color_2.lower() or color_2.upper()) == "rojo")):
        mezcla = "rojo"
    elif (((color.lower() or color.upper()) == "azul") and ((color_2.lower() or color_2.upper()) == "azul")):
        mezcla = "azul"
    elif (((color.lower() or color.upper()) == "amarillo") and ((color_2.lower() or color_2.upper()) == "amarillo")):
        mezcla = "amarillo"
    else:
        mezcla = "Error de mezcla: Datos ingresados invalidos"
    return mezcla

# Función principal que ingresa e imprime datos
def main():
    print("")
    print("Escoge entre los colores rojo, azul y amarillo para mezclar")
    print("")
    primer_Color = input("Ingresa el primer color: ")
    segundo_Color = input("Ingresa el segundo color: ")
# Evaluar parametros, si no cumplen mandar un mensaje de error
    if ((primer_Color == "rojo" or "azul" or "amarillo") and (segundo_Color == "rojo" or "azul" or "amarillo")):
        print("La mezcla de ", primer_Color, "y", segundo_Color, "da:", calcularMezcla(primer_Color, segundo_Color))
    else:
        print("Error de mezcla: Datos ingresados invalidos")
main()

