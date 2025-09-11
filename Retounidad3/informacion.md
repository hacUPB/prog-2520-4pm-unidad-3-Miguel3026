# Simulaciones aeronauticas


## Ejercicio 2: Planeo de emergencia sin motores
## Enunciado
Un avión pierde todos sus motores y entra en planeo. El objetivo es simular si logra llegar a la pista antes de quedarse sin altitud.
El programa calculará minuto a minuto el descenso del avión en función de la relación sustentación/arrastre (L/D). El usuario podrá decidir si mantiene la velocidad de planeo óptima o si la aumenta, lo cual le permitirá avanzar más rápido en horizontal pero perderá más altitud.
________________________________________
1. El usuario ingresa: altitud inicial, velocidad inicial, relación L/D y la distancia horizontal a la pista.

2.	El programa simula el planeo minuto a minuto.

3.	En cada minuto: 
	El avión avanza cierta distancia horizontal según la velocidad.
o	Pierde altitud según la relación L/D.
	Se muestran la altitud y distancia restantes.
o	El usuario decide: mantener o aumentar velocidad. 
	Si aumenta velocidad → avanza más pero pierde más altitud.

4.	La simulación termina cuando: 	El avión llega a la pista con altitud suficiente → Aterrizaje exitoso.
o	El avión se queda sin altitud antes de cubrir la distancia → Impacto en terreno.







# Tablas de variables

## Ejercicio 2: Planeo de emergencia sin motores

| Nombre de la variable   | Clasificación         | Descripción                                                                 |
| ----------------------- | --------------------- | --------------------------------------------------------------------------- |
| altitud_inicial         | Entrada               | Altitud inicial del avión al comenzar el planeo.                            |
| velocidad_inicial       | Entrada               | Velocidad inicial del avión.                                                |
| LD                      | Entrada               | Relación sustentación/arrastre (L/D).                                       |
| distancia_pista         | Entrada               | Distancia horizontal desde la posición actual a la pista.                   |
| vel_optima_planeo       | Entrada / Constante   | Velocidad de planeo óptima asociada al L/D.                                 |
| factor_aumento_vel      | Entrada / Parámetro   | Factor que multiplica la velocidad al “aumentar”.                           |
| accion_usuario          | Control               | Decisión del usuario en cada minuto.                                        |
| velocidad_actual        | Control / Estado      | Velocidad usada en el minuto actual, según decisión.                        |
| dt                      | Control / Constante   | Paso de tiempo de la simulación (ej: 1 min).                                |
| altitud_actual          | Estado / Salida parcial | Altitud del avión en cada instante.                                       |
| distancia_restante      | Estado / Salida parcial | Distancia que falta para llegar a la pista.                                |
| avance_horizontal       | Intermedia            | Distancia horizontal recorrida en cada minuto.                              |
| altitud_perdida         | Intermedia            | Altitud perdida en cada minuto según velocidad y L/D.                       |
| tiempo_transcurrido     | Intermedia            | Minutos acumulados en la simulación.                                        |
| resultado_simulacion    | Salida final          | Resultado final: “Aterrizaje exitoso” o “Impacto en terreno”.               |
| altitud_final           | Salida final          | Altitud del avión al final de la simulación.                                |
| distancia_final         | Salida final          | Distancia restante al final (0 si llegó a la pista).                        |
| tiempo_total            | Salida final          | Tiempo total hasta finalizar la simulación.                                 |









# Ecuaciones