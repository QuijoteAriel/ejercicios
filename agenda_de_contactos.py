
mi_agenda = []

def agregar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el teléfono: ")
    
    # Aquí creamos el diccionario del contacto
    contacto = {
        "nombre": nombre,
        "telefono": telefono
    }
    
    agenda.append(contacto)
    print(f"Contacto {nombre} y {telefono} guardado exitosamente!")

def mostrar_contactos(agenda):
    print("\n--- LISTA DE CONTACTOS ---")
    if len(agenda) == 0:
        print("La agenda está vacía.")
    else:
        for c in agenda:
            # Ojo aquí con cómo accedemos a los datos
            print(f"Nombre: {c['nombre']} | Teléfono: {c['telefono']}")

def buscar_contacto(agenda):
    nombre_buscado = input("¿Qué nombre buscas?: ")
    encontrado = False
    
    # TODO: Tienes que completar esta parte.
    # 1. Recorre la lista 'agenda'.1
    
    # 2. Si el nombre del contacto coincide con 'nombre_buscado', imprímelo.
    # 3. Cambia la variable 'encontrado' a True.
    
def buscar_contacto(agenda):
    nombre_buscado = input("¿Qué nombre buscas?: ")
    encontrado = False  # PASO 1: Empezamos pesimistas
    
    # PASO 2: El Bucle
    for c in agenda:
        # PASO 3: La comparación
        if c['nombre'] == nombre_buscado:
            print(f"¡Encontrado! Nombre: {c['nombre']} | Teléfono: {c['telefono']}")
            encontrado = True  # ¡Lo encontramos! Cambiamos el estado
    
    # PASO 4: Verificación final
    if not encontrado: # Si 'encontrado' sigue siendo False
        print("No se encontró ese contacto.")
def main():
    
    while True:
        print("\n1. Agregar contacto")
        print("2. Ver contactos")
        print("3. Buscar contacto")
        print("4. Salir")
        
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Opción no válida, intenta de nuevoss.")
            continue

        if opcion == 1:
            agregar_contacto(mi_agenda)
        elif opcion == 2:
            mostrar_contactos(mi_agenda) 
        elif opcion == 3:
            buscar_contacto(mi_agenda)
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo23.")
            

if __name__=='__main__':
    main()
