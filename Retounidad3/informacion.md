# Simulaciones aeronauticas

## Ejercicio 1: Estabilidad del avión en turbulencia
## Enunciado 
Un avión en vuelo se enfrenta a una turbulencia que dura 8 segundos.  
Durante este tiempo, el **piloto debe decidir en cada segundo** si aumentar, disminuir o mantener:  

- El **ángulo de ataque (AoA)**, que afecta el **coeficiente de sustentación (Cl)**.  
- La **velocidad del avión (V)**.  

El programa simula los efectos de estas decisiones sobre la sustentación y evalúa si el avión logra mantenerse en vuelo o entra en pérdida.  

El usuario no ingresa datos numéricos, sino que selecciona uno de tres aviones predefinidos **(Cessna 172, Airbus A320 o Boeing 747-8)**, cada uno con su peso, área alar, velocidad inicial, coeficiente de sustentación base y un ángulo de ataque inicial.

## Aviones predefinidos

| Avión               | Peso (N) | Área alar (m²) | Velocidad inicial (m/s) | Cl base | AoA inicial (°) |
|----------------------|----------|----------------|--------------------------|---------|-----------------|
| Cessna 172 Skyhawk  | 10,000   | 16.2           | 65                       | 0.4     | 5               |
| Airbus A320         | 600,000  | 122.6          | 130                      | 0.5     | 5               |
| Boeing 747-8        | 3,500,000| 554            | 250                      | 0.6     | 5               |

## Constantes utilizadas

- **Densidad del aire a nivel del mar:**  
  ρ = 1.225 kg/m³  

- **Relación simplificada entre Cl y AoA:**  
 Cl_actual = Cl_base + 0.1 x (AoA - AoA_inicial)

 ## Estados definidos

- **Estable:** Sustentación ≥ Peso.  
- **Crítico:** 0.5 × Peso ≤ Sustentación < 0.8 × Peso.  
- **Pérdida:** Sustentación < 0.5 × Peso → fin de simulación.  

## Bucle de simulación

- El ciclo se ejecuta por **8 segundos**.  
- En cada segundo:  
  1. Se muestra el **AoA actual** y el usuario decide aumentarlo, disminuirlo o mantenerlo.  
  2. Se recalcula el **Cl** y la **sustentación**.  
  3. Se muestra el **estado del vuelo** (Estable, Crítico o Pérdida).  
  4. Se muestra la **velocidad actual** y el usuario decide aumentarla, disminuirla o mantenerla.  

## Finalización del programa

- **Fracaso:** si ocurre pérdida antes de los 8 segundos.  
- **Éxito:** si se completan los 8 segundos sin pérdida.  

## Resultados posibles

- **Éxito:**  
  El avión logró atravesar la turbulencia con éxito.

- **Fracaso:**  
  El avión no logró superar la turbulencia.


  # Ejercicio 2: Planeo de emergencia sin motores
  ## Enunciado 
  Un avión sufre una falla total de motores durante el vuelo y debe planear hasta tocar el suelo.  
El desempeño del planeo depende de la relación de planeo (L/D), que indica cuántos metros avanza horizontalmente por cada metro que pierde en altitud.  

Durante la simulación, el piloto debe decidir en cada segundo si:  
- Aumentar el ángulo de picado → gana velocidad, pero la eficiencia (L/D) disminuye.  
- Disminuir el ángulo de picado → pierde velocidad, pero la eficiencia (L/D) mejora.  
- Mantener → conserva la eficiencia base.  

El objetivo es recorrer la mayor distancia horizontal posible antes de llegar al suelo.  

## Aviones predefinidos y duración del planeo

| Avión                | Altura inicial (m) | Pérdida por segundo (m) | Duración aprox. (s) | Relación L/D base |
|-----------------------|--------------------|--------------------------|----------------------|-------------------|
| Piper PA-28 Cherokee | 600                | 100                      | 6                    | 10:1              |
| Embraer E190         | 1200               | 150                      | 8                    | 14:1              |
| Concorde             | 2000               | 250                      | 8                    | 7:1               |

## Constantes utilizadas

- ρ = 1.225 kg/m³ (densidad del aire a nivel del mar, ISA).  
- Δh: pérdida de altura por segundo según el avión:  
  - Piper PA-28 Cherokee → 100 m/seg  
  - Embraer E190 → 150 m/seg  
  - Concorde → 250 m/seg  
