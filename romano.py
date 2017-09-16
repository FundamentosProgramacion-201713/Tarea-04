#encoding UTF-8
#Autor: Angel Ramírez Martínez
#Descripción: Este programa lee un número decimal del 1-10 e imprime el número romano correspondiente


#Esta función calcula el número romano a partir del número decimal que llega como parámetro.
def calcularomano(num):
    if num <=3:
        return (num*'I')
    elif num ==4:
        return 'IV'
    elif num <=8:
        return ('V%s' %((num%5)*'I'))
    elif num ==9:
        return 'IX'
    return 'X'

#La función main lee un número y lo valida, si es valido, llama a la función anterior para calcular su número romano correspondiente.
def main():
    num = int(input('Ingresa el número que deseas en romano: '))
    if num >=1 and num <=10:
        rom = calcularomano(num)
    else:
        print('Su número es invalido favor de ingresar un número correcto')
    print('El número romano correspondiente a %d es %s'%(num,rom))
main()