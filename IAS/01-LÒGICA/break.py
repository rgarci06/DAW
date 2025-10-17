llista = []

while True:
    num = int(input("Digues un numero: "))
    if num >0:
        llista.append(num)
    elif num <0:
        print("Error, has introduit un numero negatiu")
        print(llista)
        break;