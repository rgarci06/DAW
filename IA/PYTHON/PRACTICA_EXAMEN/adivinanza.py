import random

numero_secreto = random.randint(1,100)
win=False

for intento in range(10):
    adivinanza = int(input("Adivina el numero del 1 al 100: "))

    if adivinanza == numero_secreto:
        print("¡Correcto! Has acertado")
        win = True
        break
    elif adivinanza < numero_secreto:
        print("El numero es mayor")
        print(f"Intento: {intento}")
    else:
        print("El numero es menor")
        print(f"Intento: {intento}")

if not win:
    print(f"Se acabaron los intentos, tonto. El numero secreto era {numero_secreto}")
