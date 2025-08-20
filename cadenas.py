"""" 

# Ejercicio 1
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("dome tu nombre ")
numero = int(input("dime un numero "))
print((nombre + '\n') * numero )


# Ejercico 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.



n= input("dime tu nombre completo ")

print(n.upper())
print(n.lower())
print(n.title())


# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.



n= input("dime tu nombre completo ")

print(n.upper(), "tiene ", len(n), "letras  ")

# Ejercicio 4
# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.


n_telefono = input("dime  el numero de telefono  ")
print("el numero es " , n_telefono[4:-3]) #se usan slice para aislar la cadena



# Ejercicio 5
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = input("frase : ")
print(frase[::-1])




# Ejercico 6
# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.


frase = input("frase ")
vocal = input("vocal ")


print(frase.replace(vocal, vocal.upper())) # para usar replace se necesitan 2 argumentos , el que se quiere cambiar y el por el que se quiere cambiar 



# Ejercicio 7
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

email = input("dime tu email ")
print(email[:email.find('@')] + "@ceu.es")


# Ejercicio 8
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = str(input("dime el precio : "))
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

""" 

# Ejercicio 9
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.


fecha = input("dime una fecha ")

print("dias ", fecha[:2:])
print("mes ", fecha[3:5])
print("año ", fecha[6::])







