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
    # El que fan tots aquests properties i setters es retornar el valor de la variable corresponent
    @property
    def id(self):
        return self.__id
    
    @property
    def num_compte(self):
        return self.__num_compte

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, nou_dni):
        self.__dni = nou_dni

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nou_nom):
        self.__nom = nou_nom

    @property
    def cognoms(self):
        return self.__cognoms
    @cognoms.setter
    def cognoms(self, nou_cognoms):
        self.__cognoms = nou_cognoms

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, nou_saldo):
        if nou_saldo < 0:
            print("El saldo no pot ser negatiu.")
        else:
            self.__saldo = float(nou_saldo)

    # Aqui defineixo una variable per poder ingressar diners dient que si la quantitat que vull afegir es major a 0 s'afegeixi al teu salari, i si la quantitat es negativa dona un avis.
    def ingressar(self, quantitat):
        if quantitat > 0:
            self.saldo += quantitat
            print(f"S'han ingressat {quantitat}€. El teu saldo és: {self.saldo}")
        else:
            print("La quantitat no es correcte.")
    # Aqui faig la variable per treure diners dient que si la quantitat es major al saldo de tens doni un avis de que no tens saldo suficient.Despres he possat que si es menor o igual a 0 doni error. I per últim que si el saldo es menor o igual a la quantitat que vols retirar es resti del saldo.
    def retirar(self, quantitat):
        if quantitat > self.saldo:
            print("No tens saldo")
        elif quantitat <= 0:
            print("La quantitat no es correcte.")
        else:
            self.saldo -= quantitat
            print(f"S'han retirat {quantitat}€. El teu saldo es: {self.saldo}")
    # Aquesta variable es per veure el teu saldo
    def veure_saldo(self):
        print(f"Saldo actual: {self.saldo}")
    # I aqui per últim faig prints per mostrar totes les dades del compte.
    def veure_dades(self):
        print("---- DADES DEL TEU COMPTE ----")
        print(f"ID del compte: {self.id}")
        print(f"Numero del compte: {self.num_compte}")
        print(f"DNI: {self.dni}")
        print(f"Nom del titular: {self.nom} {self.cognoms}")
        print(f"Saldo actual: {self.saldo}€")
        print("------------------------------")
