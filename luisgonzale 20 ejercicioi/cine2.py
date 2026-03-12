capacidad = int(input("Capacidad de la sala: "))

niños = 0
adultos = 0
mayores = 0

for i in range(capacidad):
    edad = int(input("Edad de la persona: "))

    if edad < 18:
        niños += 1
    elif edad < 60:
        adultos += 1
    else:
        mayores += 1

print("Total personas:", capacidad)
print("Niños:", niños)
print("Adultos:", adultos)
print("Adultos mayores:", mayores)