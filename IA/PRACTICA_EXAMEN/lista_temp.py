'''
⚙️ 1. Lista de temperaturas

Genera una lista de 7 temperaturas aleatorias entre -5 y 40.
Muestra:

La temperatura máxima y mínima

El promedio semanal

Cuántos días superan los 30 grados

👉 Practicas: random, listas, min/max, sum/len, count.
'''
import random

temperaturas = []
for _ in range(7):
    temperaturas.append(random.randint(-5,40))

valor_maximo = max(temperaturas)
valor_minimo = min(temperaturas)
promedio = sum(temperaturas) / len(temperaturas)
dias_calor = sum(1 for t in temperaturas if t > 30)


print(f"Temperaturas registradas: {temperaturas}")
print(f"La temperatura máxima es: {valor_maximo}°C")
print(f"La temperatura mínima es: {valor_minimo}°C")
print(f"El promedio semanal es: {promedio:.2f}°C")
print(f"Días con más de 30°C: {dias_calor}")