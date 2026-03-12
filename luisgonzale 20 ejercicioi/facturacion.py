print ("EJERCICIO 1")
# Contadores de cada sabor
vainilla = 0
chocolate = 0
fresa = 0

# Registrar 5 pedidos
for i in range(5):
    sabor = input("Ingrese el sabor del helado (vainilla, chocolate, fresa ): ").lower
    if sabor == "vainilla":
        vainilla += 1
    elif sabor == "chocolate":
        chocolate += 1
    elif sabor == "fresa":
        fresa += 1
    else:
        print("Sabor no válido")

# Mostrar resultados
print("\nResultados de los pedidos:")
print("Vainilla:", vainilla)
print("Chocolate:", chocolate)
print("Fresa:", fresa)