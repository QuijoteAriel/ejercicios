def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es numero  primo", n, "es divisor")
            return False
    print("Es primo")
    return True

es_primo(1000000009) #este numero es primo
