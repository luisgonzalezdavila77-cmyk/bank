saldo_ahorros = 0
saldo_corriente = 0
clave_correcta = "Bomberos8*"

# Validar contraseña
clave = input("Ingrese su contraseña: ")

if clave != clave_correcta:
    print("Contraseña incorrecta")
else:
    print("Bienvenido al sistema bancario")

    # Elegir tipo de cuenta
    print("\nSeleccione tipo de cuenta:")
    print("1. Ahorros")
    print("2. Corriente")
    tipo = input("Opción: ")

    if tipo == "1":
        cuenta = "ahorros"
    elif tipo == "2":
        cuenta = "corriente"
    else:
        print("Opción inválida")
        exit()

    # Menú principal
    while True:
        print("\n--- MENÚ ---")
        print("1. Consultar saldo")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")
        op = input("Seleccione: ")

        if cuenta == "ahorros":
            saldo = saldo_ahorros
            otra_cuenta = "corriente"
        else:
            saldo = saldo_corriente
            otra_cuenta = "ahorros"

        if op == "1":
            print(f"Saldo en cuenta {cuenta}:", saldo)

        elif op == "2":
            monto = float(input("Ingrese monto a depositar: ").replace(",", "."))
            impuesto = monto * 0.004
            monto_final = monto - impuesto
            saldo += monto_final
            print("4x1000 cobrado:", impuesto)
            print("Monto consignado:", monto_final)

        elif op == "3":
            monto = float(input("Ingrese monto a retirar: ").replace(",", "."))
            impuesto = monto * 0.004
            total = monto + impuesto

            if total > saldo:
                print("Saldo insuficiente en cuenta", cuenta)
                cambiar = input(f"¿Desea intentar con la cuenta {otra_cuenta}? (s/n): ").lower()

                if cambiar == "s":
                    if otra_cuenta == "ahorros":
                        saldo_otro = saldo_ahorros
                    else:
                        saldo_otro = saldo_corriente

                    if total > saldo_otro:
                        print("Tampoco hay saldo suficiente en la otra cuenta.")
                    else:
                        cuenta = otra_cuenta
                        saldo = saldo_otro - total
                        print("Cambio de cuenta exitoso.")
                        print("4x1000 cobrado:", impuesto)
                        print("Retiro realizado desde cuenta", cuenta)

                        if cuenta == "ahorros":
                            saldo_ahorros = saldo
                        else:
                            saldo_corriente = saldo
                else:
                    print("Operación cancelada")

            else:
                saldo -= total
                print("4x1000 cobrado:", impuesto)
                print("Retiro exitoso")

        elif op == "4":
            print("Gracias por usar el sistema")
            break

        else:
            print("Opción inválida")

        # Guardar saldo actualizado
        if cuenta == "ahorros":
            saldo_ahorros = saldo
        else:
            saldo_corriente = saldo