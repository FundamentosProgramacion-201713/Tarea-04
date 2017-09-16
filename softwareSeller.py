#encoding: utf-8
#coded by: Jordan González Bustamante
#Este programa calcula el precio con descuento aplicado de acuerdo a la
#tabla de precios.

#Esta función verifica si se tecleo número negativo
def verifyNumber(packages):
    return packages <= 0

#Aquí calculamos el precio según la tabla de descuentos
def calculatePrice(packages):
    if packages > 0:
        if packages <10:
            price = float(packages * 1500)
        elif packages <= 19:
            price = float(packages * 1500 * 0.8)
        elif packages <= 49:
            price = float(packages * 1500 * 0.7)
        elif packages <= 99:
            price = float(packages * 1500 * 0.6)
        elif packages >=100:
            price = float(packages * 1500 * 0.5)
    return price

#Función principal que pide los datos, y llama a las anteriores.
def main():
    packages = int(input("Teclee el número de paquetes comprados : "))
    if verifyNumber(packages) == False:
        price = calculatePrice(packages)
        print("El pago a realizar es de $ %.2f" % price)
    else:
        print("No se ha podido procesar la orden debido a que ingreso datos invalidos")
main()