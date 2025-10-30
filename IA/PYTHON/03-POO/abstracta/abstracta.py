'''
Què és una classe abstracta: Seria una classe que serveix com a plantilla 
amb unes propietats i mètodes prefixats, aquesta classe no es podrà implementar, sí modificar.
Perquè una classe sigui abstracta ha de tenir un mètode abstracta
'''
# necessitem importar aquesta llibreria i aquests dos mètodes
from abc import ABC, abstractmethod

# definim que és abstracta
class Persona(ABC):
    
    # hem de posar o no hem de posar constructor?! Aquesta és la qüestió...ho podem fer
    def __init__(self, nom:str):
        # Evitar el doble guió ja que farà molt complicat importar les propietats
        self._nom=nom
    
    # entrem dins d'una propietat, definim que hi ha d'haver un getter i un setter però res més   
    @property
    @abstractmethod
    def nom(self):
        pass
    
    @nom.setter
    @abstractmethod
    def nom(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass
    
    @abstractmethod
    def menjar(self):
        pass
    
    @abstractmethod
    def __str__(self):
        #? aquí si que definim el comportament
        return f"Nom: {self._nom}"