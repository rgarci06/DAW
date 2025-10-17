'''
Funcions anònimes aquelles que no tenen nom.
Ens permet després utilitzar funcions d'ordre superior.
Paraula reservada lambda
: substitueixen el return
el resultat del lambda s'ha de guardar en una variable sí o sí
'''

def areatriangle(base: float, altura: float):
    return (base*altura)/2

# variable = lamba (paramestres) : codi
resultat = lambda base, altura: (base*altura)/2
#print(resultat(2,6))

# fer el mateix transformant una data americana a una europea
data="10/17/2025" 
data_europea = lambda data:f"{data[3:5]}/{data[0:2]}/{data[6:10]}"
#print(data_europea(data))


if __name__ == "__main__":
    pass

