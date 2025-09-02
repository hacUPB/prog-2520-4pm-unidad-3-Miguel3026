
control = True
while control == True:
    print("1. Entradas\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salir")
    opcion = int(input("Elija una opcion: "))
    match opcion:
        case 1:
            print("1. Patacon con hogao")
            print("2. Yuca con chicharron")
            print("3. Guineo con suero")
            print()
        case 2:
            print("1. Solomito")
            print("2. Hamburguesa")
            print("3. Sushi")
            print()
        case 3:
            print("1. Limonada")
            print("2. Jugos naturales")
            print("3. Cerveza")
            print()
        case 4:
            print("1. Tres leches")
            print("2. Tiramusu")
            print("3. Sushi")
            print()
        case 5:
            control = False
        case _:
            print("Opcion no valida")
            print()