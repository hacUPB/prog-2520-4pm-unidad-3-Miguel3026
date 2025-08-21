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




