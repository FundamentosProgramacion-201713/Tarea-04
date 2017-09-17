#encoding: UTF-8
#autor: Juan Sebastian Lozano Derbez
#Conversiión a números romanos

def romanos(numero):
   if numero == 10 or numero == 9:
       print ("I" * (10 - numero),"X")

   elif numero <= 8 and numero >= 5:
       print("V", "I" * (numero - 5))

   elif numero == 4:
       print("IV")

   elif numero <= 3 and numero >= 1:
       print("I" * numero)

   elif numero <= 0 or numero >10:
       print("Numero invalido")
def main():
    numero = int(input("Escribe un numero del 1 al 10: "))
    romanos(numero)

main()

