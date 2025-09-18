def primo(valor:int):
    divisor = valor // 2 #división entera
    cont = 0
 
    for i in range(2, divisor + 1):
        if valor % i == 0:
            cont += 1
 
    if cont == 0:
        print(f"{valor} es primo")
    else:
        print(f"{valor} no es primo")
        print(f"Los divisores de {valor} son:")
        for i in range(1, valor+1):
            if valor % i == 0:
                print(i)
 
def fibonacci(numero:int):
    if numero <= 0:
        print("No se imprimen términos.")
    elif numero == 1:
        print(0)
    else:
        a = 0
        b = 1
        print(a)
        print(b)
        cont = 1
        while cont <= (numero - 2):
            siguiente = a + b
            print(siguiente)
            a = b
            b = siguiente
            cont += 1
 
def triangulo(numero:int):
    for i in range(1, numero + 1):
        for j in range(1, i+1):
            print(j,end=' ')
        print()

def carta():
    print("1. Numero primo:")
    print("2. Serie Fibonacci:")
    print("3. Triángulo de números:")
    print("4. Salir")
    opc = int(input("Seleccione una opción (1-4): "))
    return opc

