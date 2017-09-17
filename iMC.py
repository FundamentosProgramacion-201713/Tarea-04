#encoding: UTF-8

# Autor: DiegoArmandoPerezGonzalez, A01374794
# Descripcion: con respecto al peso y altura dado por los usuarios calcula tu imc

def iMC(pesoKg, alturaM):
    iMC = ((pesoKg)/(alturaM**2))
    if iMC < 18.5:
        return ("Bajo peso", iMC)
    elif iMC <= 25 or iMC >= 18.5:
        return ("Peso Normal", iMC)
    elif iMC >= 25:
        return ("Sobrepeso", iMC)


def main ():
    pesoKg = float(input("Ingresa tu peso en kg: "))
    alturaM = float(input("Ingresa tu altura en M: "))
    print("Tu peso es de: ", pesoKg, "kg")
    print("Tu altura es de: ", alturaM, "m")
    if pesoKg <= 0 or alturaM <= 0:
        print("Error")
    #if alturaM <= 0:
        #print("Error")
    print(iMC(pesoKg, alturaM))

main()