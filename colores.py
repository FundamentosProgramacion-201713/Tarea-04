#encoding: UTF-8
#Autor: Luis Alfonso Alcántara López Ortega, A01374785

#Función para determinar el color resultante
def colorResultante(a, b):
    resultado = ""
    if a == 'ROJO':
        if b == 'AZUL':
            resultado = "MORADO"
        elif b == 'AMARILLO':
            resultado = "NARANJA"
        elif b == 'ROJO':
            resultado = "ROJO"
        else:
            resultado = "Error en los colores escritos."

    elif a == 'AZUL':
        if b == 'AZUL':
            resultado = "AZUL"
        elif b == 'AMARILLO':
            resultado = "VERDE"
        elif b == 'ROJO':
            resultado = "MORADO"
        else:
            resultado = "Error en los colores escritos."
    elif a == 'AMARILLO':
        if b == 'AZUL':
            resultado = "VERDE"
        elif b == 'AMARILLO':
            resultado = "AMARILLO"
        elif b == 'ROJO':
            resultado = "NARANJA"
        else:
            resultado = "Error en los colores escritos."
    else:
        resultado = "Error en los colores escritos."
    return resultado

def main():

    color1 = input("Ingresa el primer color: ")
    color1 = color1.upper()
    color2 = input("Ingresa el segundo color: ")
    color2 = color2.upper()

    colorFinal = colorResultante(color1, color2)
    print(colorFinal)

main()