- Relación L/D ajustada según decisión del piloto:  
  - Aumentar ángulo → L/D - 2  
  - Disminuir ángulo → L/D + 2  
  - Mantener → L/D sin cambios  
## Estados definidos

- En planeo: mientras h > 0 y L/D ≥ 5.  
- Crítico: si L/D < 5 (planeo ineficiente, riesgo de caída brusca).  
- Aterrizado: cuando h ≤ 0.  

## Bucle de simulación

1. El usuario selecciona un avión.  
2. Se asigna la altura inicial, el L/D base y la pérdida de altura por segundo (Δh).  
3. Se establece: segundo = 1, distancia = 0, estado = “planeo”.  
4. Mientras la altura sea mayor a 0:  
   - Mostrar la altura y la distancia recorrida.  
   - Preguntar al usuario si desea aumentar, disminuir o mantener el ángulo.  
   - Ajustar el valor de L/D según la decisión.  
   - Calcular la distancia horizontal de ese segundo y restar Δh de altura.  
   - Evaluar el estado (planeo normal, crítico o aterrizado).  
   - Incrementar el contador de segundos.  
5. El bucle termina cuando el avión llega al suelo. 

## Resultados posibles

- **Éxito completo:** el avión logra recorrer la máxima distancia posible según su L/D base.  
- **Éxito parcial:** el avión recorre una distancia considerable, aunque con decisiones subóptimas.  
- **Fracaso:** el avión baja demasiado el L/D (<5) y pierde eficiencia, aterrizando de forma crítica.


# Ejercicio 3: Consumo de combustible
## Enunciado
Un Airbus A320 inicia un vuelo con una cierta cantidad de combustible.  
El vuelo se divide en tres fases:  

1. **Ascenso** → consumo elevado: 75 litros/minuto.  
2. **Crucero** → consumo moderado: 50 litros/minuto.  
3. **Descenso** → consumo reducido: 37.5 litros/minuto.  

El usuario debe ingresar:  
- La cantidad inicial de combustible disponible.
- La duración de cada fase (ascenso, crucero y descenso) en minutos.  

Durante la simulación, el sistema calcula cada **5 minutos**:  
- El combustible restante.  
- Verifica si el vuelo entra en estado de normalidad, emergencia o falla.  
- Informa si el vuelo finaliza con éxito o en emergencia.  

## Objetivos del ejercicio
- Simular el consumo progresivo de combustible en las fases de vuelo.  
- Mostrar cómo las diferentes fases afectan directamente el gasto de combustible.  
- Destacar la importancia de mantener siempre la reserva mínima de seguridad (1500 L).  

## Estados posibles durante la simulación

- **Normal:** combustible > 1500 litros.  
- **Emergencia:** combustible ≤ 1500 litros (aunque no llegue a 0).  
- **Sin combustible:** combustible = 0 antes de completar todas las fases.  
- **Vuelo exitoso:** se completan todas las fases con combustible ≥ 1500 litros (reserva reglamentaria). 


# Tablas de variables

## Ejercicio 1: Estabilidad del avión en turbulencia

| Tipo       | Variable      | Descripción                                      | Tipo de dato |
|------------|---------------|--------------------------------------------------|--------------|
| Entrada    | avion         | Selección del avión (1, 2 o 3)                   | int          |
| Entrada    | aoa           | Ángulo de ataque actual (°)                      | int          |
| Entrada    | decision_aoa  | Decisión sobre el ángulo: aumentar, disminuir o mantener | str  |
| Entrada    | v             | Velocidad (m/s)                                  | float        |
| Entrada    | decision_v    | Decisión sobre la velocidad: aumentar, disminuir o mantener | str |
| Constante  | rho           | Densidad del aire (1.225 kg/m³)                  | float        |
| Constante  | cl_base       | Cl inicial del avión en el AoA base              | float        |
| Constante  | aoa_inicial   | Ángulo de ataque de referencia para Cl base      | int          |
| Salida     | cl_actual     | Coeficiente de sustentación ajustado por AoA     | float        |
| Salida     | sustentacion  | Sustentación (N) en cada segundo                 | float        |
| Salida     | estado        | Estado de vuelo (Estable, Crítico o Pérdida)     | str          |
| Control    | segundo       | Contador de tiempo (1 a 8)                       | int          |
| Control    | estado_final  | Resultado final de la simulación (Exitoso o Pérdida) | str      |


