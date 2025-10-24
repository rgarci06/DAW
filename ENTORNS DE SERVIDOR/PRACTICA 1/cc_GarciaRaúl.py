#Propietats encapsulades:
#ID
#Número de 10 xifres creades aleatòriament que serà el número de compte corrent. 
#DNI: es pregunta a l'usuari.
#Nom: es pregunta a l'usuari
#Cognoms: es pregunta a l'usuari
#Saldo inicial: es pregunta a l'usuari
#Mètodes:
#Ingressar diners
#Retirada d'efectiu
#Veure Saldo
#Les dades generals del compte amb el saldo
import random
class cuenta:

    __ID=0
    __num_compte=0

    def __init__(self, DNI: int, nom: str, cognoms: str, salari: int):
        cuenta.__ID =+1
        cuenta.__num_compte = random.randint(0,9999999999)
        self.__DNI = DNI
        self.__nom = nom
        self.__cognoms = cognoms
        self.__salari = salari
        
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, nom):
        self.__nom = nom