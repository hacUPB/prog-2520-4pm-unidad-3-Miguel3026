def simulacion_planeo():
    # Entradas del usuario
    altitud = float(input("Altitud inicial (m): "))
    v = float(input("Velocidad inicial (m/s): "))
    LD = float(input("Relación L/D: "))
    distancia_pista = float(input("Distancia a la pista (m): "))

    # Inicialización
    minuto = 0
    altitud_restante = altitud
    distancia_restante = distancia_pista

    print("\n--- Simulación de Planeo de Emergencia ---\n")

    # Bucle principal
    while altitud_restante > 0 and distancia_restante > 0:
        minuto += 1
        # Avance horizontal en 1 minuto
        avance = v * 60  # (m)
        # Pérdida de altitud
        perdida_altitud = avance / LD

        # Actualizar estado
        distancia_restante -= avance
        altitud_restante -= perdida_altitud

        print(f"Minuto {minuto}:")
        print(f"  Altitud restante: {altitud_restante:.1f} m")
        print(f"  Distancia a la pista: {distancia_restante:.1f} m\n")

        # Si ya llegó
        if distancia_restante <= 0 and altitud_restante >= 0:
            print("✅ Aterrizaje exitoso en la pista.")
            return
        if altitud_restante <= 0 and distancia_restante > 0:
            print("💥 Impacto en el terreno antes de llegar a la pista.")
            return

        # Decisión del usuario
        decision = input("¿Mantener (m) o aumentar (a) velocidad? ").lower()
        if decision == "a":
            v *= 1.2       # Aumentar velocidad un 20%
            LD *= 0.8      # Penalización: baja eficiencia

    # Salida final si se rompe el bucle
    if distancia_restante <= 0 and altitud_restante >= 0:
        print("✅ Aterrizaje exitoso en la pista.")
    else:
        print("💥 Impacto en el terreno antes de llegar a la pista.")

# Ejecutar simulación
simulacion_planeo()
