#encoding-UTF-8
#AUTOR: José Antonio Vázquez Gabián
#Este programa imprime el número romano de los 10 primeros numeros enteros
def calcularRomano(numero):
    if numero <=3:
        n=numero*"I"
    elif numero ==4:
        n=((numero-3)*"I")+"V"
    elif numero <=8:
        n="V"+((numero-5)*"I")
    elif numero ==9:
        n=((numero-8)*"I")+"X"
    elif numero ==10:
        n="X"
    return(n)
#Esta función lee un número introducido por el usuario y llama a la funcion anterior para imprimir resultado
def main():
    entero=int(input("Teclea numeros del 1 al 10:"))
    if 1<=entero<=10:
        print("El número romano es",calcularRomano(entero))
    else:
        print("error")
main()