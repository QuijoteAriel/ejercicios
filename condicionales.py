# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = int(input("dime tu edad "))

if edad >= 18:
    print("eres mayor de edad")
else:
    print("No eres  mayor")


# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

c = "papa"


# Ejercicio 3

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""" 
n1 = int(input('dime un numero entero: '))
n2 = int(input('dime otro numero entero: '))


try:
    if n1 or n2 != 0 :
        print(n1/n2)
   
else:
except ValueError:
    print("¡Error! Debes introducir un número entero válido.")
except ZeroDivisionError:
    print("¡Error! No puedes dividir entre cero.")

"""
########
try:
    n1 = int(input('dime un numero entero: '))
    n2 = int(input('dime otro numero entero: '))
    print(n1 / n2)
except ValueError:
    print("¡Error! Debes introducir un número entero válido.")
except ZeroDivisionError:
    print("¡Error! No puedes dividir entre cero.")



