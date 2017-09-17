#Encoding: UTF-8
#Autor: Angel Roberto Pesado Bartolo A01374942
#Descripcion: Calcula el indice de masa  corporal de una persoa e indica si está bajo de peso, normal o tiene sobrepeso.

def calcularIMC(peso,altura):   #Definimos la función que calculará el IMC y clasificará a la peprsona si tiene peso bajo, normal o sobre peso
    imc = ((peso)/(altura**2))   #Obtenemos el IMC del usuario a partir de los datos dados por el usuario.
    if imc < 18.5:   #Si el IMC es menor a 18.5 regresa que el usuario tiene bajo peso
        return ("Bajo de peso, su IMC es: ", (imc))
    elif imc >=18.5 and imc <= 25:  #Si el IMC es mayor o igual a 18.5 y menor o igual a 25 regresa que la persona esta en su peso normal
        return ("Peso optimo, su IMC es: ", imc)
    else:
        return ("Sobrepeso, su IMC es: ", imc)   #Si el IMC es mayor a 25 regresa que el usuario tiene sobrepeso.

def main():
    peso = float(input("Ingresa tu peso en kg: "))   #Pedimos su peso al usuario
    altura = float(input("Ingresa altura en m: ")) #Pedimos su altura al usuario
    if peso <= 0: #si el peso es menos a 0 no es valido el dato
        print("Error, ingrese numeros validos para calcular tu IMC")
    if altura <= 0: #si la aultura es 0 no es valido el dato
        print("Error, ingrese numeros validos para calcular tu IMC")
    print("Su altura es: ",peso, "Kg") #Imprimir peso en kg
    print("Su peso es: ",altura, "m") #Imprimir altura en m
    print(calcularIMC(peso,altura)) #Imprimir el menssaje dentro de la función calcularIMC dependiendo a los datos dados por el usuario

main()  #Llamamos a la funcion main para que realice lo que  tiene dentro de ella