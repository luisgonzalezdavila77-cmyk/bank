alimento = 0
juguete = 0
accesorio = 0

for i in range(10):
    categoria = input("Categoría (alimento/juguete/accesorio): ")
    valor = int(input("Valor de la venta: "))

    if categoria == "alimento":
        alimento += valor
    elif categoria == "juguete":
        juguete += valor
    elif categoria == "accesorio":
        accesorio += valor

print("Total alimento:", alimento)
print("Total juguete:", juguete)
print("Total accesorio:", accesorio)

if alimento > juguete and alimento > accesorio:
    print("Mayor venta: alimento")
elif juguete > accesorio:
    print("Mayor venta: juguete")
else:
    print("Mayor venta: accesorio") 