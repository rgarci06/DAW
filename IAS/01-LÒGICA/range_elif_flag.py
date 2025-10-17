'''
Escriu un programa que mostri per consola (amb un print) els
números d'1 a 100 (tots dos inclosos i amb un salt de línia entre
cada impressió), substituint els següents:
- Múltiples de 3 per la paraula "fizz".
- Múltiples de 5 per la paraula "buzz".
- Múltiples de 3 i de 5 alhora per la paraula "fizzbuzz".
'''

# codi més elegant que validar directament strings
resultats={3:"fizz", 5:"buzz", 35:"fizzbuzz"}

# ? bucle diccionari=>items retorna llistat [(clau, valor), (clau, valor)]
# for clau, valor in resultats.items():
    #print(clau, valor)

# ? flag segons resultats farà una cosa o una altre ---------------------------------

for num in range(1,101): # range últim valor no el té en compte
    if num%3==0 and num%5==0:
        print(num, resultats[35])
    elif num%3==0:
        print(num, resultats[3])
    elif num%5==0:
        print(num, resultats[5])
    










