#los bubles while son buclas que se seguiran ejecutando hasta que la condicion sea falsa 
""" 
x= 0
while x < 5:
    x +=1 #suma el iterador en cada vuelta hasta que la condicion se cumpla  
    print(x) 
""" 

i=0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)

frutas = ["Manzana", "Banano", "Cereza"]
adjetivos = ["roja", "madura", "deliciosa"]
for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta,adjetivo)

x= 4
y= 3
z= 5

if x > y and x < z:
    print("true")



