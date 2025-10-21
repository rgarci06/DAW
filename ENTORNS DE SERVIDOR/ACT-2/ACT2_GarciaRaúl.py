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