# ? ----------DATETIME-------------
from datetime import datetime, date

# Què ens retorni la data i hora actuals
data_hora_actual = datetime.now()
print("Data i hora actuals:", data_hora_actual)

# D'aquesta data i hora actuals fes un type. Per saber quin tipus de variable retorna dita funció.
print("Tipus de variable:", type(data_hora_actual))

# La creació d'una data a través dels paràmetres del constructor datetime i date.
data_creada = datetime(2024, 12, 25, 15, 30, 0)
print("Data creada:", data_creada)

# Amb la funció date que ens retorni la data d'avui.
data_avui = date.today()
print("Data d'avui:", data_avui)

# Aquesta, data d'avui, transformar-la en una data europea amb strftime().
data_europea = data_avui.strftime("%d/%m/%Y")
print("Data europea:", data_europea)

# ? ----------PROGRAMA-------------
# Preguntarem el nom de l'usuari.
# Preguntarem usuari per una activitat posant el nom de l'usuari.
# Preguntarem usuari per aquesta activitat quin dia l'ha de fer. El calendari ha de ser Europeu.
# Si l'activitat és un nombre o una cadena buida dirà que és error i ho tornarà a preguntar.
# Si usuari posa 0 a activitat o a data. Sortirà del programa.
# En sortir del programa mostrarà totes les activitats i les seves dates.
# I dirà adeu a l'usuari amb el seu nom!

from datetime import datetime

# Demana el nom a l'usuari
nom = input("Posa el teu nom d'usuari: ")

# Aqui guardo la informació de les acttivitats
activitats = {}

while True:
    # Demana el nom de l'activitat
    activitat = input(f"Nom de la activitat de {nom} (0 per sortir): ")

    # Si l'usuari vol sortir posa un 0
    if activitat == "0":
        break

    # Si l'usuari no posa res, torna a preguntar
    while activitat == "":
        print("Error: Has d'introduir un nom d'activitat.")
        activitat = input(f"Nom de la activitat de {nom}: ")

    # Demana la data a l'usuari
    data_usuari = input(f"Data de la activitat '{activitat}' (dd/mm/yyyy): ")

    # Valida la data perque estigui en fomat europeu
    try:
        data = datetime.strptime(data_usuari, "%d/%m/%Y").date()
    except ValueError:
        print("Data invàlida. Torna-ho a intentar.")
        continue # Si la data es invalida, torna a començar el segon bucle
    else:
        print("La data és correcta!")

    # Guarda l'activitat al diccionari amb la seva data
    activitats[data.strftime("%d/%m/%Y")] = activitat

# Mostra totes les activitats amb les dates y el nom d'usuari
print("\n--- Resum d'activitats ---")
print(f"Nom d'usuari: {nom}")
for data, act in activitats.items():
    print(f"- {data}: {act}")

print(f"\nAdéu {nom}!")
