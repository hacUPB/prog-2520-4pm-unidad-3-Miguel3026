# Simulaciones aeronauticas


## Ejercicio 3: Consumo de combustible
## Enunciado
Un Airbus A320 inicia un vuelo con una cantidad determinada de combustible. El vuelo se divide en tres fases: ascenso, crucero y descenso, cada una con un consumo de combustible distinto.

- En la fase de ascenso, el consumo es de 75 Litros/min.

- En la fase de crucero, el consumo es de 50 Litros/min.

- En la fase de descenso, el consumo es de 37.5 Litros/min.

El usuario debe ingresar:

- La cantidad inicial de combustible disponible.

- La duración de cada fase en minutos.

Durante el vuelo, el sistema debe calcular cada 5 minutos el combustible restante y verificar:

- Si el combustible baja del nivel mínimo de seguridad 1500 litros, la aeronave debe declarar una emergencia y buscar un aeropuerto cercano.

- Si el combustible llega a cero, el avión se queda sin combustible en vuelo.

- Si se completan todas las fases y queda combustible suficiente, el vuelo termina con éxito.


# Tablas de variables

## Ejercicio 3: Consumo de combustible

#  Tabla de Variables

| Variable                       | Tipo de variable | Descripción                                                          |
|--------------------------------|------------------|----------------------------------------------------------------------|
| AVION                          | Constante        | Nombre del avión simulado (Airbus A320)                              |
| combustible_seguridad   | Constante        | Nivel mínimo de combustible de seguridad (1500 L)                    |
| combustible_inicial            | Entrada          | Cantidad de combustible inicial definida por el usuario (L)           |
| tiempo_ascenso                 | Entrada          | Duración de la fase de ascenso en minutos                            |
| tiempo_crucero                 | Entrada          | Duración de la fase de crucero en minutos                            |
| tiempo_descenso                | Entrada          | Duración de la fase de descenso en minutos                           |
| consumo_ascenso                | Constante        | Consumo de combustible en la fase de ascenso (75 L/min)              |
| consumo_crucero                | Constante        | Consumo de combustible en la fase de crucero (50 L/min)              |
| consumo_descenso               | Constante        | Consumo de combustible en la fase de descenso (37.5 L/min)           |
| INTERVALO                      | Constante        | Intervalo de cálculo del consumo de combustible (5 minutos)          |
| combustible_actual             | Estado           | Cantidad de combustible restante en cada instante del vuelo (L)       |
| minuto                         | Control          | Contador del tiempo transcurrido en cada fase                        |
| fase                           | Control          | Indica en qué fase del vuelo se encuentra la aeronave                 |
| mensaje_final                  | Salida           | Estado final del vuelo: éxito, emergencia o avión sin combustible     |







# Pseudocodigos

## Ejercicio 3
```
INICIO

Constante AVION = Airbus A320
Constante combustible_seguridad = 1500   
Constante consumo_ascenso = 75                  
Constante consumo_crucero = 50                 
Constante consumo_descenso = 37.5               
Constante INTERVALO = 5                        

Leer combustible_inicial    
Leer tiempo_ascenso         
Leer tiempo_crucero         
Leer tiempo_descenso        

combustible_actual = combustible_inicial
fase = "ascenso"

PARA cada fase en (ascenso, crucero y descenso) HACER
    SI fase = "ascenso" ENTONCES
        consumo = consumo_ascenso
        duracion = tiempo_ascenso
    SINO SI fase = "crucero" ENTONCES
        consumo = consumo_crucero
        duracion = tiempo_crucero
    SINO
        consumo = consumo_descenso
        duracion = tiempo_descenso
    FIN SI

    minuto = 0
    MIENTRAS minuto < duracion Y combustible_actual > 0 HACER
        Mostrar "Fase:", fase, " Minuto:", minuto, " Combustible:", combustible_actual, "L"
        
        combustible_actual = combustible_actual - (consumo * INTERVALO)

        SI combustible_actual <= combustible_seguridad ENTONCES
            Mostrar "ALERTA: Combustible crítico. Buscar aeropuerto cercano."
            mensaje_final = "Emergencia por bajo nivel de combustible"
            SALIR de todos los bucles
        FIN SI

        minuto = minuto + INTERVALO
    FIN MIENTRAS

    SI combustible_actual <= 0 ENTONCES
        mensaje_final = "El avión se quedó sin combustible en vuelo."
        SALIR de todos los bucles
    FIN SI
FIN PARA

SI combustible_actual > combustible_seguridad Y fase = "descenso" Y minuto >= duracion ENTONCES
    mensaje_final = "El avión completó el vuelo con éxito."
FIN SI

Mostrar: mensaje_final

FIN
```









