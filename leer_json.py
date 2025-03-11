import json

#lectura del json

with open('products.json', mode= 'r')as file:
    products = json.load(file)


for produc in products:
    print(produc)
    print(f"Producto: {produc['name']}, Precio: {produc['price']}")
