'''
self._variable->convencional només es pot accedir dins de la mateixa classe i subclasses
self.__variable->només es pot accedir dins de la mateixa classe
Crear alumne1.__nom = ... fora de la classe no sobreescriu atribut privat, només crea un altre atribut.
'''

class Alumnat:
    
    __ID=0

    def __init__(self, nom, cognoms, edat:int, curs:dict):
        Alumnat.__ID+=1
        self.__id=Alumnat.__ID
        self.__nom=nom
        self.__cognoms=cognoms
        self.__edat=edat
        # assegurem que sempre es passin aquest valors al diccionari
        self.__curs = {
            "cursant": curs.get("cursant", "Desconegut"),
            "titols": curs.get("títols", "Sense títols")
        }

    @property
    def nom(self):
       return self.__nom
   
    @nom.setter
    def nom(self, nom):
       self.__nom = nom 
    
    @property
    def curs(self):
        return self.__curs
    
    # només podem passar un paràmetre!!!
    @curs.setter
    def curs(self, noucurs:dict):
        # aquí sobreescriurà les claus amb els nous valors que afegim
        self.__curs.update({
            "cursant": noucurs["cursant"],
            "titols": noucurs["titols"],
        })
    
    def __str__(self):
        return f"""
        ID Alumne: {self.__id}
        Alumme: {self.__nom} {self.__cognoms},
        Edat: {self.__edat}
        Formació: {self.__curs.get("cursant")}, {self.__curs.get("títol")}
        """   

if __name__ == "__main__":

    alumne1=Alumnat("Xavi", "Bertran Fleitas", 43, {})
    print(alumne1)  
    
    # El que fa no és modificar l’atribut privat original (_Alumnat__nom), sinó afegir un atribut nou a l’objecte alumne1.
    alumne1.__nom="Maria"
    
    # accés propietat en setter 
    alumne1.nom="Maria"
    # imprimim propietat en getter
    print(alumne1.nom)

    # canvi curs
    alumne1.curs={
        "cursant":"2on DAW",
        "titols":"Batxillerat, SMIX"
    }

    # ? amb dict veiem els atributs------------------------------------------------------------
    print(alumne1.__dict__)