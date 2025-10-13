´´´
1
12
123
1234
12345

i                      j
1  hasta n            1 hasta 1
2  hasta n            1 hasta 2
3  hasta n            1 hasta 3
4  hasta n            1 hasta 4
5  hasta n            1 hasta 5

´´´
numero = int(input("Introduce un número entero positivo:"))

for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print(i,end="")
    print()