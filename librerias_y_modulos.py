import os

#obtener la rura donde estoy
''' 
cwd = os.getcwd()
print(cwd)

''' 

#listar directorios

txt_files = [ f for f in os.listdir('.') if f.endswith('.py') ]
print('los archivos .py son ', txt_files)

os.rename('primo.js','primero.py')
print('archivo cambiado')

txt_files = [ f for f in os.listdir('.') if f.endswith('.py') ]
print('los archivos .py son ', txt_files)

