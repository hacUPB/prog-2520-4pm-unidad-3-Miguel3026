print("por favor ingrese su nombre: ")
nombre = input()
print("Bienvenido", nombre)

#Calcular el indice de Masa Corporal
#IMC = peso / estatura**2

#Leer estatura
estatura = input("ingrese su estatura en metros")
estatura = float(estatura)
#Leer peso
peso = input("Ingrese su peso en kilogramos")
peso = float(peso)
#Calcular IMC
IMC = peso / estatura**2
#Mostrar IMC
print("su IMC = ", IMC)
#Dado su IMC significa que:
if IMC < 18.49:
    print("peso bajo") 
else:
    if IMC < 24.99:
        print("peso normal")
    else:
        if IMC < 39.99:
            print("obesidad")
        else: 
            if IMC > 40:
                print("obesidad extrema")







