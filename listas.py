colores = [ 'amarillo', 'verde ', 'azul' ]

colores.pop(1) 
#pop() por defecto elimina el ultimo item de l lista a meno que se le especifique con el numero de indice 
print(colores)

numero = [ 2, 3, 2, 5, 2, 1, 2, 1, 3 ,4 ]
palabra = ['hola', 'chao', 'perdon', 'hola']
print(palabra.count('hola'))
print(numero.count(2))
# count() cuenta la repeticion de un item de una lista 

lista1 = ['1', '2', '3']
lista2 = ['4', '5', '6']
lista1.extend(lista2)
print(lista1)
# extend(), extiende lap rimera lista con la segunda lista1.extend(lista2)


n= [2,3,4,5,6,7,7,]
#n.reverse()
print(n.reverse())

numeros = [4, 5, 2, 67, 4, 2, 7, 9, 55]
numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

pintas = ['♥️', '♦️', '♣️', '♠️']


valor_decimal = 8.99
valor = int(valor_decimal)
print(valor)
