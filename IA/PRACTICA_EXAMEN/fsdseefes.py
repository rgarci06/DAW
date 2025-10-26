'''Ejercicio:
Crea un programa de contactos.
Cada contacto tiene un nombre (clave) y un teléfono (valor).
Permite:

Añadir contacto.

Buscar contacto.

Mostrar todos los contactos.

Salir.

👉 Practicas: diccionarios, match/case, input, control de flujo.'''

contactos = {}

while True:
    print("1. Añadir contacto")
    print("2. Buscar contacto")
    print("3. Mostrar contactos")
    print("4. Salir")

    opcion = input("Elije una opcion:")

    match opcion:
        case "1":
            nombre = input("Nombre:")
            telefono = input("Telefono:")
            contactos[nombre] = telefono
        case "2":
            nombre = input("Nombre del contacto que quieres buscar:")
            if nombre in contactos:
                print(f"{nombre}: {contactos[nombre]}")
            else:
                print("Contacto no encontrado")
        case "3":
            for nombre, telefono in contactos.items():
                print(f"- {nombre}, {telefono}")
        case "4":
            print("Chupala")
            break
