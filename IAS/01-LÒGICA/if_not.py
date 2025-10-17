"""
Crea un programa en Pyhton que gestioni una llista de tasques pendents. El programa ha de fer el següent:
Demanar a usuari que introdueixi una nova tasca.
Comprovar si la tasca ja existeix a la llista.
Si no hi ha elements a la llista mostrar un missatge de que la llista esta buida.
Si la tasca no existeix a la llista, afegir-la i confirmar-ho.
Si la tasca ja existeix, mostrar missatge que ja hi era.
Permetre repetir operacio fins que l'usuari escrigui "sortir".
"""
llista_tasques = []

while True:
    if llista_tasques == []:
        print("La llista esta buida, afegeix una tasca:")

    text = input("Introduieix una tasca (o 'sortir' per acabar):")
    if text.lower() == "sortir":
        print("Adeu!")
        break

    if text in llista_tasques:
        print("Aquesta tasca ja existeix a la llista")
    
    if text not in llista_tasques:
        llista_tasques.append(text)
        print("Tasca afegida correctament")

    print("Llista de tasques:", llista_tasques)
print("Llista final de tasques:", llista_tasques)