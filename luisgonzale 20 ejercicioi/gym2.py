bajo = 0
medio = 0
alto = 0

for i in range(5):
    print("Persona", i+1)

    nombre = input("Nombre: ")
    dias = int(input("Días asistidos en la semana: "))
    minutos = int(input("Minutos promedio entrenados por día: "))

    if dias < 3:
        print(nombre, "→ bajo compromiso")
        bajo += 1
    elif dias <= 4:
        print(nombre, "→ compromiso medio")
        medio += 1
    else:
        print(nombre, "→ compromiso alto")
        alto += 1

print("\nResumen semanal")
print("Bajo compromiso:", bajo)
print("Compromiso medio:", medio)
print("Compromiso alto:", alto)