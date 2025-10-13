
num1 = int(input("ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    mayor = num1
    menor = num2 
else:
    mayor = num2
    menor = num1
while menor <= mayor:
    if menor %2 == 1:
        print(menor)
    menor += 1
