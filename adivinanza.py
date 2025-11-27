"""
Juego de Adivinanza de Números:
Descripción: El programa genera un número aleatorio y el usuario intenta adivinarlo. Da pistas si el número es mayor o menor.
Conceptos a Practicar: Bucles (while), generación de números aleatorios, condiciones (if/else).
"""

import random


pc = random.randint(1, 51)
while True:
    n = int(input("dime un numero "))
    #    pc = random.randint(1,51)
    print(pc)
    if n == pc:
        print("numero correcto !!!")
        break
    elif n < pc:
        print("es un numero mas grande ")

    elif n > pc:
        print("es un numero mas chico ")

    else:
        print("pon una opcion valida ")
        continue
