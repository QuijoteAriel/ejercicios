import os
import subprocess

try:
    os.system('mkdir -p ~/Documentos/python')
    os.system('cp *.py ~/Documentos/python')

    os.system('mkdir -p ~/Documentos/csv')
    os.system('cp *.csv ~/Documentos/csv')
        
    os.system('mkdir -p ~/Documentos/json')
    os.system('cp *.json ~/Documentos/json')

    os.system('mkdir -p ~/Documentos/js')
    os.system('cp *.js ~/Documentos/js')
    

    os.system('mkdir -p ~/Documentos/c')
    os.system('cp *.c ~/Documentos/c')

except FileNotFoundError as error:
    print(error)



