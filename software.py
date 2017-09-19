#Encoding UTF-8
#Anaid Fernanda Labat González, A01746289
#Calcular el precio total de los paquetes comprados

def calcularPrecio(cantidad):
    total=cantidad*1500
    return total
#Calcular el descuento
def calcularDescuento(cantidad):
    total1=calcularPrecio(cantidad)
    if cantidad>=0 and cantidad <=9:
        return total1
    elif cantidad>=10 and cantidad <=19:
        total2=total1-(total1*.20)
        return total2
    elif cantidad >= 20 and cantidad <= 49:
        total2 = total1 - (total1 * .30)
        return total2
    elif cantidad >= 50 and cantidad <= 99:
        total2 = total1 - (total1 * .40)
        return total2
    elif cantidad >= 100:
        total2 = total1 - (total1 * .50)
        return total2

#imprimir resultados
def main():
    cantidad=int(input("Teclee la cantidad de paquetes comprados: "))
    if cantidad>=0:
        total1=calcularDescuento(cantidad)
        print ("0.2f El costo total de los paquetes con el descuento incluido es de: $",total1)
    else:
        print("ERROR, ingrese números positivos")
main()