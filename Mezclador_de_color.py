#Pedro Cortés Soberanes A01374919
#Función: imprimir el color resultante de dos colores primarios


#Calcular mezcla de color
def calcularColorResultante(color1,color2):
    if color1=="rojo" and color2=="azul" or color1=="azul" and color2=="rojo":
        x = "Morado"
    else:
        if color1=="rojo" and color2=="amarillo" or color1=="amarillo" and color2=="rojo":
            x = "Naranja"
        else:
            if color1=="azul" and color2=="amarillo" or color1=="amarillo" and color2=="azul":
                x = "Verde"
            else:
                if color1!="rojo" or color1!="azul" or color1!="amarillo" and color2!="rojo" or color2!="azul" or color2!="amarillo":
                    x = "ERROR, ¡ESCRIBE UN COLOR PRIMARIO!"
    return x


def main():
    color1 = (input("Teclea un color primario: "))
    color2 = (input("Teclea un color primario: "))
    c1 = color1.lower()
    c2 = color2.lower()
    colorR = calcularColorResultante(c1,c2)
    print("""
    - EL color resultante es: """, colorR)


main()