#encoding:UTF-8
#Autor: Ana María López Soto
#Descripción: Este programa da el color resultante de la mezcla de dos colores ingresados.

#Calcula el color resultante de los dos ingresados
def mezclarColores(color1,color2):
    if color1.upper == "ROJO" or color2.upper() == "ROJO"  and color1.upper() == "AZUL" or color2.lower() == "azul":
        colorResultante = "Morado"
    elif color1.upper() == "ROJO" or color2.upper() == "ROJO" and color2.upper() == "AMARILLO" or color1.lower() == "amarillo":
        colorResultante = "Anaranjado"
    elif color1.upper() == "AZUL" or color2.upper() == "AZUL" and color2.upper() == "AMARILLO" or color1.lower() == "amarillo":
        colorResultante = "Verde"
    elif color1 == color2:
       colorResultante = color1
    else:
        colorResultante = "x"
    return colorResultante


#Lee los colores que ingresan los usuarios e imprime resultados
def main():
    color1= input("Ingrese el primer color primario: ")
    color2 = input("Tecleé el segundo color primario: ")
    print("------------------------------------------")
    colorResultante = mezclarColores(color1, color2)
    if colorResultante == "x":
        print("ERROR. Inserte sólo colores primarios.")
    else:
        print("El color resultante de la mezcla ente", color1, "y", color2, "es:", colorResultante)

main()

