#encoding: UTF-8
#Autor: Javier Martínez Hernández A01375496
#Descripción: Se imprimiran los numeros romanos del 1 al 10 dependiendo de lo que incerte el usuario

def numeroRomanoUno(numero):
    if numero <= 3: #si el numero es mmenor o igual a 3 regresar numero romano
        return "I"*numero

def numeroRomanoDos(numero):
    if numero ==4: #si el numero es igual a 4 regresar numero romano
        return "IV"
    else:  #si no regresar romano
        return "V"

def main():
    print("Los numeros posibles son del 1 al 10 ")
    numero=int(input("Dar un numero ")) #dar numero
    if numero>=1 and numero<=10: #si el numero es de mayor igual a 1 y menor igual a 10 seguir adelante si no no correr el programa
        if numero<4: # si el numero es menor que 4 imprimir el numero romano de 1,2,3
            Romano=numeroRomanoUno(numero)
            print("El numero romano es ",Romano)
        elif numero<9:   # si el numero romano es menor a 9
            Romano=numeroRomanoDos(numero) # guardar el numero romano de 5
            numero=numero-5 # restar el numero menos 5 para obtener los primero 3 numeros en romanos
            numero=numeroRomanoUno(numero)  # obtener el numero romano de 1 a 3
            print("El numero romano es:  ",Romano,numero) #imprimir el numero romano compuesto
        elif numero==9:  #si el numero es igual a 9 sacar su romano
            print("El numero romano es IX" )
        else: # sacar el romano de 10
            print("El numero romano es X")
    else:
        print("Error, ingrese un numero valido ")
main()