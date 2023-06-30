import time

# Lista de las letras de las columnas con fin de asociar la letra a un índice numérico.
letras_columnas = ["A", "B", "C", "D", "E", "F", "G", "H"]
# Inicialización de las variables.
cantidad_casillas_disponibles = 64
cantidad_reinas = 0
cantidad_intentos = 3


# Pobla las listas de casillas con filas y sus valores correspondientes, al mismo tiempo que forma e imprime el tablero vacío.
def inicializar_tablero():
    tablero_str = "\n    A    B    C    D    E    F    G    H"
    for i in range(8):
        casillas.append([])
        casillas_disponibles.append([])
        tablero_str += "\n" + str(i + 1) + " "
        for j in range(8):
            casillas[i].append(False)
            casillas_disponibles[i].append(False)
            tablero_str += " [  ]"
        tablero_str += "  " + str(i + 1)
    tablero_str += "\n    A    B    C    D    E    F    G    H\n"
    # Imprimir interfaz del tablero de las 8 reinas.
    print(tablero_str)


# Forma el tablero en un string y marca las casillas ocupadas por las piezas.
def tablero():
    tablero_str = "\n    A    B    C    D    E    F    G    H"
    for m in range(8):
        tablero_str += "\n" + str(m + 1) + " "
        for n in range(8):
            if casillas[m][n]:
                tablero_str += " [♛ ]"
            # Las próximas dos líneas de código sirven para visualizar las casillas amenazadas en la partida, marcándolas con un peón.
            # elif casillas_disponibles[m][n]:
            #     tablero_str += " [♙ ]"
            else:
                tablero_str += " [  ]"
        tablero_str += "  " + str(m + 1)
    tablero_str += "\n    A    B    C    D    E    F    G    H\n"
    return tablero_str


# Verifica las condiciones de juego para concluir el intento y partida. En su defecto, no interfiere.
def concluir_intento(tiempo_inicio):
    tiempo_total = str(round((time.time() - tiempo_inicio) / 60, 2))
    # Respuesta en caso de dar con algunas de las soluciones existentes dentro de las 8 reinas.
    if cantidad_reinas == 8:
        input("\n¡Enhorabuena, encontraste una solución!\nTe demoraste " + tiempo_total + " minutos en completarlo. " + tablero() + "Presiona ENTER para continuar\n")
    # Respuesta en caso de fallar en todos los intentos posibles del programa.
    # Se muestra resultado del tablero, cantidad de reinas posicionadas y duración de la partida.
    elif cantidad_intentos == 0:
        input(
            "\n¡Se te acabaron los intentos!\n Este es tu resultado:"
            + tablero()
            + "Cantidad de reinas posicionadas: "
            + str(cantidad_reinas)
            + "\nTe demoraste "
            + tiempo_total
            + " minutos\nPresiona ENTER para continuar\n"
        )
    # Respuesta en caso de no presentarse más casillas disponibles en la partida del jugador.
    # Se muestra resultado del tablero, cantidad de reinas posicionadas y duración de la partida.
    elif cantidad_casillas_disponibles == 0:
        input(
            "\n¡Las reinas están amenazando todas las casillas y no encontraste una solución!. Este es tu resultado:"
            + tablero()
            + "Cantidad de reinas posicionadas: "
            + str(cantidad_reinas)
            + "Te demoraste "
            + tiempo_total
            + " minutos.\nPresiona ENTER para continuar\n"
        )


