# \t és tabulador i \n és salt de línia
anime="Bola de Drac"
print(anime)

# ? claudators en Sting --------------------------------------

#[valor incial 1: valor final-1]
# 0 no compte res
# -negatius ho te en compte tot
serie="One Piece"
print(serie[:6])
print(serie[1:6])
print(serie[:-3])
print(serie[1:-3])
print(serie[1:])

# ? strip treu espais final string=>formularis ---------------

valor=anime.strip()
print(len(valor))

# ? len=>comptador total de caràcters i posicions=>no int ni float --------------------------------------------------

print("Caràcters anime:", len(anime))

# ? majúscules, minúscules i Capitalize -------------------------------

print(anime.upper())
print(anime.lower())
print(anime.capitalize())

# ? find primer element que troba en posició----------------------------------------------------

# si no hi és -1
print(anime.find("X"))

# ? count comptar caràcters ----------------------

num_a=anime.count("Bola")
print(num_a)

# ? replace canviar valor antic per valor nou -----------------------------
anime=anime.replace("Bola de Drac Z", "Attack on Titans")
print(anime)

# ? split retorna array -----------------------------------------
# caràcter que volem dividir-->no poses res ja agafa espai
llista_anime=anime.split()
print(llista_anime)

# ? join ajuntar array amb un caràcter especial ---------------------------------
# preguntar que pot passar si l'array és int
data=["9","7","2025"] 
print("/".join(data))

# ? validadors de caràcters True/False ------------------------
# si és alfanumèric
nums="123a"
print(nums.isalnum())
# et diu si té lletres
print(nums.isalpha())
# et diu si té nombres
print(nums.isdigit())
