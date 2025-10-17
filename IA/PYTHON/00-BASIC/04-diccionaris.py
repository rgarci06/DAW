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

#? per obtenir valor si no existeix clau retorna None -------------------
print(dies.get("Pepito"))

abc={"b":"2", "c":"3", "a":"1"}
abc_ordre=dict(sorted((abc.items())))
print(abc_ordre)

