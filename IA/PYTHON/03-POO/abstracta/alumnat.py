'''
classe filla per implementar la classe abstracta
'''
from abstracta import Persona

class Alumnat(Persona):
    
    def __init__(self, nom, curs:str):
        super().__init__(nom)
        self.curs=curs
    
    def dormir(self):
        # aquí definim el comportament ja definit a la classe pare!!!
        return "Dorm"    
    
    def menjar(self):
        return "Menja"
    
    # definim el què farem amb la propietat
    @property
    def nom(self):
        return self._nom
    
    @nom.setter
    def nom(self, valor):
        self._nom = valor
    
    def __str__(self):
        return f"{super().__str__()} i cursa el curs: {self.curs}"
    
        
    
        
        
        