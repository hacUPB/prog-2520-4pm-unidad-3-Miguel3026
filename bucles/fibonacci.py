numero = int(input("ingrese el numero de terminos"))
if numero <= 0:
    print("no se imprimen terminos")
elif numero == 1:
    print(0)
else:
    a = 0
    b = 1
    print(a)
    print(b)
    contador = 1
    while contador <= (numero - 2):
        siguiente = a + b
        a = b
        b = siguiente
        print(siguiente)
        contador += 1