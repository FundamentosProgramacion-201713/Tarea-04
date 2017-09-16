# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Determinación del resultado de la mezcla de dos colores.

# Determinar y guardar en la variable colorResultante el color resultante de la mezcla.
def determinarColorResultante(color1, color2):
    if (color1 == "rojo" and color2 == "azul") or (color1 == "azul" and color2 == "rojo"):
        colorResultante = "morado"
        return colorResultante
    elif (color1 == "rojo" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "rojo"):
        colorResultante = "naranja"
        return colorResultante
    elif (color1 == "azul" and color2 == "amarillo") or (color1 == "amarillo" and color2 == "azul"):
        colorResultante = "verde"
        return colorResultante
    elif (color1 == color2):
        colorResultante = color1
        return colorResultante

# Función principal.
def main():
    color1 = input("Inserta un color primario: ")
    color1 = color1.lower()
    if (color1 == "rojo") or (color1 == "azul") or (color1 == "amarillo"):
        color2 = input("Inserta otro color primario: ")
        color2 = color2.lower()
        if (color2 == "rojo") or (color2 == "azul") or (color2 == "amarillo"):
            colorResultante = determinarColorResultante(color1, color2)
            print("El color resultante de la mezcla es:", colorResultante)
    else:
        print("El color es inválido. Por favor, inténtalo de nuevo.")

# Ejecutar función principal.
main()