opción = 0
# Bucle que da introducción al menú de opciones otorgadas por el programa.
while opción != 2:
    opción = int(input("¡Bienvenido a 8 Reinas!\n1.- Iniciar partida\n2.- Salir\nOpción: "))
    if opción == 1:
        # Lista donde se almacenan las filas y columnas y cada casilla es un valor booleano, dependiendo si hay una pieza en esa casilla o no.
        casillas = []
        # Lista donde se almacenan las filas y columnas amenazadas y cada casilla es un valor booleano, dependiendo si está amenazada.
        casillas_disponibles = []
        # Cantidad de casillas no amenazadas ni ocupadas por piezas. Se le resta 1 cada vez que se marca una casilla no disponible en la lista previa.
        cantidad_casillas_disponibles = 64
        print('Puedes digitar "TERMINAR" para finalizar la partida')
        cantidad_reinas = 0
        cantidad_intentos = 3
        inicializar_tablero()
        tiempo_inicio = time.time()
        print("Tienes 3 intentos para completarlo. ¡Mucha suerte!")
        # Bucle que mantiene el ciclo de la partida, verificando que queden intentos, no se haya completado la partida y que queden casillas disponibles.
        while cantidad_reinas < 8 and cantidad_intentos > 0 and cantidad_casillas_disponibles > 0:
            columna_fila = input("Ingresa la columna y fila donde deseas la pieza (ej: A3): ")
            # Cierre del programa en caso de ingresar "TERMINAR".
            if columna_fila == "TERMINAR":
                break

            # Bucle que verifica que se hayan ingresado caracteres correspondientes a una fila y columna.
            while len(columna_fila) != 2 or columna_fila[0].upper() not in letras_columnas or not columna_fila[1].isdigit() or (int(columna_fila[1]) < 1 or int(columna_fila[1]) > 8):
                columna_fila = input("Ingresa una columna y fila válida: ")

            # Convierte la columna a un número, para después utilizarlo como índice en una lista.
            columna = letras_columnas.index(columna_fila[0].upper())

            # Se debe restar 1 debido a que el usuario tiene permitido ingresar un número desde el 1 al 8, pero los índices de las listas inician desde 0.
            fila = int(columna_fila[1]) - 1

            # Verifica si la casilla indicada por el usuario está ocupada.
            if casillas[fila][columna]:
                print("La casilla indicada está ocupada por otra pieza.")
                continue

            # Verifica si la casilla indicada por el usuario está amenazada y resta 1 intento. En el caso de que no queden intentos, se concluye la partida.
            if casillas_disponibles[fila][columna]:
                cantidad_intentos -= 1
                # Respuesta en caso de intentar colocar una pieza en una casilla amenazada por otra pieza y término de la partida mostrando tiempo de juego y tablero realizado.
                if cantidad_intentos == 0:
                    print("La casilla indicada está amenazada por otra pieza y ya no quedan intentos.")
                    concluir_intento(tiempo_inicio)
                    break
                # Aviso de 1 intento restante.
                elif cantidad_intentos == 1:
                    print("La casilla indicada está amenazada por otra pieza. Queda 1 intento.")
                    concluir_intento(tiempo_inicio)
                else:
                    # Aviso de n intentos restantes mayor a 1.
                    print("La casilla indicada está amenazada por otra pieza. Quedan " + str(cantidad_intentos) + " intentos.")
                    concluir_intento(tiempo_inicio)
                continue

            # Si pasa todas las verificaciones, la casilla señalada se convierte a "True", lo que indica que esa casilla está ocupada.
            casillas[fila][columna] = True
            cantidad_reinas += 1

            # Bucle que marca cada casilla (columna, fila y ambas diagonales) como amenazada en función de la pieza.
            for l in range(8):
                # Si la casilla de la fila presente no está ocupada, se le marca como amenazada y se resta una casilla disponible.
                if not casillas_disponibles[fila][l]:
                    casillas_disponibles[fila][l] = True
                    cantidad_casillas_disponibles -= 1

                # Si la casilla de la columna presente no está ocupada, se le marca como amenazada y se resta una casilla disponible.
                if not casillas_disponibles[l][columna]:
                    casillas_disponibles[l][columna] = True
                    cantidad_casillas_disponibles -= 1

                # Bucle que marca las diagonales como amenazadas.
                for k in range(8):
                    # Si la suma o resta de los índices de los bucles coincide con la suma o resta del N° de columna y fila y no está ocupada, se le marca como amenazada y se resta una casilla disponible
                    # La resta marca la diagonal principal y la suma marca la diagonal inversa.
                    if (l - k == fila - columna or l + k == fila + columna) and not casillas_disponibles[l][k]:
                        casillas_disponibles[l][k] = True
                        cantidad_casillas_disponibles -= 1
            # Cierre del programa según resultados acciones realizadas por el jugador.
            print(tablero())
            concluir_intento(tiempo_inicio)
# Mensaje de cierre del programa.
print("¡Gracias por participar!")
