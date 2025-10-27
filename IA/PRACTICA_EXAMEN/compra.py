"""Pide al usuario que ingrese 5 productos y su precio.

Guarda los datos en un diccionario {producto: precio}.

Calcula:

Total de la compra

Producto más caro

Producto más barato

Permite buscar un producto y mostrar su precio.
👉 Practicas: diccionarios, for, input, min/max, sum."""
print("Añade 5 productos con sus precios")
productos={}
for i in range(2):
    producto=input("Nombre del producto ")
    precio=int(input("Precio del producto "))
    #productos es el diccionario, "producto" es la calu(keys), "precio" es el valor(values)
    productos[producto]=precio
    print(f"Llista de la compra: {productos}")
    i += 1
suma_total = sum(productos.values())
print(f"\nSuma total {suma_total}€")

caro_producto=max(productos.keys())
caro_precio=max(productos.values())
print(f"\nEl producto mas alto es {caro_producto} que cuesta {caro_precio}€")

barato_producto=min(productos.keys())
barato_precio=min(productos.values())
print(f"El producto mas alto es {barato_producto} que cuesta {barato_precio}€")


while True:
    opcion=input("""\nque quieres hacer
            1) buscar el precio de un producto
            2) mostrar todos los productos
            3) irte a la mierda """)
    match opcion:
        case "1":
            producto=input("Que producto quieres buscar ")
            if producto in productos:
                print(f"\n-----Del producto: {producto}: su precio es {productos[producto]}€----")
            if producto not in productos:
                print("Producto no encontrado")
                continue
        case "2":
            for producto, precio in productos.items():
                print(f"- {producto}, {precio}")
        case "3":
            print("!!!!chupala!!!!!")
            break