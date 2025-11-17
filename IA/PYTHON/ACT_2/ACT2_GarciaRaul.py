# ? Investigar la llibreria os de Python:
# ? Què fa? Per què serveix i els principals mètodes que té.
# El modul os permet interactuar amb el sistema operatiu del ordinador, podent manipular fitxers, directoris, gestionar processos...
# ? -----------------------------------------------------------------
# ? Buscar informació sobre el funcionament del with open de Python, fes i contesta:
# ? Què és el buffer i per a què serveix?
# El buffer es un espai de memoria temporal que el que fan es guardar dades abans de que siguin processades, serveix perque no hi hagin diferents velocitats entre la lectura i escriptura de dades.
# ? Crear un fitxer txt.
# ? Escriure contingut dins d'aquest fitxer.
with open("ACT2_GarciaRaul.txt", "x") as f:
    f.write("Aquesta es la primera linia del fitxer.\n")
# ? Llegir-ho i veure el resultat per consola.
with open("ACT2_GarciaRaul.txt", "r") as f:
    content = f.read()
    print(content)
# ? Afegir una altra línia.
with open("ACT2_GarciaRaul.txt", "a") as f:
    f.write("Aquesta es la segona linia del fitxer.\n")
# ? Fes una taula amb les opcions que hi ha per fer amb els fitxers...r, +r, wr...
# r: es per llegir el fitxer, si no existeix dona error
# w: es per escriure al fitxer, si no existeix el crea, si existeix esborra el contingut
# a: es per afegir contingut al fitxer, si no existeix el crea
# x: es per crear un fitxer, si existeix dona error
# b: es per obrir el fitxer en mode binari
# rb: es per llegir el fitxer en mode binari
# wb: es per escriure al fitxer en mode binari
# ab: es per afegir contingut al fitxer en mode binari
# r+: es per llegir i escriure al fitxer, si no existeix dona error
# w+: es per llegir i escriure al fitxer, si no existeix el crea, si existeix esborra el contingut
# a+: es per llegir i afegir contingut al fitxer, si no existeix el crea
# ? Respon: Cal fer servir .close() per tancar el flux dels fitxers amb with open? I el try/except? Quantes línies t'ha fet falta per fer aquestes activitats? Busca un altre llenguatge de programació (Java) i compara.
# Amb el .close() no cal tancar el flux perque el with open ja ho fa automaticament. El try/except no cal possarlo per es recomendable perque garanteix que el fiter es tanqui encara que doni error. M'han fet falta 12 linies per fer l'activitat. Amb java fer aixo són moltes linies més que amb python, en java s'han d'importar biblioteques i altres coses amb python no cal. Em quedo amb python
# ? Creieu que la llibreria os és complementària per fitxers?
# Si, perque es més facil manipular fitxers i directoris amb aixo i estalvia temps i aixi practicar.