# Diccionario global para guardar el stock
# Ejemplo de cómo se verá: {"manzana": 10, "pera": 5}
inventario = {} 

def mostrar_stock():
    print("\n--- BODEGA ---")
    if len(inventario) == 0:
        print("No hay nada en el inventario.")
    else:
        # Ojo aquí, falta algo pequeñito al final de la linea
        for fruta, cantidad in inventario.items():
            print(f"Producto: {fruta} | Cantidad: {cantidad}")

def agregar_cajas():
    fruta = input("¿Qué fruta llegó?: ")
    # CUIDADO AQUÍ: input siempre devuelve texto (string)
    cantidad = input("¿Cuántas cajas llegaron?: ") 

    if fruta in inventario:
        # Si la fruta ya existe, sumamos lo nuevo a lo que había
        inventario[fruta] = inventario[fruta] + cantidad
    else:
        # Si es nueva, la creamos
        inventario[fruta] = cantidad
    
    print(f"Se agregaron {cantidad} cajas de {fruta}.")

def realizar_venta():
    fruta_pedida = input("¿Qué fruta quiere el cliente?: ")
    
    # TODO: Tienes que completar esta parte.
    # 1. Verifica si 'fruta_pedida' EXISTE en el diccionario 'inventario'.
    # 2. Si existe, pide cuántas quiere comprar (conviértelo a entero int()).
    # 3. Verifica si hay SUFICIENTE stock (inventario[fruta_pedida] >= cantidad_cliente).
    # 4. Si alcanza, resta la cantidad al inventario.
    # 5. Si NO alcanza o no existe la fruta, imprime un mensaje de error.
    
    if fruta_pedida in inventario:
        pedido = int(input(f"Cuanta cantidad de {fruta_pedida} , quieres ? "))
        if inventario[fruta_pedida.value] >= pedido:
            

    
    
    
    
    print("Funcionalidad de venta en construcción...") 

def main():
    while True:
        print("\n1. Ver Stock")
        print("2. Reponer Mercadería (Agregar)")
        print("3. Vender")
        print("4. Salir")
        
        opcion = input("--> ")

        if opcion == "1":
            mostrar_stock()  # Aquí pasa algo raro, la función no corre...
        elif opcion == "2":
            agregar_cajas()
        elif opcion == "3":
            realizar_venta()
        elif opcion == "4":
            print("Cerrando caja...")
            break
        else:
            print("Opción incorrecta.")

if '__main__'==__name__:
    main()