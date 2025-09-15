# Simulación de consumo de combustible de un Airbus A320 en vuelo

# Constantes
AVION = "Airbus A320"
COMBUSTIBLE_SEGURIDAD = 1500         # litros
CONSUMO_ASCENSO = 75                  # litros/min
CONSUMO_CRUCERO = 50                  # litros/min
CONSUMO_DESCENSO = 37.5               # litros/min
INTERVALO = 5                         # minutos

# Entradas del usuario
combustible_inicial = float(input("Ingrese el combustible inicial (LITROS): "))
tiempo_ascenso = int(input("Ingrese la duración del ascenso (minutos): "))
tiempo_crucero = int(input("Ingrese la duración del crucero (minutos): "))
tiempo_descenso = int(input("Ingrese la duración del descenso (minutos): "))

combustible_actual = combustible_inicial
mensaje_final = ""

# Secuencia de fases
for fase in ["ascenso", "crucero", "descenso"]:
    if fase == "ascenso":
        consumo = CONSUMO_ASCENSO
        duracion = tiempo_ascenso
    elif fase == "crucero":
        consumo = CONSUMO_CRUCERO
        duracion = tiempo_crucero
    else:
        consumo = CONSUMO_DESCENSO
        duracion = tiempo_descenso

    minuto = 0
    while minuto < duracion and combustible_actual > 0:
        print(f"Fase: {fase} | Minuto: {minuto} | Combustible: {combustible_actual:.2f} LITROS")

        # REDUCCIÓN de combustible
        combustible_actual -= (consumo * INTERVALO)

        # Verificar la emergencia
        if combustible_actual <= COMBUSTIBLE_SEGURIDAD:
            print("ALERTA: Combustible crítico. Buscar aeropuerto alterno.")
            mensaje_final = "Emergencia por bajo nivel de combustible"
            break

        minuto += INTERVALO
    
    if combustible_actual <= 0:
        mensaje_final = "El avión se quedó sin combustible en pleno vuelo."
        break

# Verificar si el vuelo terminó con éxito
if combustible_actual > COMBUSTIBLE_SEGURIDAD and mensaje_final == "":
    mensaje_final = "El avión completó el vuelo con éxito."

print("\nResultado final:", mensaje_final)
