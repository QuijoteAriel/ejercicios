# ejercicio 1

# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

#p = input("dime una palabra : ")

#for i in range(10):
#    print(p)


# ejericio 2

# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad) 

# edad = int(input("cual es tu edad: "))

# for i in range(1,edad+1):
#     print(i)


# ejercicio 3

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.


# n= int(input("dime un numero entero positivo: "))


# for i in range(1,n+1,2):
#     print(i ,end=", ")

# ejercicio 4 

# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.


# atras = int(input("dime un numero: "))

# for i in range(atras,-1, -1):
#    print(i, end=",")


# ejercico 6 

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

# triangulo = int(input("dime un numero : "))
# for i in range(triangulo+1):
#    tri = "*" * i
#    print(tri)


# ejercicio 7


# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.


# for i in range(1,11):
#     print(5 ,"x", i,"=", 5* i) 

# ejercicio 8 

# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.


# n= int(input("dime un numero entero positivo: "))

# for i in range(1, n+1, 2):
#     for j in range(i, 0, -2):
#         print(j, end=" ")
#     print("")
        


# Ejercicio 9
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


p = "" 
cont = "papa"

while p != cont:
    p = input("contraseña !! : ")
print( "contraseña correcta ")
        


