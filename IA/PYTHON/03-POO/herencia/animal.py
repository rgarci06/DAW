'''
classe pare o superclasse,
En python existeix la múltiple herència QUE EXISTEIXI NO VOL DIR QUE ES PUGUI FER!!!!
Tenim altres mètodes per poder-ho fer com la interfície de POO
'''

class Animal:

    def __init__(self, nom: str, edat: int):
        self.__nom=nom
        self.__edat=edat
    
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, nom:str):
        # ? afegeix validació si cal
        self.__nom = nom

    @property
    def edat(self):
        return self.__edat
    
    @edat.setter
    def edat(self, edat):
        # ? afegeix validació si cal
        self.__edat = edat
    
    def menjar(self):
        return "L'animal menja"
    
    def dorm(self):
        return "L'animal dorm"
    
    def reproduccio(self):
        return "Es reprodueix"
    
    def parlen(self):
        return "Els animals fan el soroll "

    def __str__(self):
        return f"El nom de l'animal és {self.__nom} i té {self.__edat} anys"