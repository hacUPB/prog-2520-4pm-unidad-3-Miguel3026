numero = 1
while numero >= 0:
    print(numero)
    numero += 1            #numero = numero + 1

#Imprimir los numeros pares entre el 20 y el 80:
numero = 20
while numero <= 80:
    if numero % 2 == 0:
        print(numero)
    numero += 1

#Imprimir los numeros impares entre 99 y 61, en orden descendente:
numero = 99
while numero >= 61:
    if numero % 2 != 0:
        print(numero)
    numero -= 1

#Solicitar dos numeros al usuario e imprimir los numeros impares entre ellos:
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1
while menor <= mayor:
    if menor % 2 == 1:
        print(menor)
    menor += 1

#Imprimir los multiplos de 7 entre 0 y 100:
numero = 0
while numero <= 100:
    if numero % 7 == 0:
        print(numero)
        numero += 1

#Solicitar un numero al usuario e imprimir su tabla de multiplicar hasta el 15
numero =int(input("Ingrese un numero:"))
i = 1
while i <= 15:
    resultado = i * numero 
    print(f"{numero} x {i} = {resultado}")
    i += 1 
    