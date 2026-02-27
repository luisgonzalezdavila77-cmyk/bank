saldo = 0
op = "0"

print("🏛️ Bienvenido 🏛️")

while op != "4":
    print("\n1. retirar")
    print("2. deposito")
    print("3. ver saldo")
    print("4. cancelar")

    op = input("elige una opcion: ")

    if op == "1":
        texto = input("¿Cuánto vas a retirar?: ").replace(",", ".")
        try:
            monto = abs(float(texto))  # acepta +, - o normal
            if monto <= saldo:
                saldo -= monto
                print("Retiro exitoso. Nuevo saldo:", saldo)
            else:
                print("Fondos insuficientes")
        except:
            print("Error: escribe un número válido")

    elif op == "2":
        texto = input("¿Cuánto vas a depositar?: ").replace(",", ".")
        try:
            monto = float(texto)
            if monto > 0:
                saldo += monto
                print("Depósito exitoso. Nuevo saldo:", saldo)
            else:
                print("El depósito debe ser positivo")
        except:
            print("Error: escribe un número válido")

    elif op == "3":
        print("Tu saldo actual es:", saldo)

    elif op == "4":
        print("Gracias por usar el banco")

    else:
        print("Opción inválida")