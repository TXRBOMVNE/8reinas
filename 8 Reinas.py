# Lista de las letras de las columnas con fin de asociar la letra a un índice numérico
letras_columnas = ["A", "B", "C", "D", "E", "F", "G", "H"]
# Tablero inicializado en string
tablero_str = ""


#  Pobla las listas de casillas con filas y sus valores correspondientes, al mismo tiempo que forma el tablero vacío para visualizarlo.
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
    print(tablero_str)


# Forma el tablero en un string y marca las casillas ocupadas por las piezas
def crear_tablero():
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
    print(tablero_str)


# Concluye la partida o en su defecto sólo el intento dependiendo de las condiciones de la partida
def concluir_intento():
    if cantidad_reinas == 8:
        input("¡Enhorabuena, encontraste una solución!" + tablero_str + "Presiona ENTER para continuar\n")
    elif cantidad_intentos == 0:
        input("¡Se te acabaron los intentos!. Este es tu resultado:" + tablero_str + "Cantidad de reinas posicionadas: " + str(cantidad_reinas) + "\nPresiona ENTER para continuar\n")
    elif cantidad_casillas_disponibles == 0:
        input(
            "¡Las reinas están amenazando todas las casillas y no encontraste una solución!. Este es tu resultado:"
            + tablero_str
            + "Cantidad de reinas posicionadas: "
            + str(cantidad_reinas)
            + "\nPresiona ENTER para continuar\n"
        )


opción = 0
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
        # Bucle que mantiene el ciclo de la partida
        while cantidad_reinas < 8 and cantidad_intentos > 0 and cantidad_casillas_disponibles > 0:
            columna_fila = input("Ingresa la columna y fila donde deseas la pieza (ej: A3): ")
            if columna_fila == "TERMINAR":
                break
            # Bucle que verifica que se hayan ingresado caracteres correspondientes a las filas y columnas
            while len(columna_fila) != 2 or columna_fila[0].upper() not in letras_columnas or not columna_fila[1].isdigit() or (int(columna_fila[1]) < 1 or int(columna_fila[1]) > 8):
                columna_fila = input("Ingresa una columna y fila válida: ")
            columna = letras_columnas.index(columna_fila[0].upper())
            fila = int(columna_fila[1]) - 1
            # Verifica si la casilla indicada por el usuario está ocupada
            if casillas[fila][columna]:
                print("La casilla indicada está ocupada por otra pieza.")
                continue
            # Verifica si la casilla indicada por el usuario está amenazada y resta 1 intento
            if casillas_disponibles[fila][columna]:
                cantidad_intentos -= 1
                if cantidad_intentos == 0:
                    print("La casilla indicada está amenazada por otra pieza y ya no quedan intentos.")
                    break
                elif cantidad_intentos == 1:
                    print("La casilla indicada está amenazada por otra pieza. Queda 1 intento.")
                else:
                    print("La casilla indicada está amenazada por otra pieza. Quedan " + str(cantidad_intentos) + " intentos.")
                continue
            # Si pasa todas las verificaciones, la casilla señalada se convierte a "True", lo que indica que es una casilla ocupada por una pieza.
            casillas[fila][columna] = True
            cantidad_reinas += 1

            # Bucle que marca cada casilla amenazada según el patrón de amenaza de las piezas.
            for l in range(8):
                if not casillas_disponibles[fila][l]:
                    casillas_disponibles[fila][l] = True
                    cantidad_casillas_disponibles -= 1
                if not casillas_disponibles[l][columna]:
                    casillas_disponibles[l][columna] = True
                    cantidad_casillas_disponibles -= 1
                for k in range(8):
                    if (l - k == fila - columna or l + k == fila + columna) and not casillas_disponibles[l][k]:
                        casillas_disponibles[l][k] = True
                        cantidad_casillas_disponibles -= 1
            crear_tablero()
            concluir_intento()
print("¡Gracias por participar!")
