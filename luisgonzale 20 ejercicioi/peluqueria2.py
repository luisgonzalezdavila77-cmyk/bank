total = 0

corte = 0
cepillado = 0
tintura = 0

for i in range(7):
    nombre = input("Nombre: ")
    servicio = input("Servicio (corte/cepillado/tintura): ")
    valor = int(input("Valor pagado: "))

    total += valor

    if servicio == "corte":
        corte += 1
    elif servicio == "cepillado":
        cepillado += 1
    elif servicio == "tintura":
        tintura += 1

print("Total del día:", total)
print("Cortes:", corte)
print("Cepillados:", cepillado)
print("Tinturas:", tintura)