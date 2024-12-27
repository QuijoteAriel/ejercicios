#import ramdon 
def contrasena():
    p='papa'
    while True:
        palabra= str(input('dime la contraseña '))
        if palabra == p:
            print('contraseña correcta ')
            break
        else:
            print('contraseña incorrecta intente de nuevo ')
contrasena()
