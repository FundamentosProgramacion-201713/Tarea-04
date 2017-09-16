#encoding UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: Este programa calcula el índice de masa corporal e imprime si estas bajo de peso, en peso o tienes sobrepeso.

#Esta función calcula el indice de masa corporal a apartir de la altura y la masa que recibe como parámetros
def calcularIMC(altura, masa):
    imc  = masa/(altura**2)
    return imc

#Esta función calcula en que rango de IMC se encuentra el ususario a partir del imc que recibe como parámetro
def calcularNivel(imc):
    if imc < 18.5:
        return 'Tienes bajo peso'
    elif imc >=18.5 and imc <=25:
        return 'Tienes peso normal'
    else:
        return 'Tienes sobrepeso'

#La función main pide la altura y la masa y las valida, si es valida, llama a las funciones anteriores para calcular el IMC
# e imprime el valor y el rango en el que se encuentra el IMC obtenido
def main():
    altura=float(input('Ingresa tu estatura en metros: '))
    if altura > 0:
        masa = float(input('Ingresa tu peso en kilogramos: '))
        if masa >0:
            imc = calcularIMC(altura,masa)
            nivelpeso= calcularNivel(imc)
            print('Tu IMC es de %.2f, %s' %(imc,nivelpeso))
        else:
            print('Peso inválido favor de ingresar un peso correcto')

    else:
        print('Altura inválida favor de ingresar una altura correcta')

main()