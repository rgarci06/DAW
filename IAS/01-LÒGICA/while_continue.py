'''
Fes una llista del 1 al 100 que quedin exclosos el 25, 57, 68, 87
'''
# variable de control del while
cont=1
resultat=[]

# condició
while cont<=100:
    if cont==25 or cont==57 or cont==68 or cont==87:
        cont+=1
        # salta línia però dins de la mateix identació si no torna al principi
        continue
    resultat.append(cont)
    # variable control del while
    cont+=1

for num in resultat:
    # end mostra com vols que sigui el resultat final del print
    print(num, end=" ")