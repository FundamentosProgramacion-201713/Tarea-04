#encode: UTF-8
#Autor: Leonardo Castillejos Vite
#Desripción: El usuario escribe uno de los colores primarios y da el color resultante de mezclarlos.

def main():
    color1 = input("Escriba el primer color primario: ")
    color2 = input("Escriba el segundo color primario: ")
    color1Min = color1.lower()
    color2Min = color2.lower()
    if validarRespuesta(color1Min, color2Min) == True:
        combinacion = mezclarColores(color1Min, color2Min)
        print("La combinación de %s y %s es: %s" % (color1, color2, combinacion))
    elif color1Min != "rojo" or color1Min != "azul" or color1Min != "amarillo":
        print("El color 1 no es un color primario")
    else:
        print("El color 2 no es un color primario")




# Valida que las respuestas dadas por el usuario para que sean una de las permitidas
def validarRespuesta(color1Min, color2Min):
    if color1Min == "rojo" or color1Min == "azul" or color1Min == "amarillo":
        if color2Min == "rojo" or color2Min == "azul" or color2Min == "amarillo":
            return True
        else:
            return False
    else:
        return False

# Da el resultado de la mezcla de los colores
def mezclarColores(color1Min, color2Min):
    if color1Min == "rojo":
        if color2Min == "rojo":
            return "Rojo"
        elif color2Min == "azul":
            return "Morado"
        elif color2Min == "amarillo":
            return "Naranja"
    elif color1Min == "azul":
        if color2Min == "azul":
            return "Azul"
        elif color2Min == "rojo":
            return "Amarillo"
        elif color2Min == "amarillo":
            return "Verde"
    elif color1Min == "amarillo":
        if color2Min == "amarillo":
            return "Amarillo"
        elif color2Min == "azul":
            return "Verde"
        elif color2Min == "rojo":
            return "Naranja"

main()