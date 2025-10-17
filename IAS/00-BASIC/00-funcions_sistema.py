# Primer programa a la classe=> comentaris en Python
"""
Comentaris de més d'una línia
"""

# ? variables ------------------------------------------------------------

# deconstrucció de String, variables
nom="Xavi"
x, a, v, i=nom
edat1, edat2, edat3=12, 13, 666

print(a)
print(edat3)

# ? type funció per saber quin tipus de variable és -----------

print(type(edat3))
print(type(nom))
nom=33
print(type(nom))

# ? casting-> canviar tipus de variable --------------------------------------------------

num="23"
num=int("23")
print(type(num))


# ? modificar prints SuperStrings ------------------------------------------

# super String f""{variable}"
soldat=666
print(f"Baixant de la font del gat una noia i un {soldat}")
PI=3.149

# una manera de rodonir int i float amb super
print(f"El nombre pi és: {PI:.2f}")

# posar espais com volem
print(f"""
Aquesta és la primera línia
    Aquesta és la segona
Ja estic cansat de la classe

""")

# ?  constant=> canvien valor, majúscules avís a developers -----------------------------------------

PI="Les constant no em molen!!"
print(PI)


# ? funció input=> interacció usuari, valor guardar retorna str-----------------------------

edat=0
edat=input("Quina edat tens: ")
print(edat)

# valor "" si usuari no posa res
animal=input("Digues un animal: ")
print(animal)


# ? esborrar de la memòria -----------------------------------

del(num)
print(num)