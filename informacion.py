info = {
    "jose": {"apellido": "flores", "edad": 39, "estatura": 1.7},
    "florencia": {"apellido": "lentijo", "edad": 38, "estatura": 1.6},
}

claves = info.keys()
valores = info.values()

print(claves)
print(valores)
print(info["jose"])

print("##############")


def check_numbers_if_if_if(num):
    if num > 0:
        print("El número es positivo.")
    if num % 2 == 0:
        print("El número es par.")
    if num < 10:
        print("El número es menor que 10.")
    else:
        print("El número no es positivo, no es par o no es menor que 10.")


print("--- Usando if...if...if...else ---")
check_numbers_if_if_if(4)

print("\n")
check_numbers_if_if_if(12)
