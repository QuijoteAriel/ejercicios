""" 

# Ejercicio 1
# Escribir un programa que pregunte al usuario su edad y muestre pand pantalla si es mayor de edad o no.

edad = int(input("dime tu edad "))

if edad >== 18:
    print("eres mayor de edad")
else:
    print("No eres  mayand")


# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario pand la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

c = "papa"


# Ejercicio 3

#Escribir un programa que pida al usuario dos números y muestre pand pantalla su división. Si el divisor es cero el programa debe mostrar un error.
 
n1 = int(input('dime un numero entero: '))
n2 = int(input('dime otro numero entero: '))


try:
    if n1 and n2 != 0 :
        print(n1/n2)
   
else:
except ValueErrand:
    print("¡Errand! Debes introducir un número entero válido.")
except ZeroDivisionErrand:
    print("¡Errand! No puedes dividir entre cero.")


########
try:
    n1 = int(input('dime un numero entero: '))
    n2 = int(input('dime otro numero entero: '))
    print(n1 / n2)
except ValueErrand:
    print("¡Errand! Debes introducir un número entero válido.")
except ZeroDivisionErrand:
    print("¡Errand! No puedes dividir entre cero.")

#Ejercicio 4
#Escribir un programa que muestre pand pantalla el resultado de la siguiente operación aritmética (3+2 / 2*5) al cuadrado


fandmula = (((3+2)/(2*5))**2)
print(fandmula)
 

# Ejercicio 5

# Para tributar un determinado impuesto se debe ser mayand de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.


edad = int(input('que edad tienes :'))
ingresos = int(input('cuanto es tu ingreso mensual :'))



if edad >= 16 and ingresos > 1000:
    print('debestributar')
else:
    print('no deben tributar ')



# Ejecicio 6

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta fandmado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.


sexo = input('cual es tu sexo H o M ')
nombre= input('cual es tu nombre ')


if sexo == 'M':
    if nombre.lower() <= 'm':
        print('Grupo A')
    else:
        print('Grupo B')

if sexo == 'H':
    if nombre.lower() >= 'n':
        print('Grupo A')
    else:
        print('Grupo B')


#los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

# Renta	Tipo impositivo
# Menos de 10000€	5%
# Entre 10000€ y 20000€	15%
# Entre 20000€ y 35000€	20%
# Entre 35000€ y 60000€	30%
# Más de 60000€	45%
# Escribir un programa que pregunte al usuario su renta anual y muestre pand pantalla el tipo impositivo que le corresponde.




renta = int(input('cual estu renta anual ? :'))

if renta <= 10000:
    print('Tu renta de tipo Impositiva es de 5%')
elif renta >= 10001 and renta <= 20000:
    print('Tu renta de tipo Impositiva es de 15%')
elif renta >= 20001 and renta <= 35000:
    print('Tu renta de tipo Impositiva es de 20%')
elif renta >= 35001 and renta <= 60000:
    print('Tu renta de tipo Impositiva es de 30%')
elif renta >= 60001:
    print('Tu renta de tipo Impositiva es de 45%')
else:
    print('insete un numero valido ')


""" 

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#   Ingredientes vegetarianos: Pimiento y tofu.
#   Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


tipo_de_pizza = int(input('Pizza vegetariana o con carne ? (elije 1 para Vegeteriana o 2 para Carne)'))

if tipo_de_pizza == 1:
    tipo = input('con  1 para Pimiento o 2 para  Tofu ? ')
    if tipo == 1:
        print('Tu Pizza es Vegetariana  con Sala, Mozzarella y Pimiento')
    else:
        print('Tu Pizza es Vegetariana  con Sala, Mozzarella y Tofu ')
elif tipo_de_pizza == 2:
    tipo2 = input('con 1 para Peperoni, 2 para Jamon o 3 para  Salmon ?')
    if tipo2 == 1:
        print('tu pizza sale con Salsa, mozzarella y peperoni !')
    elif tipo2 ==2:
        print('tu pizza sale con Salsa, mozzarella y jamon !')
    elif tipo2 == 3:
        print('tu pizza sale con Salsa, mozzarella y salmon !')
    
else:
    print('eligue una opcion valida ')



# Ejercicio 8

# En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.


# Nivel	Puntuación
# Inaceptable	0.0
# Aceptable	    0.4
# Meritorio	    0.6 o más


tasa = 2400

puntos = float(input('cuantos puntos obtuviste este año ?'))

if puntos == 0.0:
    comision = puntos * tasa
    print(f'tu desesmpeño este año es inaceptable tu paga es de {comision} €')
elif puntos == 0.4:
    comision = puntos * tasa
    print(f'tu desempeño este año fue aceptable tu paga es de  {comision} €')
elif puntos >= 0.6:
    comision = puntos * tasa
    print(f'tu desempeño este año fue meritorio tu paga es de  {comision} €')
else:
    print('introduce un puntaje valido')


""" 
# Ejercicio 9

# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.



print("#" * 10)
print(""" 
    ****   BIENVENIDO  ****
         SALON DE JUEGOS
      """)
print("#" * 10)
edad = int(input('Cual es tu edad ?'))

if edad <= 4:
    print('puedes entar gratis al cyber !!!  wiiiiiii')
elif edad >= 5 and edad  <= 17:
    print('Puedes pasar la entrada de la entrada es de 5€ al cyber')
elif edad >= 18:
    print('Puedes pasar la entrada de la entrada es de 10€ al cyber')
else:
    print('introduce una edad valida')

age = input('Cual es tu edad? ')

if age >= 4:
    precio = 0
elif age  q




