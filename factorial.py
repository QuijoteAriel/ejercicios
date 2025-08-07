# factoriales 

# factorial(n)= n* factorial (n-1)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_n = print(factorial(10))

# fibonacci con recursibidad

def fibo(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)

number = 10
print(fibo(number))
