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

nom_usuari = input("Introdueix el teu nom d'usuari: ")
nom_usuaris = [nom_usuari]

while activitat or data == 0:

    activitat = input(f"Introdueix l'activitat que vols guardar (0 per sortir), {nom_usuari}: ")
    data = input(f"Introdueix la data de l'activitat de {activitat} en format DD/MM/YYYY (0 per sortir), {nom_usuari}: ")

    llista_activitats = {}    
    llista_activitats[data] = activitat

    if activitat == "" or data == "":
        print ("Error")
    
    if activitat == "0":
        print(f"""
        Nom d'usuari: {nom_usuari}
        Nom de l'activitat: {activitat}
        Data: {data_europea}""")
        print(f"Adéu, {nom_usuari}!")
        break
    
    
