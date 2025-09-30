import random

random_list = []
for i in range (10):
    random_list.append(random.randint(0,20))

ordenar = sorted(random_list)


print(random_list)
print(ordenar)
