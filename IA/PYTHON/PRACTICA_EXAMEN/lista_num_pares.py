'''
Crea una lista de números aleatorios entre 1 y 20 (usa random).

Genera otra lista que solo tenga los números pares.

Conviértela en set para eliminar duplicados.

Calcula el promedio de los números pares.
'''
import random
lista_numeros = [random.randint(1,20) for i in range(15)]
print(f"me la chupas{lista_numeros}")

lista_pares = [i for i in lista_numeros if i % 2 == 0]

print(f"Lista pares {lista_pares}")

pares_set = set(lista_pares) 
print(f"lista pares sin duplicados {pares_set}")

promedio = sum(pares_set) / len(pares_set)

print(f"promedio {promedio}")