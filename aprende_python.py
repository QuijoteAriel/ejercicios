""" 
# Ejercicio 1
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("Hola mundo ")


# Ejercicio 2
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

saludo = "Hola mundo"
print(saludo)

# Ejercicio 3
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

nombre = input("Cual es tu nombre:  ")
print("¡Hola  ", nombre)

# Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética ( (3+2)/ (2*5))²

formula = ( ((3+2)/ (2*5))**2)
print(formula)

# Ejercicio 5
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


horas = int(input("cual es el numero de horas trasbajadas? : "))
costo_hora = int(input("Cuanto cuestas cada hora de tabajo? : "))

dia_trabajado = horas * costo_hora

print("tu dia la boras cuenta : ", dia_trabajado)


# Ejercico 6
# Escribir un programa que lea un entero positivo, n , introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n . La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:


n= int(input("dime un numero "))
suma = ( n *( n+ 1 ) )/ 2
print("la suma  es  ", str(n) , "es ", str(suma))


# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.


peso = int(input("cuanto pesas en  kg "))
altura = float(input("cuento mides en metros ? "))

imc = peso / ( altura * altura)

print("tu IMC es : ", imc )


# Ejercico 8
#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.

n= int(input("dime un numero entero "))
m= int(input("dime otro numero entero "))

c = n/m
r = n%m

print(f"la division entre {n} y {m} es {c} y el resto es {r}")


# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = int(input("cuantos quieres invertir? "))
tasa_anual = int(input("a que tasa ? "))
ages = int(input("cuantos años ? "))

interes = tasa_anual / 100 +1

tin = round( inversion * interes ** ages,2)

print(f"el capital obtenido de {inversion}, a {ages} años  es de {tin}")


# Ejercicio 10
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.



PAYASO = 112
MUNECA = 75

venta_payasos = int(input("Cuantos payasos se vendieron ?"))
venta_munecas = int(input("cuantas muñecas se vendieron ? "))

total_payasos = PAYASO * venta_payasos
total_munecas = MUNECA * venta_munecas 

print(f"El numero de payasos vendidos fue de {venta_payasos} y  el de muñecas vendidas fue de {venta_munecas} y el total de peso en gramos es de " , total_payasos + total_munecas )


# Ejercicio 11
#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.


ahorros = int(input("monto de deposito:  "))

interes = 0.04

balance = ahorros * ( 1 + interes ) 
print("intereses al primer año son: ", str(round(balance,2)))

balance2 = balance * (1 + interes) 
print("intereses al segundo año son: ", str(round(balance2,2)))

balance3 = balance2 * (1 + interes)
print("intereses al tercer  año son: ", str(round(balance3,2)))


"""
# Ejercicio 12
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.


precio = 3.49
descuento = (precio * 0.60) 
precio_descuento = precio - descuento 
barras_ayer = 5
print(f"barras de pan de ayer {barras_ayer}")
print("barras de pan del dia  ", precio)
print("barras de pan de ayer ", round(precio_descuento,2))
print("descuento de por barra de pan viejo de 60% es ", barras_ayer + round(descuento,2))



