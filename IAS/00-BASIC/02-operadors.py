'''
Operadors com funciona en Python 
'''
# importar llibreries * tot, nom funció
from math import *

total=0

# ? operadors operacions mates -------------------------
total+=1
total*=2

# residu
dividir=4%2
print(dividir)

print(total)

# arrodonir cap avall amb //
total_dividir=63//2
print(f"total_dividir:{total_dividir}")

# exponent
print(4**3) 

# ? operadors lògics -----------------------------

# and=&& si una False tot false
print(True and False and True)

# si una True tot True or=>||
print(True or False or False)