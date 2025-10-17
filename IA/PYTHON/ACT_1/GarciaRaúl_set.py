# ? -----------------------QUE SON LES SETS?-----------------------------------
# - SETS: És una llista desordenada pero que si es pot modificar, es defineix amb claudators {}.
set1 = {1, "hola", 3.14}
set2 = {1, 2, 3, 4, 5}
set3 = {"a", "b", "c", "d"}
# print(set1)
# print(set2)
# print(set3)
# ? -----------------------QUE FAN ELS SETS?-----------------------------------
# S'utlitzen per guardar dades que son uniques i no vols que es repeteixin al executar el programa, com per exemple el nom d'un usuari.
set4 = {"Raul", "Maria", "Joan", "Raul"} # Aqui per exemple el nom "Raul" no es repetira quan s'executi el programa.
set5 = {1, 2, 3, 4, 5, 1, 2, 3}
set6 = {"a", "b", "c", "d", "a", "b", "c"}
# print(set4)
# print(set5)
# print(set6)
# ? -----------------------PER A QUE SERVEIXEN ELS SETS?-----------------------
# Es po tutilitzar per exemple per fer grups de treball que no vols que es repeteixin els membres.
grup_treball = {"Programador", "Dissenyador", "Tester", "Programador"}
nom_empresa = {"TechCorp", "InnovaSoft", "CodeWorks", "TechCorp"}
institut = {"Daniel Balart", "Montilivi", "La Salle", "Daniel Balart"}
# print(nom_empresa)
# print(institut)
# print(grup_treball)
# ? -----------------------DIFERENCIA ENTRE TUPLES, SETS I LLISTES--------------
#| Característiques      | Tupla                                | Set                                            | Llista                       |
#|-----------------------|--------------------------------------|------------------------------------------------|------------------------------|
#| Ordre                 | Ordenada                             | Desordenada                                    | Ordenada                     |
#| Modificar             | No                                   | Sí                                             | Sí                           |
#| Dades duplicades      | Sí                                   | No                                             | Sí                           |
#| Sintaxis              | Parèntesis: ( )                      | Claudators: { }                                | Claudators: [ ]              |
#| Us principal          | Emmagatzemar dades que no vols que   | Emmagatzemar dades úniques sense duplicats     | Emmagatzemar dades que pots canviar |
#                          canviïn 
# ? ----------------------- Utilitza tres mètodes, tant de tuples com de sets, que siguin vàlids. I fes algun càsting entre tuples, sets i llistes per veure el que passa.  Respon: Creus que són útils els sets? Per a fer el què? Les tuples en quin moment les utilitzaries?  -----------------------
set7 = {1, 2, 2, 3}

# 3 mètodes fàcils
print(len(set7))       # longitud que te el set (quants elements té) = 3
print(set7.add(4))     # Afegeix un element al set = {1,2,3,4}
print(set7.remove(1))  # Treu un element del set = {2,3,4}
print(set7)

# Càstings entre llistes i sets
llista = list(set7)          # Set{} -> Llista[]
print(llista)               # {1, 2, 2, 3} -> [1, 2, 3, 2]

set2 = set(llista)          # Llista[] -> Set{}
print(set2)                 # [1, 2, 3] -> {1, 2, 3}