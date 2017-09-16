#encoding: UTF-8
#Autor: Javier Martínez Hernández A01375496
#Descripción: Se hará un programa donde se combinaran los colores

def conocerCombinación(color1, color2): #Compara los colores para sacar su combinación
    if (color1=="ROJO" or color2=="ROJO") and (color1=="AZUL" or color2=="AZUL") and  (color1!=color2):
        return "MORADO"
    elif (color1=="ROJO" or color2=="ROJO") and (color1=="AMARILLO" or color2=="AMARILLO") and (color1!=color2):
        return "NARANJA"
    elif (color1 == "AZUL" or color2 == "AZUL") and (color1 == "AMARILLO" or color2 == "AMARILLO") and (color1 != color2):
        return "VERDE"
    elif color1==color2:
        return "MISMO COLOR"
    else:
        return"Introduzca color primario valido"

def main():
    color1=input("Ingresa un color primario: ")
    color2=input("Ingresa otro color primario: ")
    color1=color1.upper()
    color2=color2.upper()
    combinacion=conocerCombinación(color1,color2)
    print("Tu combinación es ", combinacion)
main()