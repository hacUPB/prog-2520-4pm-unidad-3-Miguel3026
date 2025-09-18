#import modulo
from modulo import *
 
#Función principal
def main():
    while True:
        variable = carta()
        match variable:
            case 1:
                print("Calcula si un número es primo.")
                numero = int(input("Ingrese un número entero mayor que 1: "))
                primo(numero)
            case 2:
                print("Imprime un número de términos de la serie de Fibonacci.")
                numero = int(input("Ingrese el número de términos: "))
                fibonacci(numero)
            case 3:
                print("Imprime un triángulo de números.")
                numero = int(input("Ingrese el número entero positivo: "))
                triangulo(numero)
            case 4:
                break
            case _:
                print("Esta opción no es válida")
 
# Verifica si existe una función llamada main()
if __name__ == "__main__":
    main()