## Ejercicio 2: Planeo de emergencia sin motores

| Tipo       | Variable      | Descripción                                                   | Tipo de dato |
|------------|---------------|---------------------------------------------------------------|--------------|
| Entrada    | avion         | Selección del avión (1, 2 o 3)                                | int          |
| Entrada    | decision      | Elección del usuario: aumentar, disminuir o mantener ángulo   | str          |
| Constante  | rho           | Densidad del aire (1.225 kg/m³)                               | float        |
| Constante  | L_D_base      | Relación de planeo base del avión (L/D)                       | float        |
| Constante  | h_inicial     | Altura inicial asignada según el avión                        | float        |
| Constante  | delta_h       | Pérdida de altura por segundo (depende del avión)             | float        |
| Salida     | h_actual      | Altura restante en cada segundo (m)                           | float        |
| Salida     | distancia     | Distancia horizontal acumulada (m)                            | float        |
| Salida     | estado        | Estado del vuelo (En planeo, Crítico o Aterrizado)            | str          |
| Control    | segundo       | Contador de tiempo (segundos de simulación)                   | int          |







## Ejercicio 3: Consumo de combustible


| Tipo       | Variable          | Descripción                                                  | Tipo de dato |
|------------|------------------|--------------------------------------------------------------|--------------|
| Entrada    | combustible_ini  | Combustible inicial del avión (litros)                       | float        |
| Entrada    | t_ascenso        | Duración de la fase de ascenso (minutos)                     | int          |
| Entrada    | t_crucero        | Duración de la fase de crucero (minutos)                     | int          |
| Entrada    | t_descenso       | Duración de la fase de descenso (minutos)                    | int          |
| Constante  | consumo_ascenso  | 75 L/min                                                     | float        |
| Constante  | consumo_crucero  | 50 L/min                                                     | float        |
| Constante  | consumo_descenso | 37.5 L/min                                                   | float        |
| Constante  | intervalo        | Intervalo de reporte: cada 5 min                             | int          |
| Constante  | min_seguridad    | Nivel mínimo de seguridad: 1500 L                            | float        |
| Salida     | combustible_act  | Combustible restante después de cada intervalo               | float        |
| Salida     | estado           | Estado del vuelo (Normal, Emergencia, Sin combustible, Éxito)| str          |
| Control    | tiempo_total     | Suma de los minutos simulados                                | int          |
| Control    | fase             | Indica la fase actual (ascenso, crucero o descenso)          | str          |






# Ecuaciones 
## Ejericio 1:
## Ecuación principal
L = 0.5 x \rho x V^2 x Cl x A

Donde:  
- **L** = Sustentación (N)  
- **ρ** = Densidad del aire (kg/m³)  
- **V** = Velocidad (m/s)  
- **Cl** = Coeficiente de sustentación  
- **A** = Área alar (m²)  


## Ejercicio 2:
## Ecuaciones principales

1. Pérdida de altura por segundo:  
   Δh = valor definido por el avión  

2. Distancia horizontal recorrida por segundo:  
   Δx = (L/D) x Δh  

3. Actualización de altura y distancia:  
   h_nuevo = h_anterior - Δh  
   x_nuevo = x_anterior + Δx  

## Ejercicio 3:
## Ecuaciones principales

1. Combustible consumido en un intervalo de 5 minutos:  
   Δcombustible = consumo_fase × intervalo  

2. Combustible restante tras cada intervalo:  
   combustible_act = combustible_ant − Δcombustible  

3. Estado del vuelo:  
   - Si combustible_act = 0 → "Sin combustible"  
   - Si 0 < combustible_act ≤ 1500 → "Emergencia"  
   - Si combustible_act > 1500 → "Normal"  
 

