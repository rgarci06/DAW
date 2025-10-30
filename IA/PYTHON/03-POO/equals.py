'''
equals és un mètode que ens permet comparar dues instàncies per saber si són la mateixa o no,
nosaltres sobreescriurem aquest mètode i el farem per comparar si tenen el mateix nom o no
isinstance(objecte, classe)=>ens permet saber si aquella instància pertany aquella classe
'''
class Persona:
    
    def __init__(self, nom: str, edat: int):
        self.__nom=nom
        self.__edat=edat

    # genero el getter per veure el seu nom
    @property
    def nom(self):
        return self.__nom
    
    @nom.setter
    def nom(self, valor):
        if not valor:
            return "Valor ha de ser vàlid"
        self.__nom=valor
    
    def __eq__(self, altre):
        """comparar propietat nom entre dues instàncies de la mateixa classe, valida si hi ha instància d'aquella classe
        
        Args:
            altre (): fa referencia altre instància 

        Returns:
            _type_: bool si és el mateix nom
        """
        if not isinstance(altre, Persona):
            return NotImplemented
        if self.__nom==altre.nom:
            return True
        else: 
            return False       
        
if __name__ == "__main__":
    
    p1=Persona("Xavi", 33)
    p2=Persona("Elena", 23)
    p3=Persona("Xavi", 44)
    
    print(f"És instància: {isinstance(p3, Persona)}")
    print(p2.nom==p3.nom)

    # amb name podem saber el nom de la classe, funció o...si el fitxer es diu main per executar codi
    print(Persona.__name__)
    
    