'''
Super variable per emmagatzemar dades de tot tipus inclús diccionaris, llistes...
va de la posició 0 fins n
'''

# ? llistes de diferents dades-------------------------------------

Bird=["Aler", 2.03, "Celtics", ["1985", "1986", "1982"], True, "Celtics", "Celtics"]
print(Bird)
animals=["tigres", "lleons", "àligues", "Trump", "panteres", "gats", "gossos"]
# array buida
celtics=[]
print(celtics)
# per classe list() per paràmetre un element iterable per fer càsting
bulls=list()
print(bulls)

# ? sumar llistes -------------------------------------------------------------------

total=Bird+animals
print(total)

#? cridar per posició array ------------------------------------------------------

titols_bird=Bird[3]
print(titols_bird)

# ? len compta posicions primera posició 1------------------------------

llarg=len(Bird)
final=Bird[llarg-1]
print(final)

# ? deconstrucció de variables = nombre de posicions array -----------------------------

#pos, altura, equip, titols, retirat=Bird
#print(equip)

# ? afegir element al final -----------------------------------------------------------

Bird.append("Magic")
print(Bird)

# ? eliminar element últim --------------------------------------

Bird.pop()
print(Bird)
# paràmetre index elimina element
Bird.pop(2)
print(Bird)

# ? afegir element segons  (pos, valor) --------------------------

Bird.insert(3, "Jordan")
print(Bird)

# ? remove al primer valor que troba --------------------------------------

Bird.remove("Celtics")
print(Bird)

# ? clear esborrar tota la llista però no de la memòria ----------------------

Bird.clear()
print(Bird)

# ? Agafar elements de llistes amb empanades ---------------------------------

Bird=["Aler", 2.03, "Celtics", ["1985", "1986", "1982"], True, "Celtics", "Celtics"]
print(Bird[1:3])

# nou array al revés 
Bird2=Bird[::-1]
print(Bird2)

# ? ordenar llista, vigilar les majúscules!! ----------------------------------------------

# moficiant llista original, key=funció manera d'ordenar nombre caràcters
animals.sort(key=len)
print(animals)

# nova llista, reverse=>ordre descendent
reves2=sorted(animals, reverse=True)
print(reves2)