# Pseudocodigos
## Ejercicio 1
```
Inicio

ρ = 1.225    // densidad del aire (kg/m³)

Definir aviones:
    1 → Cessna 172 Skyhawk: peso=10000, área=16.2, v=65, Cl_base=0.4, AoA_inicial=5
    2 → Airbus A320: peso=600000, área=122.6, v=130, Cl_base=0.5, AoA_inicial=5
    3 → Boeing 747-8: peso=3500000, área=554, v=250, Cl_base=0.6, AoA_inicial=5

Mostrar "Seleccione un avión:"
Leer opcion

Si opcion no está en {1,2,3} Entonces
    Mostrar "Opción inválida. Debe seleccionar 1, 2 o 3."
    Fin
Fin Si

peso = valor_peso_del_avion
área = valor_area_del_avion
v = valor_velocidad_inicial
Cl_base = valor_Cl_base
AoA_inicial = valor_AoA_inicial

AoA = AoA_inicial
estado_final = "Exitoso"

Para segundo desde 1 hasta 8 Hacer
    Mostrar "Segundo", segundo
    Mostrar "Ángulo de ataque actual =", AoA

    Mostrar "¿Ángulo de ataque: (a)umentar, (d)isminuir o (m)antener?"
    Leer decision_AoA

    Si decision_AoA = "a" Entonces
        AoA = AoA + 1
        Mostrar "Ángulo de ataque aumentó a", AoA
    Sino Si decision_AoA = "d" Entonces
        AoA = AoA - 1
        Mostrar "Ángulo de ataque disminuyó a", AoA
    Sino Si decision_AoA = "m" Entonces
        Mostrar "Ángulo de ataque se mantiene en", AoA
    Sino
        Mostrar "Opción inválida → se mantiene ángulo"
    Fin Si

    Cl_actual = Cl_base + 0.1 × (AoA - AoA_inicial)
    sustentación = 0.5 × ρ × v² × Cl_actual × área
    Mostrar "Velocidad =", v, "| Cl =", Cl_actual, "| Sustentación =", sustentación

    Si sustentación ≥ peso Entonces
        Mostrar "Estado: Estable"
    Sino Si sustentación < 0.5 × peso Entonces
        Mostrar "Estado: Pérdida - Fin de simulación"
        estado_final = "Pérdida"
        Salir del bucle
    Sino Si sustentación < 0.8 × peso Entonces
        Mostrar "Estado: Crítico"
    Fin Si

    Mostrar "Velocidad actual =", v
    Mostrar "¿Velocidad: (a)umentar, (d)isminuir, (m)antener?"
    Leer decision_v

    Si decision_v = "a" Entonces
        v = v + 10
        Mostrar "Velocidad aumentó a", v
    Sino Si decision_v = "d" Entonces
        v = v - 10
        Mostrar "Velocidad disminuyó a", v
    Sino Si decision_v = "m" Entonces
        Mostrar "Velocidad se mantiene en", v
    Sino
        Mostrar "Opción inválida → velocidad se mantiene"
    Fin Si

Fin Para

Si estado_final = "Exitoso" Entonces
    Mostrar "El avión logró atravesar la turbulencia con éxito."
Sino
    Mostrar "El avión no logró superar la turbulencia."
Fin Si

Fin
```

## Ejercicio 2

```
Inicio

Definir aviones:
    1 → Piper PA-28 Cherokee: h_inicial=600, L_D=10, delta_h=100
    2 → Embraer E190: h_inicial=1200, L_D=14, delta_h=150
    3 → Concorde: h_inicial=2000, L_D=7, delta_h=250

Mostrar "Seleccione un avión:"
Mostrar "1. Piper PA-28 Cherokee"
Mostrar "2. Embraer E190"
Mostrar "3. Concorde"
Leer opcion

Si opcion no está en {1,2,3} Entonces
    Mostrar "Opción inválida."
    Fin
Fin Si

h_actual = h_inicial del avión seleccionado
L_D = L_D del avión seleccionado
delta_h = delta_h del avión seleccionado
distancia = 0
segundo = 0
estado_final = "Exitoso"

Mostrar "Has seleccionado:", nombre del avión
Mostrar "Altura inicial =", h_actual, "Relación L/D base =", L_D, "Pérdida por segundo =", delta_h

Mientras h_actual > 0 Hacer
    segundo = segundo + 1
    Mostrar "Segundo", segundo
    Mostrar "Altura actual =", h_actual, "Distancia recorrida =", distancia
    Mostrar "Relación L/D actual =", L_D

    Mostrar "¿Ángulo de picado: (a)umentar, (d)isminuir o (m)antener?"
    Leer decision

    Si decision = "a" Entonces
        L_D = L_D - 2
        Mostrar "El ángulo aumentó → L/D disminuye a", L_D
    Sino Si decision = "d" Entonces
        L_D = L_D + 2
        Mostrar "El ángulo disminuyó → L/D aumenta a", L_D
    Sino Si decision = "m" Entonces
        Mostrar "El ángulo se mantiene → L/D =", L_D
    Sino
        Mostrar "Opción inválida → se mantiene el valor."
    Fin Si

    Si L_D < 5 Entonces
        Mostrar "Estado: Crítico, el avión perdió eficiencia de planeo."
        estado_final = "Fracaso"
        Salir del bucle
    Fin Si

    delta_x = L_D × delta_h
    h_actual = h_actual - delta_h
    Si h_actual < 0 Entonces
        h_actual = 0
    Fin Si
    distancia = distancia + delta_x

Fin Mientras

Mostrar "---- FIN DE SIMULACIÓN ----"
Mostrar "Tiempo total =", segundo
Mostrar "Distancia total recorrida =", distancia

Si estado_final = "Exitoso" Entonces
    Mostrar "El avión logró planear hasta el suelo con éxito."
Sino
    Mostrar "El avión no logró mantener un planeo eficiente y aterrizó de forma crítica."
Fin Si

Fin

```

