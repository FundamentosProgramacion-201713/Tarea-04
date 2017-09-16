#Autor: Jose Heinz Moller
#Descripción: te dice el color que sale al mezclar dos

#define el color que se hace por la combinacion

def definirElColor(colorNumero1,colorNumero2):
 if colorNumero1=="azul" and colorNumero2=="rojo" or colorNumero1=="rojo" and colorNumero2=="azul":
     return ("morado")

 elif colorNumero1=="azul" and colorNumero2=="amarillo" or colorNumero1=="amarillo" and colorNumero2=="azul":
     return ("verde")

 elif colorNumero1=="amarillo" and colorNumero2=="rojo" or colorNumero1=="rojo" and colorNumero2=="amarillo":
     return ("naranja")

def main():
 colorNumero1=str(input("Escribe color 1:"))
 colorNumero2=str(input("Escribe color 2:"))
 colorFinal = definirElColor(colorNumero1, colorNumero2)

 if colorNumero1=="rojo" and colorNumero2=="amarillo" or colorNumero1=="amarillo" and colorNumero2=="rojo":
     print("Mezclando", colorNumero1, "con", colorNumero2, "tienes:", colorFinal)
 elif colorNumero1=="azul" and colorNumero2=="rojo" or colorNumero1=="rojo" and colorNumero2=="azul":
     print("Mezclando",colorNumero1, "con", colorNumero2, "tienes:", colorFinal)
 elif colorNumero1=="azul" and colorNumero2=="amarillo" or colorNumero1=="amarillo" and colorNumero2=="azul":
     print("Mezclando", colorNumero1, "con", colorNumero2, "tienes:", colorFinal)
 else:
     print("Usa colores primarios")

main()