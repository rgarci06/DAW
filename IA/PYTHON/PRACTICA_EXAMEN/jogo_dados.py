"""Genera un juego de 2 jugadores.

Cada jugador lanza 3 dados (1–6).

Calcula la suma de los dados para cada jugador.

Muestra el resultado de cada jugador y quién gana.

Permite repetir el juego hasta que el usuario escriba “salir”.

👉 Practicas: random.randint, listas, while, for, if/else, acumuladores."""
import random
valores1=[]
valores2=[]
while True:
    nom=input("Quien eres ")
    for i in range(3):
        input("!Tira el dado!")
        valor1=random.randint(1,6)
        print(f"A salido {valor1}")
        valores1.append(valor1)

    suma_total1 = sum(valores1)
    print(f"\n Suma total de {nom} es {suma_total1}")
    input("Turno de la maquina")

    for i in range(3):
        valor2=random.randint(1,6)
        print(f"La maquina a sacado {valor2}")
        valores2.append(valor2)

    suma_total2 = sum(valores2)
    print(f"Suma total de la maquina {suma_total2}")

    print(f"""\n----Resultados----

{nom} a sacado {suma_total1}
La maquina a sacado {suma_total2}""")

    if suma_total1 > suma_total2:
        print(f"!A ganado {nom}!")
        break
    if suma_total1 < suma_total2:
        print(f"!A ganado La maquina, se siente!")
        break
    if suma_total1 == suma_total2:
        print(f"empate")
        break