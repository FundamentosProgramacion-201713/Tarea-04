#Encoding: UTF-8
#Autor: Rodrigo Rivera Salinas
#Descripcion: Calcula el indice de masa corporal de una persona e imprime la altura,el  peso y el indice de masa corporal

def imc(peso,altura):
    imc = ((peso)/(altura**2))   #A partir de los datos dados dividir peso entre (altura al cuadrado) y nos dara el imc
    if imc < 18.5:   #si el imc es menor a 18.5 nos dira que estamos bajos de peso
        return ("Bajo de peso, su imc es: ", imc)
    elif imc <= 25 or imc >= 18.5: #si el imc es mayor a 18.5 y menor a 25 nos dira que estamos en peso normal
        return ("Peso normal, su imc es: ", imc)
    else:
        return ("Sobrepeso, su imc es: ", imc)   #si es mayor a 25 tiene sobrepeso

def main():
    peso = float(input("Dar peso en kg: "))   #pedir peso en kg
    altura = float(input("Dar altura en m: ")) #pedir altura en m
    if peso <= 0: #si el peso es 0 va a ser invalido ya que ninguna persona pesa 0
        print("Error, ingrese numeros validos")
    if altura <= 0: #si la aultura es 0 va a ser invalido ya que ninguna persona mide 0
        print("Error, ingrese datos validos")
    print("La altura es: ",peso, "Kg") #imprimir la altura en m
    print("El peso es : ",altura, "m") #imprimir peso en kg
    print(imc(peso,altura)) #imprimir el imc

main()