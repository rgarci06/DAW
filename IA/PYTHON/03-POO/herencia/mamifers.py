# ens reformulem la pregunta si un gos/gat és una Animal? Sí la resposta és sí ja tenim molt a guanyar
# importem la classe
from animal import Animal

# fem herència(classe importar)
class Gos(Animal):

    # paràmetres definits al final del mètode
    def __init__(self, nom:str, edat:int, potes: str, especie="mamífer"):
        # importem els valors de la classe pare amb super()
        super().__init__(nom, edat)
        self.__especie=especie
        self.__potes=potes
    
    def parlen(self):
        # importem els mètodes de la classe pare ()
        return f"{super().parlen()}: borden"
    
    def __str__(self):
        # importem els comportaments de la classe pare...
        return f"{super().__str__()} pertany {self.__especie} i té {self.__potes} potes"

    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, especie:str):
        self.__especie = especie

class Gat(Animal):

    def __init__(self, nom:str, edat:int, potes: str, especie="mamífer"):
        super().__init__(nom, edat)
        self.__especie=especie
        self.__potes=potes

    # sobreescrivim el mètode del pare i importem els seus comportaments
    def parlen(self):
        return f"{super().parlen()}: miaulen"
    