# encoding: UTF-8


# Autor: Iván Alejandro Dumas
# Descripción: Este programa calcula el indice de masa corporal del ususario cuando este ingresa
# su peso en kilogramos y su estatura en metros


# Esta función calcula el indice de masa corporal del usuario
def calcularIMC(masa,altura):
    imc = masa/(altura**2)
    return imc

# Esta función compara el imc y determina si la persona tiene bajo peso, peso normal o sobrepeso
def compararIMC(imc):
    n = "Peso normal"
    if imc > 25:
        n = "Sobrepeso"
    elif imc <18.5:
        n = "Bajo peso"
    return n

# Función principal del programa
def main():
    masa = float(input("Ingresa tu peso en kilogramos : "))
    altura = float(input("Ingresa tu altura en metros : "))
    print("""
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
""")
    if masa > 0 and altura > 0:
        imc = calcularIMC(masa,altura)
        compare = compararIMC(imc)
        print("Tu indice de masa corporal es %.2f, lo cual refleja un: %s" % (imc,compare))
    else:
        print ("ERROR: Los valores ingresados son invalidos")


#Llamar a la función pricipal
main()