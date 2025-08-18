#frozenset({1,2,3})
#bytearray(4)
#range(1,34)
#memoryview(bytes(5))

user = {
  "name": "Pepito",
  "age": 20,
  "role": "Python developer"
}

for prop in user:
  print(user[prop])



technologies = ["py", "django", "webscraping"]
t = [1,2,3,4,5,]
for element in technologies:
  print(element)
while True:
    numero_str = input("Introduce un número mayor que 10: ")
    try:
        numero = int(numero_str)
        if numero > 10:
            print(f"Número válido: {numero}")
            break  # Salir del bucle
        else:
            print("El número no es mayor que 10. Intenta de nuevo.")
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")
