'''
Anem a veure aquests tipus de funció:
map=>modifica tots els valors d'una llista retornan nou element iterable map
filter=>agafa aquells valors que necessitem, retorna nou element iterable filter, valors que consideri false no
els retorna. 
'''

noms=["goku", "vegeta", "trunks", "yamcha", "krilin"]
nums=[1,2,3,4,5,6,7,8,9]

# ? map retorna objecte iterable map i aquest objecte no es por llegir--------------------------------------

# variable = map(lambda, llista)
nomsMaju=map(lambda nom: nom.capitalize(), noms)
#print(list(nomsMaju))

# ? filter (només retona valors que sigui True) ------------------------------------------------------------

# variable = filter(lambda, llista)
parells=filter(lambda num: num%2==0, nums)
#print(list(parells))