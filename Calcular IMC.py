#Encoding: UTF-8
#Autor: Luis Daniel Rivera Salinas  A01374997
#Descripcion: Calcula el imc de una persona e imprime los datos (altura, peso) y el imc

def imc(peso,altura): #calcula el imc y lo cataloga en bajo, normal o con sobrepeso
    imc = ((peso)/(altura**2))
    if imc < 18.5:
        return ("Su peso es bajo, su imc es de: ", imc)
    elif imc <= 25 or imc >= 18.5:
        return ("Su peso es normal, su imc es de: ", imc)
    else:
        return ("Usted tiene sobrepeso, su imc es de: ", imc)

def main(): #toma la altura y el peso, y dependiendo de los valores, imrpime error o no, e imprime el imc y si es bajo, normal o sobrepeso
    peso = float(input("Ingresa su peso en kg: "))
    altura = float(input("Ingresa su altura en m: "))
    if peso <= 0:
        print("Error, datos no validos")
    if altura <= 0:
        print("Error, datos para altura no validos")
    print("Su altura es de: ",altura )
    print("Su peso es de peso: ",peso)
    print(imc(peso,altura))

main()