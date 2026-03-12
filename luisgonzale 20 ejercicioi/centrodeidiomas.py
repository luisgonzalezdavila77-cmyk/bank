cantidad = int(input("Número de estudiantes: "))

bajo = 0
medio = 0
alto = 0

mejor_prom = 0
mejor_nombre = ""

suma_prom = 0

for i in range(cantidad):
    nombre = input("Nombre: ")
    speaking = int(input("Speaking: "))
    listening = int(input("Listening: "))
    reading = int(input("Reading: "))

    promedio = (speaking + listening + reading) / 3
    suma_prom += promedio

    if promedio < 60:
        bajo += 1
    elif promedio < 80:
        medio += 1
    else:
        alto += 1

    if promedio > mejor_prom:
        mejor_prom = promedio
        mejor_nombre = nombre

promedio_grupo = suma_prom / cantidad

print("Promedio del grupo:", promedio_grupo)
print("Mejor estudiante:", mejor_nombre)
print("Bajo:", bajo)
print("Medio:", medio)
print("Alto:", alto)