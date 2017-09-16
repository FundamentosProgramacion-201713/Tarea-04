# encoding UTF-8
# Autor: Siham El Khoury Caviedes, A01374764

# Descripción: Cálculo del índice de masa corporal.

# Calcular y guargar en la variable imc el índice de masa corporal.
def calcularIMC(peso, estatura):
    imc = peso / estatura**2
    return imc


# Calcular y guardar en la variable estado el estado del usuario dependiendo de su índice de masa corporal.
def determinarEstado(imc):
    if imc < 18.5:
        estado = "Bajo peso."
        return estado
    elif 18.5 <= imc <= 25:
        estado = "Peso Normal."
        return estado
    elif imc > 25:
        estado = "Sobrepeso."
        return estado


# Función principal:
def main():
    peso = float(input("Indique su peso en kg: "))
    if peso <= 0:
        print ("Error. Peso no válido.")
    estatura = float(input("Indique su estatura en m: "))
    if peso <= 0:
        print ("Error. Estatura no válida.")
    imc = calcularIMC (peso, estatura)
    estado = determinarEstado(imc)
    print ("Su índice de masa corporal es: %.2f" % imc)
    print ("Su estado es:", estado)

# Ejecutar la función principal.
main()
