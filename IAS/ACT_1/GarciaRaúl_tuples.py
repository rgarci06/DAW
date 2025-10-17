# ? -----------------------QUE SON LES TUPLES-----------------------
# - TUPLES: És una llista ordenada que no es pot modificar, es defineix amb parentesis ().
tupla1 = (1, "hola", 3.14)
tupla2 = (1, 2, 3, 4, 5)
tupla3 = ("a", "b", "c", "d")
# print(tupla1)
# print(tupla2)
# print(tupla3)
# ? -----------------------QUE FAN LES TUPLES?-----------------------------------
# S'utilizen per guardar dades que no vols que canviin en la ejecució del programa, com per exemple unes coordenades.
tupla4 = (10.0, 20.0) # Aqui per exemple quan s'executi el programa les coordenades no canviaran.
tupla5 = (100, 200, 300, 400, 500)
tupla6 = ("x", "y", "z", "w", "v")
# print(tupla4)
# print(tupla5)
# print(tupla6)
# ? -----------------------PER A QUE SERVEIXEN LES TUPLES?-----------------------
# S'utilitzen en jocs per exemple per guardar les coordenades d'un personatge que no vol que canviin.
coordenades_personatge = (100, 200) # Aquestes coordenades no canviaran en la ejecució del joc i el personatge sempre començarà en aquesta posició.
coordenades_bruixola = (0, 0)
coordenades_inventari = ("espasa", "escut", "poció")
# print(coordenades_personatge)
# print(coordenades_bruixola)
# print(coordenades_inventari)
# ? -----------------------DIFERENCIA ENTRE TUPLES, SETS I LLISTES-----------------------
#| Característiques      | Tupla                                | Set                                            | Llista                       |
#|-----------------------|--------------------------------------|------------------------------------------------|------------------------------|
#| Ordre                 | Ordenada                             | Desordenada                                    | Ordenada                     |
#| Modificar             | No                                   | Sí                                             | Sí                           |
#| Dades duplicades      | Sí                                   | No                                             | Sí                           |
#| Sintaxis              | Parèntesis: ( )                      | Claudators: { }                                | Claudators: [ ]              |
#| Us principal          | Emmagatzemar dades que no vols que   | Emmagatzemar dades úniques sense duplicats     | Emmagatzemar dades que pots canviar |
#                          canviïn 
# ? ----------------------- Utilitza tres mètodes, tant de tuples com de sets, que siguin vàlids. I fes algun càsting entre tuples, sets i llistes per veure el que passa.  Respon: Creus que són útils els sets? Per a fer el què? Les tuples en quin moment les utilitzaries?  -----------------------
tupla = (1, 2, 3, 2)

# 3 mètodes
print(len(tupla))      # longitud de la tupla (quants elements té) = 4
print(tupla.count(2))  # Compta quantes vegades surt el 2 = 2
print(tupla.index(3))  # Diu la posició del 3 = 2

# Càstings entre llistes i tuples
llista = list(tupla)        # Pasa la tupla() a llista[] 
print(llista)               # (1, 2, 3, 2) -> [1, 2, 3, 2]

tupla2 = tuple(llista)      # Pasa la llista[] a tupla() 
print(tupla2)               # [1, 2, 3, 2] -> (1, 2, 3, 2)