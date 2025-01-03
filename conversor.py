'''
Convertidor de Unidades:
Descripción: Un programa que convierte unidades de medida, como centímetros a pulgadas o grados Celsius a Fahrenheit.
Conceptos a Practicar: Funciones, manejo de flotantes, manejo de cadenas.
'''
 

def conversor():
    print('''que quieres convertir ??
        1. cm a pulgadas 
        2. grados centigrados a grador farenhied
          ''')
    
    while True:
        conv = float(input('opcion : '))
        if conv == 1:
            cm =float(input('centimetro '))
            pulgadas = cm / 2.54
            print(f'{cm} centimetros en igual a' , round(pulgadas,2))
    
        elif conv == 2:
            pul = float(input('pulgadas : '))
            centimetro = pul * 2.54
            print(f'{pul} centimetros en igual a' , round(centimetro,2))
        
        elif conv == 0:
            print('saliendo ')
            break
        else:
            print('ingrese una opcion valida')
            continue

if __name__ == '__main__':
    conversor()
