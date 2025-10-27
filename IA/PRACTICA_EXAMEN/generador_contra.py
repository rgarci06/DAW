'''
🎯 Ejercicio 46: Generador de contraseñas seguras

Pide al usuario la longitud deseada de la contraseña (mínimo 8).

Genera una contraseña aleatoria con:

Letras mayúsculas y minúsculas

Números

Símbolos (!@#$%&*)

Muestra la contraseña generada.

Permite generar varias contraseñas si el usuario quiere.

👉 Practicas: random.choice, strings, while, funciones, loops.
'''

import random

def generar_contraseña(longitud):
    abc_minus = "abcdefghijklmnopqrstuvwxyz"
    abc_mayus = abc_minus.upper()
    numeros = "0123456789"
    simbolos = "!@#$%&*"

    todas = abc_minus + abc_mayus + numeros + simbolos
    contraseña = []

    contraseña.append(random.choice(abc_minus))
    contraseña.append(random.choice(abc_mayus))
    contraseña.append(random.choice(numeros))
    contraseña.append(random.choice(simbolos))

    while len(contraseña) < longitud:
        contraseña.append(random.choice(todas))

    return "".join(contraseña)

while True:
    longitud = int(input("Dime la longitud de la contraseña (mínimo 8, maximo 100): "))
    if longitud < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        continue
    if longitud > 100:
        print("La contraseña es demasiado larga, inutil.")
        continue

    print("Tu contraseña es:", generar_contraseña(longitud))

    repetir = input("¿Quieres generar otra contraseña? (s/n): ").lower()
    if repetir != "s":
        print("¡Hasta luego!")
        break

