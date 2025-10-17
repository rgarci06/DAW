'''
Fer un menú amb match que 0 sigui sortir 
i qualsevol altre valor que no estigui al menú mostri un missatge
'''

#? match ideal per fer una cadena de condicionals. Relativament nou a Python --------------

op=int(input("""
Menu:
    1)Opció 1
    2)Opció 2
    3)Opció 3
    0)Exit
    Digues opció: """))

#switch
match op:
    # case=>opció 
    case 1:
        print("Opció 1")
    case 2:
        print("Opció 2")
    case 3:
        print("Opció 3")
    case 0:
        print("Exit")
    # si no es dona el cas
    case _:
        print("Valor Erroni")    