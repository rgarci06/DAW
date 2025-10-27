'''
Pide al usuario una frase.

Cuenta cuántas consonantes hay (ignora espacios y vocales).

Muestra el total.

👉 Practicas: strings, for, if, lower(), lógica.
'''

frase = input("Dime una frase, guapetona: ")
vocales = "aeiouáéíóú"

consonantes = 0

consonantes_lista = []

for letra in frase.lower():
    if letra.isalpha() and letra not in vocales:
        consonantes += 1
        consonantes_lista.append(letra)

print(f"Total de consonantes: {consonantes}")
print(f"Consonantes encontradas: {consonantes_lista}")
