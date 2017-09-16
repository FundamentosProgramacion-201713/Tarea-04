#encoding UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: Este programa lee	dos	colores	primarios (rojo,	azul,	amarillo) e imprime el color resultante

#Esta función mazcla los colores que recibe como parámetro y los regresa.
def mezclarcolores(color1, color2):
    if color1 == color2:
        return color1.title()
    elif (color1 == 'rojo' or color1 == 'azul') and (color2 == 'azul' or color2 == 'rojo'):
        return 'Morado'
    elif (color1 == 'rojo' or color1 == 'amarillo') and (color2 == 'amarillo' or color2 == 'rojo'):
        return 'Naranja'
    else:
        return 'Verde'

#La función main llama a la función anterior siempre y cuando los valores ingresados sean validos e imprime la mezcla de los colores
def main():
    c1 = input('Ingresa un color a combinar: ')
    color1=c1.lower()
    if (color1 == 'rojo' or color1 == 'amarillo' or color1 == 'azul'):
        c2 = input('Ingresa otro color a combinar: ')
        color2 = c2.lower()
        if (color2 == 'rojo' or color2 == 'amarillo' or color2 == 'azul'):
            resultante = mezclarcolores(color1,color2)
            print ('El color resultante de combinar %s y %s es %s' %(c1,c2,resultante))
        else:
            print('El color %s es invalido' % c2)
    else:
        print('El color %s es invalido'% c1)
main()
