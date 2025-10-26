import random

# Pide la fecha de nacimiento al usuario
while True:
    try:
        fecha_nacimiento = int(input("Pon el día de tu nacimiento (1-31): "))
        if 1 <= fecha_nacimiento <= 31:
            break
        else:
            print("Error: El día debe estar entre 1 y 31.")
    except ValueError:
        print("Error: Debes introducir un número válido.")

# Genera un número mágico aleatorio entre 1 y 31
numero_magico = random.randint(1, 31)

# Inicializa la variable de victoria y los intentos
victoria = False
intentos = 5

# Bucle para adivinar
while intentos > 0 and not victoria:
    try:
        numero_usuario = int(input(f"Escribe un número del 1 al 31 (te quedan {intentos} intentos): "))
        if 1 <= numero_usuario <= 31:
            if numero_usuario == numero_magico or numero_usuario == fecha_nacimiento:
                victoria = True
                print("¡Has acertado! 🎉")
            else:
                intentos -= 1
                print("Incorrecto. Intenta de nuevo.")
        else:
            print("Número fuera de rango. Intenta de nuevo.")
    except ValueError:
        print("Debes introducir un número válido.")

# Mensaje final
if not victoria:
    print(f"Se acabaron los intentos. El número mágico era {numero_magico}.")
