hora1=5000
extra=3000

print ("parqueo")
print ("ingrese la catidad de horas que desea parquear su vehiculo")
horas=int(input())
if horas<=1:
    print ("el valor a pagar es de", hora1)
elif horas>1:
    valor_extra=(horas-1)*extra
    valor_total=hora1+valor_extra
    print ("el valor a pagar es de", valor_total)           