## Ejercicio 3

```
Inicio

consumo_ascenso = 75
consumo_crucero = 50
consumo_descenso = 37.5
intervalo = 5
min_seguridad = 1500

Mostrar "=== EJERCICIO 3: CONSUMO DE COMBUSTIBLE ==="
Leer combustible_ini
Leer t_ascenso
Leer t_crucero
Leer t_descenso

combustible_act = combustible_ini
tiempo_total = 0
estado_final = "Exitoso"

Definir procedimiento simular_fase(nombre_fase, tiempo_fase, consumo_fase)
    Para minuto desde 0 hasta tiempo_fase con paso intervalo Hacer
        delta_combustible = consumo_fase * intervalo
        combustible_act = combustible_act - delta_combustible
        tiempo_total = tiempo_total + intervalo

        Si combustible_act <= 0 Entonces
            Mostrar "Minuto", tiempo_total, ": Sin combustible durante", nombre_fase, ". Vuelo fallido."
            estado_final = "Vuelo fallido"
            salida_combustible = combustible_act
            salida_tiempo = tiempo_total
            salida_estado = estado_final
            Salir del procedimiento
        Sino Si combustible_act <= min_seguridad Entonces
            Mostrar "Minuto", tiempo_total, ": Combustible", combustible_act, "litros → Emergencia en", nombre_fase
        Sino
            Mostrar "Minuto", tiempo_total, ": Combustible", combustible_act, "litros → Normal en", nombre_fase
        Fin Si
    Fin Para

    salida_combustible = combustible_act
    salida_tiempo = tiempo_total
    salida_estado = "Continuar"
Fin Procedimiento

simular_fase("ascenso", t_ascenso, consumo_ascenso)
combustible_act = salida_combustible
tiempo_total = salida_tiempo
estado = salida_estado
Si estado = "Vuelo fallido" Entonces
    Fin
Fin Si

simular_fase("crucero", t_crucero, consumo_crucero)
combustible_act = salida_combustible
tiempo_total = salida_tiempo
estado = salida_estado
Si estado = "Vuelo fallido" Entonces
    Fin
Fin Si

simular_fase("descenso", t_descenso, consumo_descenso)
combustible_act = salida_combustible
tiempo_total = salida_tiempo
estado = salida_estado
Si estado = "Vuelo fallido" Entonces
    Fin
Fin Si

Mostrar "---- FIN DEL VUELO ----"
Mostrar "Tiempo total:", tiempo_total, "minutos"
Mostrar "Combustible final:", combustible_act, "litros"

Si combustible_act >= min_seguridad Entonces
    Mostrar "Resultado: Vuelo exitoso. Aterrizaje con reserva suficiente."
Sino Si combustible_act > 0 Entonces
    Mostrar "Resultado: Vuelo completado en emergencia. Aterrizaje con menos de la reserva mínima."
Sino
    Mostrar "Resultado: Vuelo fallido. Sin combustible antes de aterrizar."
Fin Si

Fin
```




