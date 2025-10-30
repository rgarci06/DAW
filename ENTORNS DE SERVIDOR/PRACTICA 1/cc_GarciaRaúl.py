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

import random
class CompteCorrent:

    _seguent_id = 1

    def __init__(self, dni: str, nom: str, cognoms: str, saldo_inicial: float):
        self.__id = CompteCorrent._seguent_id #    self.__id = random.randint(1,100000000000000000000000)
        CompteCorrent._seguent_id += 1
        self.__num_compte = random.randint(1_000_000_000, 9_999_999_999)
        self.__dni = dni
        self.__nom = nom
        self.__cognoms = cognoms
        self.__saldo = float(saldo_inicial)

    def ingressar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat
            print(f"S'han ingressat {quantitat}€. El teu saldo és: {self.__saldo}")
        else:
            print("La quantitat no es correcte.")

    def retirar(self, quantitat):
        if quantitat > self.__saldo:
            print("No tens saldo")
        elif quantitat <= 0:
            print("La quantitat no es correcte.")
        else:
            self.__saldo -= quantitat
            print(f"S'han retirat {quantitat}€. El teu saldo es: {self.__saldo}")

    def veure_saldo(self):
        print(f"Saldo actual: {self.__saldo}")

    def veure_dades(self):
        print("---- DADES DEL TEU COMPTE ----")
        print(f"ID del compte: {self.__id}")
        print(f"Numero del compte: {self.__num_compte}")
        print(f"DNI: {self.__dni}")
        print(f"Nom del titular: {self.__nom} {self.__cognoms}")
        print(f"Saldo actual: {self.__saldo}€")
        print("------------------------------")