total_dia = 0

while True:
    producto = input("Producto (café, capuchino, pastel o salir): ")

    if producto == "salir":
        break

    if producto == "café":
        precio = 4000
    elif producto == "capuchino":
        precio = 7000
    elif producto == "pastel":
        precio = 6000
    else:
        print("Producto no válido")
        continue

    cantidad = int(input("Cantidad: "))
    total = precio * cantidad

    if total > 20000:
        descuento = total * 0.10
        total -= descuento

    print("Total cliente:", total)

    total_dia += total

print("Total del día:", total_dia)