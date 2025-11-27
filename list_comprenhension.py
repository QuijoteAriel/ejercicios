"""

# conseguir numeros cuadrados
squares = [x**2 for x in range(1, 11)]
print(squares)


# conseguir numeros cubicos
cube = [x**3 for x in range(1, 20)]
print(cube)


# imprimir nuemros impates
impar = [x for x in range(1, 20) if x % 2 != 0]
print(impar)


# numero pares
par = [x for x in range(1, 20) if x % 2 == 0]
print(par)

# Tranponer

"""

""" 
Hace que el codigo se se lea de izquierda a derecha y de arriba a abajo , lo imprime de arriba a abajo y de izquierad a derecha 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

transponer = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transponer)

# saca el doble de los valores dados
doble = [1, 2, 3, 4, 5]

d = [x * 2 for x in doble]
print(d)

palabras = ["sol", "mar", "montaña", "rio", "estrella"]
p = [x for x in palabras if len(x) > 3 and x.upper()]
print(p)


key = ["nombre", "edad", "ocupación"]
value = ["Juan", 30, "Ingeniero"]
diccionario = [{key[i]: value[i] for i in range(len(key))}]

print(diccionario)

celcius = [-10, 0, 10, 20, 30, 40]

fahrenheit = [(temp * 9 / 5) + 32 for temp in celcius]
print(fahrenheit)

"""


articles = [
    {
        "title": "Python logra nuevo éxito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnología",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "Finance"},
        "description": "Análisis completo",
        "category": "Economía",
    },
    {
        "title": "Nueva tecnología",
        "source": {"name": "TechNews"},
        "description": "Innovación",
        "category": "Tecnología",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "Sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "Política actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "Política",
    },
    {
        "title": "Ciencia avanza",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extraer_titulos_tradicional(articles):
    title = []
    for article in articles:
        title.append(article["title"])
    return title


def extraer_titulos(articles):
    return [article["title"] for article in articles]


print(extraer_titulos_tradicional(articles))
print("==========")
print(extraer_titulos(articles))
