import csv

#leer todo el archivo
''' 
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
''' 

#mostrar columnas de interes 
''' 
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: :{row['name']}, Precio: {row['price']}")

'''
#nuevo producto
'''
new_product = {
        'name': 'cargador inalambrico',
        'price': 75,
        'quantity': 100,
        'brand': 'chino',
        'category': 'Accessories',
        'entry_date': '2024-02-02'
        }

with open('products.csv', mode= 'a', newline= '') as file:
    #file.write('\n')
    csv_writer = csv.DictWriter(file, fieldnames = new_product.keys())
    csv_writer.writerow(new_product)

''' 

# crear un nuevo archivo

file_path = 'products.csv'
updated_file_path = 'produc_updated.csv'

with open(file_path, mode= 'r')as file:
    csv_reader = csv.DictReader(file)
    #obtener los nombres de las columnas
    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames = fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            row['total_value']= float(row['price'])* int(row['quantity'])
            csv_writer.writerow(row)
