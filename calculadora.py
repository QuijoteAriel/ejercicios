def main():
    
    while True:
        print('''

        CALCULADORA !!!
        
        1. Suma
        2. Resta
        3. Multiplicacion
        4. Division

        0. Salir
        ''')

        try:
            t_calculo = int(input('Elije una operaion: '))
        except ValueError:
            print('ingrese una opcion valida ')
            continue
        if t_calculo == 1:
            print('Suma ')
            suma()
        elif t_calculo == 2:
            print('Resta ')
            resta()
        elif t_calculo == 3:
            print('Multiplicacion ')
            multiplicacion()
        elif t_calculo == 4:
            print('Division ')
            division()
        elif t_calculo == 0:
            print('Salir de Calculadora ')
            break
        else:
            print('elije una opcion valida ')
            continue

def suma():
    n1 = int(input('primer numero : '))
    n2 = int(input('segundo numero : '))
    suma = n1 + n2
    print(f' {n1} mas {n2} es :', suma)

def resta():
    n1 = int(input('primer numero : '))
    n2 = int(input('segundo numero : '))
    resta = n1 - n2
    print(f' {n1} menos {n2} es :',str(resta))


def multiplicacion():
    n1 = int(input('primer numero : '))
    n2 = int(input('segundo numero : '))
    multi = n1 * n2
    print(f'{n1} por {n2} es : ', multi)

def division():
    n1 = int(input('primer numero : '))
    n2 = int(input('segundo numero : '))
    
    try:
        n1, n2 == 0:
           
    except ZeroDivisionError:
         print('no se puede dividir entre 0 cero')
    if n2 == 0:    
            print('no se puede dividir entre 0 ')
        break
        #    n1 = int(input('primer numero : '))
        #    n2 = int(input('segundo numero : '))
        #    print('no se puede dividir por 0')
        

        else:
            divi = n1 / n2
            print(f'{n1} por {n2} es : ', divi)



if __name__ =="__main__":
    main()

