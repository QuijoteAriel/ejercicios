
clientes = ' jose, luis, '

def create_cliente(cliente_name):
    global clientes
    clientes += cliente_name
    _add_comma()

def _add_comma():
    global clientes
    
    clientes += ',' 
if __name__=='__main__':
    create_cliente('xioma, vian , teresa , fabio')
    print(clientes)
