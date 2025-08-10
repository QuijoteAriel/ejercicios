""" def my_generador():
    yield 1
    yield 2
    yield 3

for value in my_generador():
    print(value)
# fibonacci 

def fibo(limit):
    a ,b = 0,1
    while a< limit:
        yield a
        a, b =b, a+b

for num in fibo(10000):
    print(num)

iiterar numeros
#limite
limit = 10

odd_iter = iter(range(1, limit,2))
for n in odd_iter:
    print(n)


""" 
print('#########')

def par(limit):
    a=0

    while a< limit :
        yield a
        a= a + 2
        
for i in par(20):
    print("es par ", i)

def impar(limit):
    b = 1
    while b< limit:
        yield b
        b = b+2

for j in impar(20):
    print("es impar", j)
