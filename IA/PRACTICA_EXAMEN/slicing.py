# ============================================================
# SLICING EN PYTHON (empanadillas) - Apuntes con ejemplos
# Autor: Joel (apuntes)
# Ejecuta este archivo para ver los resultados y revisa los comentarios.
# ============================================================

# ---------
# Cadena base
# ---------
serie = "One Piece"  # índices: 0:O 1:n 2:e 3:' ' 4:P 5:i 6:e 7:c 8:e
# len(serie) == 9

print("=== BÁSICOS (start:stop) ===")
print(serie[:])         # Todo -> "One Piece"
print(serie[0:3])       # 0..2 -> "One"
print(serie[:6])        # inicio..5 -> "One Pi"
print(serie[1:6])       # 1..5 -> "ne Pi"
print(serie[4:])        # 4..fin -> "Piece"
print()

print("=== ÍNDICES NEGATIVOS ===")
print(serie[-1])        # último char -> "e"
print(serie[-3:])       # últimos 3 -> "ece"
print(serie[:-3])       # todo menos 3 últimos -> "One Pi"
print(serie[-8:-3])     # -8..-4 -> "ne Pi"
print()

print("=== PASO (step) ===")
print(serie[::2])       # cada 2 -> "OePc"
print(serie[1::2])      # desde 1, de 2 en 2 -> "n e e"
print(serie[:6:2])      # 0..5 de 2 en 2 -> "OeP"
print()

print("=== INVERTIR CON SLICING ===")
print(serie[::-1])      # invertido -> "ecieP enO"
print(serie[6:3:-1])    # 6..4 (desc) -> "e i"
print()

print("=== LIMITES FUERA DE RANGO (no falla) ===")
print(serie[:999])      # corta al final -> "One Piece"
print(serie[-999:3])    # empieza al inicio -> "One"
print()

print("=== SLICING NO MODIFICA STRINGS (son inmutables) ===")
# serie[0] = "A"  # ERROR: TypeError
nueva = "A" + serie[1:]  # crear una nueva cadena
print(nueva)             # "Ane Piece"
print()

print("=== LISTAS: slicing también funciona y SÍ permite asignación ===")
nums = [0, 1, 2, 3, 4, 5, 6]
print(nums[:])           # copia -> [0, 1, 2, 3, 4, 5, 6]
print(nums[2:5])         # [2,3,4]
print(nums[::-1])        # invertida -> [6,5,4,3,2,1,0]

# Reemplazar un trozo
nums[2:5] = [20, 30]     # acorta/ajusta
print(nums)              # [0, 1, 20, 30, 5, 6]

# Insertar sin borrar (rango vacío)
nums[2:2] = [100, 101]
print(nums)              # [0, 1, 100, 101, 20, 30, 5, 6]

# Borrar con slicing
del nums[4:6]
print(nums)              # [0, 1, 100, 101, 5, 6]

# Saltos en listas
print(nums[::2])         # [0, 100, 5]
print()

print("=== TUPLAS: slicing sí, pero no asignación (inmutables) ===")
t = (10, 20, 30, 40, 50, 60)
print(t[1:4])            # (20, 30, 40)
print(t[::-1])           # (60, 50, 40, 30, 20, 10)
# t[1:3] = (99,)        # ERROR
print()

print("=== OBJETO slice ===")
# Útil si quieres reutilizar una “empanadilla”
trozo = slice(1, 6, 2)   # start=1, stop=6, step=2
print(serie[trozo])      # "nP"
print([0,1,2,3,4,5,6][trozo])  # [1,3,5]
print()

print("=== SLICING Y COPIAS RÁPIDAS ===")
lista = [1, 2, 3]
copia = lista[:]         # copia superficial
print(copia)             # [1, 2, 3]
print(copia is lista)    # False (distinta referencia)
print()

print("=== PATRONES ÚTILES ===")
# 1) Quitar primer/último carácter
s = "Python"
print(s[1:-1])           # "ytho"

# 2) Tomar prefijo/sufijo
print(s[:2])             # "Py" (prefijo)
print(s[-2:])            # "on" (sufijo)

# 3) Cada n caracteres (sampling)
print(s[::3])            # "Ph"

# 4) Limpiar espacios laterales de forma “manual” (ejemplo didáctico)
esp = "   hola   "
# normalmente usarías .strip(), pero con slicing:
inicio = 0
fin = len(esp)
while inicio < fin and esp[inicio] == " ":
    inicio += 1
while fin > inicio and esp[fin-1] == " ":
    fin -= 1
print(esp[inicio:fin])   # "hola"
print()

print("=== UNIR SLICING CON MÉTODOS ===")
frase = "one piece is great"
print(frase.title()[:7])   # "One Pie"
print(frase.replace(" ", "_")[:-6])  # "one_piece_is_"
print()

print("=== SLICING EN 2D (listas de listas) ===")
mat = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
]
# Submatriz con filas 0..1 y cols 1..3
sub = [fila[1:3] for fila in mat[:2]]
print(sub)  # [[2, 3], [6, 7]]

# Cada 2 filas y cada 2 columnas
sub2 = [fila[::2] for fila in mat[::2]]
print(sub2)  # [[1, 3], [9, 11]]
print()

print("=== CAZAPIFIAS ===")
# 1) stop es exclusivo
print("ABCDE"[0:2])      # "AB", no incluye el índice 2

# 2) con step negativo, start debe ser > stop para obtener algo
print("ABCDE"[4:1:-1])   # "EDC"
print("ABCDE"[1:4:-1])   # "" (vacío)

# 3) cadenas inmutables: crea nuevas, no modifica la original
x = "ABCDE"
y = x[:2] + "-" + x[2:]
print(x, y)              # "ABCDE", "AB-CDE"

# 4) cuidado con step=0 -> ValueError
try:
    print("ABC"[::0])
except Exception as e:
    print("Error esperado:", type(e).__name__)  # ValueError
print()

print("=== PRACTICA RÁPIDA ===")
texto = "Empanadillas"
# a) "Empa"
print(texto[:4])         # "Empa"
# b) "dillas"
print(texto[-6:])        # "dillas"
# c) "Epdla" (cada 2 desde 0 hasta antes del final)
print(texto[0:-1:2])     # "Epadla"
# d) "sallidanapmE" (al revés)
print(texto[::-1])
# e) Quitar la primera y última letra
print(texto[1:-1])       # "mpanadilla"
print()

print("=== FIN ===")