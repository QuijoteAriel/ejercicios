import random
import statistics
from colorama import init, Style, Fore

lista = [random.randint(1, 100) for _ in range(100)]
print("Lista:", lista)
print("Máximo:", max(lista))
print("Mínimo:", min(lista))
print("Media:", sum(lista) / len(lista))
print("Mediana:", str(len(lista) / 2))
moda = statistics.mode(lista)
print("Moda:", moda)


def imprimir(lista):
    moda = statistics.mode(lista)
    for numero in lista:
        if numero == moda:
            print(Fore.RED + str(numero), end=" " + Fore.RESET)
        else:
            print(numero, end=" ")
    print(Style.RESET_ALL)


imprimir(lista)
