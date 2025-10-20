'''
Funció que retorna valors guardats en un element iterador.
Els retorna un en un segons la crida amb next(iterador)
Canvíem el return pel yield
'''

# ? generador normal -----------------------------------------------------------------------------

def parells(num: int):

    for i in range(1, num+1):
        if i%2==0:
            # generarem el valor i aquest ha d'anar guardat en una llista
            yield i



if __name__ == "__main__":
    
    print("Comença el codi: ")
    # fem el generador fent la crida de la funció aquest guardarà a dins d'un objecte iterable generator.
    valors=parells(20)
    print("Segueix codi...")
    print("Segueix codi...")
    # a mseura de codi que necessitem crida un valor determinat->next
    n1=next(valors)
    print("Segueix codi...")
    print("Segueix codi...")
    n2=next(valors)
    print(f"El resultat de {n1}+{n2}={n1+n2}")
    print("Segueix codi...")
    n3=next(valors)
    n4=next(valors)
    print(n4)
    print("Fi de codi")