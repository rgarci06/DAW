'''
Ejercicio 9: Encuesta con estadísticas

Pide a los usuarios que califiquen un producto del 1 al 5 (puedes simular varios usuarios con input).

Guarda las calificaciones en una lista.

Calcula y muestra:

Número de calificaciones de cada valor (usa un diccionario).

Promedio de calificaciones.

Valor más repetido (modo).
'''

calificaciones = []

while True:
    nota = input("calificacion del producto(1-5) pulsa 0 para salir: ")
    if nota == "0":
        break
    if nota not in ["1", "2", "3", "4", "5"]:
        print("calificacion no valida")

    calificaciones.append(int(nota))

cuenta = {}
for nota in calificaciones:
    cuenta[nota] = cuenta.get(nota, 0) + 1

if calificaciones:
    promedio = sum(calificaciones) / len(calificaciones)
else:
    promedio = 0

if cuenta:
    modo = max(cuenta)

print("Resultados: ")
print(calificaciones)
print(cuenta)
print(promedio)
print(modo)