'''
Una supermega variable a on podem guardar valors a través de clau:valor
String, int, arrays, dict
'''

# ? exemples de diccionaris ---------------------------------------
dies={1:"dilluns", "2":"dimarts", "llista_compra":{
    "peix": "llenguado",
    "carns": "pollastre",
    "fruita": "peres, mango"
}}

jugadors=dict([(23,"Jordan"), (33,"Bird")])
print(jugadors)

#? crida de diccionaris per clau ----------------------------------

print(dies["llista_compra"])
print(dies["llista_compra"]["fruita"])
dies["llista_compra"]="Son Goku"
print(dies["llista_compra"])

#? saber dades diccionari =>retorna llista segons petició ----------------------------------
print(dies.keys())
print(dies.values())
print(dies.items()) # ho retorna tot
print(type(dies.items()))

#? posar un element nou diccionari -----------------
dies[3]="dimecres"
# si està clau no fa res i si no afegeix al diccionari
dies.setdefault(3, "dijous")
print(dies)

#? per obtenir valor si no existeix clau retorna None, segon argument canvia None per un que vulguem -------------------
print(dies.get("Pepito"))
#print(dies.get("Pepito", ""))=> substitueix None per Pepito

#? Poder ordenar un diccionari --------------------------------

abc={"b":"2", "c":"3", "a":"1"}
abc_ordre=dict(sorted((abc.items())))
print(abc_ordre)

# ? diccionari.update(altre_diccionari) ---------------------------------------------------------------------
# Afegeix totes les claus i valors de altre_diccionari dins de diccionari.
# Si una clau ja existia, el valor es sobreescriu.
# útil per actualitzar diccionaris de classe

dades = {"nom": "Xavi", "edat": 43}
nous_valors = {"edat": 44, "ciutat": "Barcelona"}
# paràmetre nou diccionari
dades.update(nous_valors)
print(dades)

