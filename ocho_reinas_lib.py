from time import time


# Forma el tablero en un string y marca las casillas ocupadas por las piezas.
def tablero(casillas, casillas_disponibles):
    # Se establecen las letras de las columnas superiores
    tablero_str = "\n    A    B    C    D    E    F    G    H"

    # Bucle que se itera según la cantidad de columnas y filas del tablero.
    for m in range(8):
        # Se establece el número de línea actual en el tablero.
        tablero_str += "\n" + str(m + 1) + " "

        for n in range(8):
            # Si la casilla está marcada como ocupada, concatena una casilla con una reina.
            if casillas[m][n]:
                tablero_str += " [♛ ]"
            # Las próximas dos líneas de código sirven para visualizar las casillas amenazadas en la partida, marcándolas con un peón.
            # elif casillas_disponibles[m][n]:
            #     tablero_str += " [♙ ]"

            # En su defecto, concatena una casilla vacía
            else:
                tablero_str += " [  ]"

        # Se establece el número de línea actual en el tablero.
        tablero_str += "  " + str(m + 1)

    # Se establecen las letras de las columnas inferiores
    tablero_str += "\n    A    B    C    D    E    F    G    H\n"
    return tablero_str


# Verifica las condiciones de juego para concluir el intento y partida. En su defecto, no interfiere.
def concluir_intento(tiempo_inicio, casillas, casillas_disponibles, cantidad_reinas, cantidad_intentos, cantidad_casillas_disponibles):
    # Resta el tiempo de inicio de la partida con el actual para determinar la duración de la misma. Se divide en 60 para establecer el tiempo en minutos y se redondea a dos decimales.
    tiempo_total = time() - tiempo_inicio

    # Se divide en 60 para equivalarlo a minutos
    minutos = int(tiempo_total / 60)

    # Los decimales se multiplican por 60 para equivalerlos a segundos
    segundos = int(round(((tiempo_total / 60) - minutos) * 60, 0))

    # Respuesta en caso de dar con algunas de las soluciones existentes.
    if cantidad_reinas == 8:
        input(
            "\n¡Enhorabuena, encontraste una solución!\nTe demoraste "
            + str(minutos)
            + " minutos y "
            + str(segundos)
            + " segundos en completarlo."
            + tablero(casillas, casillas_disponibles)
            + "Presiona ENTER para continuar\n"
        )

    # Respuesta en caso de fallar en todos los intentos posibles de la partida.
    # Se muestra resultado del tablero, cantidad de reinas posicionadas y duración de la partida.
    elif cantidad_intentos == 0:
        input(
            "\n¡Se te acabaron los intentos!\n Este es tu resultado:"
            + tablero(casillas, casillas_disponibles)
            + "Cantidad de reinas posicionadas: "
            + str(cantidad_reinas)
            + "\nTe demoraste "
            + str(minutos)
            + " minutos y "
            + str(segundos)
            + " segundos.\nPresiona ENTER para continuar\n"
        )

    # Respuesta en caso de no presentarse más casillas disponibles en la partida.
    # Se muestra resultado del tablero, cantidad de reinas posicionadas y duración de la partida.
    elif cantidad_casillas_disponibles == 0:
        input(
            "\n¡Las reinas están amenazando todas las casillas y no encontraste una solución!. Este es tu resultado:"
            + tablero(casillas, casillas_disponibles)
            + "Cantidad de reinas posicionadas: "
            + str(cantidad_reinas)
            + "\nTe demoraste "
            + str(minutos)
            + " minutos y "
            + str(segundos)
            + " segundos.\nPresiona ENTER para continuar\n"
        )
