# Lista de las letras de las columnas con fin de asociar la letra a un índice
letras_columnas = ["A", "B", "C", "D", "E", "F", "G", "H"]
opción = 0
while opción != 2:
# Tablero inicializado en string
    tablero_str = "\n    A    B    C    D    E    F    G    H"
# Lista donde se almacenan las filas y columnas y cada casilla es un valor booleano, dependiendo si hay una pieza en esa casilla o no.
    casillas = []
    casillas_disponibles = []
    cantidad_casillas_disponibles = 64
    opción = int(input("¡Bienvenido a 8 Reinas!\n1.- Iniciar partida\n2.- Salir\nSu opción: " ))
    if opción == 1:
        print('Puede digitar "TERMINAR" al ingresar una letra de columna para finalizar la partida')
        cantidad_reinas = 0
        cantidad_intentos = 3
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
        while cantidad_reinas < 8 and cantidad_intentos > 0 and cantidad_casillas_disponibles > 0:
            columna = input("Ingrese la letra de columna: ").strip().upper()
            if columna == "TERMINAR":
                break
            if columna:
                columna = columna[0]
            while not columna or (columna != "A" and columna != "B" and columna != "C" and columna != "D" and columna != "E" and columna != "F" and columna != "G" and columna != "H"):
                columna = input("Columna no válida. Intente nuevamente: ").strip().upper()
            print("Columna: " + columna)
            columna = int(letras_columnas.index(columna))
            fila = input("Ingrese el número de fila: ").strip()
            if fila:
                fila = fila[0]
            while not fila or not fila.isdigit() or int(fila) < 1 or int(fila) > 8:
                fila = input("Fila no válida. Intente nuevamente: ").strip()[0]
            fila = int(fila) - 1
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
            casillas[fila][columna] = True
            cantidad_reinas += 1
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

            tablero_str = "\n    A    B    C    D    E    F    G    H"
            for m in range(8):
                tablero_str += "\n" + str(m + 1) + " "
                for n in range(8):
                    if casillas[m][n]:
                        tablero_str += " [♛ ]"
                    # elif casillas_disponibles[m][n]:
                    #     tablero_str += " [♙ ]"
                    else:
                        tablero_str += " [  ]"
                tablero_str += "  " + str(m + 1)
            tablero_str += "\n    A    B    C    D    E    F    G    H\n"
            print(tablero_str)
        if cantidad_reinas == 8:
            input("¡Enhorabuena, encontraste una solución!" + tablero_str + "Presiona ENTER para continuar\n")
        elif cantidad_intentos == 0:
            input("¡Se te acabaron los intentos!. Este es tu resultado:" + tablero_str + "Cantidad de reinas posicionadas: " + str(cantidad_reinas) + "\nPresiona ENTER para continuar\n")
        elif cantidad_casillas_disponibles == 0:
            input("¡Las reinas están amenazando todas las casillas y no encontraste una solución!. Este es tu resultado:" + tablero_str + "Cantidad de reinas posicionadas: " + str(cantidad_reinas) + "\nPresiona ENTER para continuar\n")
print("¡Gracias por participar!")
