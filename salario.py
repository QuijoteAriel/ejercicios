data = [ 
        { 'name':'juan',
        'salary': 12000,
        'age': 30 },
        
        {'name':'jose',
         'salary': 14000,
         'age': 28},
        
        {'name':'maria',
         'salary': 20000,
         'age': 24}
        ]

def salary_tall(person: list) ->list:
    if person['salary'] > 11000:
        print(f" el salario de {person['name']} es mayor ")
    else:
        print('no gana lo sufciiente')

for person in data:
    salary_tall(person)
