#import random
form random import randint

´´´

variable de entrada
nombre           tipo
numero           int 

variable de salida
intentos         int    contador 

variable de control 
numero         int    
´´´

#num_aleatorio = random.randint(0, 50)
num_aleatorio = randint(1, 100)
intentos = 0
numero = -1

while numero != num_aleatorio:
    numero = int(input("Adivina el número (entre 1 y 100): "))
    intentos += 1
    if numero < num_aleatorio:
        print("El número es mayor")
    elif numero > num_aleatorio:
        print("El número es menor")
    else:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.") 