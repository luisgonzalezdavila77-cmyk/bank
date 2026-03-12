total_vendido = 0
clientes = 0

cono = 0
vaso = 0
banana = 0

while True:

    producto = input("Producto (cono, vaso, banana split): ").lower()
    cantidad = int(input("Cantidad: "))

    if producto == "cono":
        precio = 3000
        cono += cantidad
    elif producto == "vaso":
        precio = 4000
        vaso += cantidad
    elif producto == "banana split":
        precio = 9000
        banana += cantidad
    else:
        print("Producto no válido")
        continue

    total = precio * cantidad
    print("Total del cliente:", total)

    total_vendido += total
    clientes += 1

    salir = input("¿Desea registrar otro cliente? (si/no): ").lower()
    if salir == "no":
        break


# determinar producto más vendido
if cono > vaso and cono > banana:
    mas_vendido = "cono"
elif vaso > cono and vaso > banana:
    mas_vendido = "vaso"
else:
    mas_vendido = "banana split"


print("Total vendido:", total_vendido)
print("Clientes atendidos:", clientes)
print("Producto más vendido:", mas_vendido)