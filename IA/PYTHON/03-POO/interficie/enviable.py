'''
En les interfícies no pot haver-hi contructor perquè ja estaríem definint les classes
Per tant només podem definir els mètodes com a tal
'''

from abc import ABC, abstractmethod

class Enviar(ABC):
    
    @abstractmethod
    def enviar(self):        
        pass
    
    # ! No podem definir res més