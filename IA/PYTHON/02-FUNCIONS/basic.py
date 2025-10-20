'''
Funció modular codi.
Crida funció perquè s'executi=>return guardar valor o mostrar-lo
'''

def passa():
    # paraula reservada pass per poder passar del codi 
    pass

# paràmetres valors externs
def suma(n1:int, n2:int)->int:
    """Suma valors per paràmetre

    Args:
        n1 (int)
        n2 (int)

    Returns:
        int: resultat de la suma
    """
    return n1+n2
 

# ? args paràmetres infinits retorna tuple-------------------------------------------------------

def valors(*nums):
    for num in nums:
        return num


# ? kwargs paràmetre type dicc per coses molt simples, clau només str ----------------------------------------------------

def jugador(**kwargs):
    return kwargs

if __name__ == "__main__":
   
   print(suma(2,3))
   print(valors(2,3,4,5,6,7,8,8,9,907897,89356773567,"Xavi"))
   print(jugador(nom="Jordan", equip="Bulls", dorsal=23))
    