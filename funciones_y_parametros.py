last_name = "flores"
name = None 
def greet(name= "no name", last_name = "no last name"):
    print("saludar", name, last_name)

greet(name, last_name)

#funciones lambda
#se debe recordar escribir los parametros de la funcion en el print o heredarlos de otro lado
add = lambda a,b: a+b
print(add(10,5))

#generar numero cuadros usando lambda

number = range(11)
square = list(map(lambda x: x**2, number))
print(square)

# numeros pares usando filter

even_number = list(filter(lambda x: x%2==0, number))
print(even_number)


