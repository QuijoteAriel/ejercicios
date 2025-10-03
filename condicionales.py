""" 

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


########
try:
    n1 = int(input('dime un numero entero: '))
    n2 = int(input('dime otro numero entero: '))
    print(n1 / n2)
except ValueError:
    print("¡Error! Debes introducir un número entero válido.")
except ZeroDivisionError:
    print("¡Error! No puedes dividir entre cero.")

#Ejercicio 4
#Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética (3+2 / 2*5) al cuadrado


formula = (((3+2)/(2*5))**2)
print(formula)
 

# Ejercicio 5

# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.


edad = int(input('que edad tienes :'))
ingresos = int(input('cuanto es tu ingreso mensual :'))



if edad > 16 and ingresos > 1000:
    print('debestributar')
else:
    print('no deben tributar ')



# Ejecicio 6

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


sexo = input('cual es tu sexo H o M ')
nombre= input('cual es tu nombre ')


if sexo == 'M':
    if nombre.lower() < 'm':
        print('Grupo A')
    else:
        print('Grupo B')

if sexo == 'H':
    if nombre.lower() > 'n':
        print('Grupo A')
    else:
        print('Grupo B')


""" 
#los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.




renta = int(input('cual estu renta anual ? :'))

if renta <= 10000:
    print('Tu renta de tipo Impositiva es de 5%')
elif renta >= 10001 or renta <= 20000:
    print('Tu renta de tipo Impositiva es de 15%')
elif renta >= 20001 or renta <= 35000:
    print('Tu renta de tipo Impositiva es de 20%')
elif renta >= 35001 or renta <= 60000:
    print('Tu renta de tipo Impositiva es de 30%')
elif renta >= 60001:
    print('Tu renta de tipo Impositiva es de 45%')
else:
    print('insete un numero valido ')










