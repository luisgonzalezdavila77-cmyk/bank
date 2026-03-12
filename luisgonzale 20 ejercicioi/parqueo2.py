total = 0
carros = 0
motos = 0

mayor_pago = 0
vehiculo_mayor = ""

for i in range(8):
    placa = input("Placa: ")
    tipo = input("Tipo (carro/moto): ")
    horas = int(input("Horas parqueado: "))

    if tipo == "carro":
        pago = horas * 4000
        carros += 1
    else:
        pago = horas * 2000
        motos += 1

    total += pago

    if pago > mayor_pago:
        mayor_pago = pago
        vehiculo_mayor = placa

print("Total recaudado:", total)
print("Carros:", carros)
print("Motos:", motos)
print("Vehículo que pagó más:", vehiculo_mayor)
