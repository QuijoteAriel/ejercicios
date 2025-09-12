"""" def found_type(value):
    return type(value)

reponse = found_type(1)
print(reponse)

response = found_type("jose")
print(reponse)

response = found_type(False)
print(reponse)
def calcular_propina(factura, porcentaje_p):
    print((round(factura * porcentaje_p) / 100),2)



calcular_propina(1524.33,25)


def calculate_tip(bill_amount, tipPercentage):
    tip = bill_amount * (tipPercentage / 100)
    return round(tip, 2)

response = calculate_tip(100, 10)
print(response)

propi = response 

print(propi +1 )


"""
def is_leap_year(year):
    if year <= 0:
        return False 
    
    elif year %4==0 and year %100!=0 or year % 100 ==0 and year %400 ==0:
        return True

    else:
        return False

resultad = is_leap_year(1988)

print(resultad)


