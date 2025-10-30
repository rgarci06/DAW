'''
El polimorfisme permet utilitzar un mateix nom de mètode per a objectes de tipus diferents, 
fent que cada classe executi la seva pròpia versió mètode.
'''

from animal import Animal
from mamifers import *

if __name__ == "__main__":
    
    animal1=Animal("Milú", 10)
    print(animal1)
    gos1=Gos("Milú", 10, 4)
    gos2=Gos("Cuqui", 3, 4)
    print(gos1)
    gos1.nom="Idefix"
    print(gos1)
    gat1=Gat("Garfield", 10, 4)

    #? polimorfisme s'adapta el mètode del mateix nom segons la classe agafa el mètode parlem de gos i gat segons
    #? classe que hem cridat
    animals=[gos1, gat1, gos2]
    for animal in animals:
        print(animal.parlen())