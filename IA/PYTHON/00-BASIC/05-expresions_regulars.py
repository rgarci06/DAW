'''
Són unes expressions que ens permeten regular i validar una cadena str
'''

# importem llibreria
import re

# amb el mètode compile(r'') definim l'expressió regular que volem
re_email=re.compile('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$')

email="holaalumnes@gmail.com"
erroremail="holaalumnesgmail"

# ? expressió_regular.match(valor) comprovem que compleix la condició si està bé retorna object match, None si no compleix

# si l'expressió regular és curta podem fer-ho tot dins del match.
# re.match(expressió regular, valor)

# casting per true o false
ver1=bool(re_email.match(email))
ver2=bool(re_email.match(erroremail))

print(ver1)
print(ver2)