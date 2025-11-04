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
#El document ha d'estar amb un fitxer cc_cognoms.py i aquest ha de funcionar per main.
# ? -----------------------------------------------------

import random
class CompteCorrent:

    _seguent_id = 1
    # Aqui el que faig es definir una variable amb el que l'usuari a d'omplir, el dni, el nom i cognoms i el saldo
    def __init__(self, dni: str, nom: str, cognoms: str, saldo_inicial: float):
        self.__id = CompteCorrent._seguent_id
        CompteCorrent._seguent_id += 1
        self.__num_compte = random.randint(1_000_000_000, 9_999_999_999)
        self.__dni = dni # Aqui defineixo els selfs per poder utilitzarlos al main.py
        self.__nom = nom
        self.__cognoms = cognoms
        self.__saldo = float(saldo_inicial)
    # El que fan tots aquests properties es retornar el valor de la variable corresponent
    @property
    def _seguent_id(self):
        return self.__id
    
    @property
    def num_compte(self):
        return self.__num_compte

    @property
    def dni(self):
        return self.__dni

    @property
    def nom(self):
        return self.__nom

    @property
    def cognoms(self):
        return self.__cognoms

    @property
    def saldo(self):
        return self.__saldo
           
    # Aqui defineixo una variable per poder ingressar diners dient que si la quantitat que vull afegir es major a 0 s'afegeixi al teu salari, i si la quantitat es negativa dona un avis.
    def ingressar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat
            print(f"S'han ingressat {quantitat}€. El teu saldo és: {self.__saldo}")
        else:
            print("La quantitat no es correcte.")
    # Aqui faig la variable per treure diners dient que si la quantitat es major al saldo de tens doni un avis de que no tens saldo suficient.Despres he possat que si es menor o igual a 0 doni error. I per últim que si el saldo es menor o igual a la quantitat que vols retirar es resti del saldo.
    def retirar(self, quantitat):
        if quantitat > self.__saldo:
            print("No tens saldo")
        elif quantitat <= 0:
            print("La quantitat no es correcte.")
        else:
            self.__saldo -= quantitat
            print(f"S'han retirat {quantitat}€. El teu saldo es: {self.__saldo}")
    # Aquesta variable es per veure el teu saldo
    def veure_saldo(self):
        print(f"Saldo actual: {self.__saldo}")
    # I aqui per últim faig prints per mostrar totes les dades del compte.
    def veure_dades(self):
        print("---- DADES DEL TEU COMPTE ----")
        print(f"ID del compte: {self.__id}")
        print(f"Numero del compte: {self.__num_compte}")
        print(f"DNI: {self.__dni}")
        print(f"Nom del titular: {self.__nom} {self.__cognoms}")
        print(f"Saldo actual: {self.__saldo}€")
        print("------------------------------")