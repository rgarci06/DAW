'''
Anem a veure una primera classe d'exemple sense encapsular:
__init__: per fer el mètode constructor
self: per fer referència a la classe en si mateixa. En aquest cas seria self=Alumnat. Referència a la instància de classe
cls: per definir una propietat de classe i s'utilitza a través de @classmethod
'''
# importem llibreria de poder fer expressions regulars
import re

# paraula reservada class
class Persona:

    # variable de classe
    ID=0

    # definim constructor (paràmetres que hem de passar aquells que no són de generació automàtica)
    def __init__(self, nom: str, cognoms: str, edat: int):
        # es fa la crida de la funció a través de la nom de classe
        self.id=Persona.generarID()
        self.nom=nom
        self.cognoms=cognoms
        self.edat=edat
        self.dni=self.generarDNI()
    
    # és un decorador que ho veurem més endavant el funcionament
    @classmethod
    def generarID(cls):
        # cls=Alumnat.ID
        cls.ID+=1
        return cls.ID

    def generarDNI(self):
     while True:
        op=int(input("Quin document tens (1)DNI o (2)NIE: "))
        match op:
            case 1:
              dni=input("Introdueix DNI: ")
              validacio=bool(re.match(r'^\d{8}+[A-Z]$', dni))
              if validacio:
                 # vigilar en posar self.dni=dni ja estem dintre un self.
                 return dni
              if not validacio:
                 print("Error en DNI")
            case 2:
               nie=input("Introdueix NIE: ")
               validacio=bool(re.match(r'^[A-Z]+\d{6}+[A-Z]$', nie))
               if validacio:
                 return nie
               if not validacio:
                 print("Error en NIE")
            case _:
                print("Error en opció!")
    
    #? aquest mètode ens permet imprimir les propietats através de print sempre ha de tenir return ----------------
    def __str__(self):
       return f"ID: {self.id:}, nom: {self.nom}, cognoms: {self.cognoms}, edat: {self.edat}, DNI: {self.dni}"
    
if __name__ == "__main__":
    # instància
    p1=Persona("James", "Hetfield", 62)
    print(p1)
    p2=Persona("Brian", "Adams", 65)
    print(p2)