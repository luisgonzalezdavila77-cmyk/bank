lases = int(input("Ingrese la cantidad de clases asistidas en el mes: "))

if clases < 5:
    print("Asistencia baja")
elif 5 <= clases <= 8:
    print("Asistencia media")
else:
    print("Asistencia alta")