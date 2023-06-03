# Lista donde se almacenan las filas y columnas y cada casilla es un valor booleano, dependiendo si hay una pieza en esa casilla o no.
casillas = []
casillas_disponibles = []
# Lista de las letras de las columnas con fin de asociar la letra a un índice
letras_columnas = ["A", "B", "C", "D", "E", "F", "G", "H"]
# Tablero inicializado en string
tablero_str = "\n    A    B    C    D    E    F    G    H"
opción = 0
while opción != 2:
    opción = int(input("¡Bienvenido a 8 Reinas!\n1.- Iniciar partida\n2.- Salir\nSu opción: "))
    if opción == 1:
        print('Puede digitar "TERMINAR" al ingresar una letra de columna para finalizar la partida')
        for i in range(8):
            casillas.append([])
            casillas_disponibles.append([])
            tablero_str += "\n" + str(i + 1) + " "
            for j in range(8):
                casillas[i].append(False)
                casillas_disponibles[i].append(False)
                tablero_str += " [  ]"
        print(tablero_str)
        while True:
            columna = input("Ingrese la letra de columna: ").strip().upper()
            if columna == "TERMINAR":
                break
            columna = columna[0]
            while not columna or (columna != "A" and columna != "B" and columna != "C" and columna != "D" and columna != "E" and columna != "F" and columna != "G" and columna != "H"):
                columna = input("Columna no válida. Intente nuevamente: ").strip().upper()
            print("Columna: " + columna)
            columna = int(letras_columnas.index(columna))

            fila = input("Ingrese el número de fila: ").strip()[0]
            while not fila.isdigit() or int(fila) < 1 or int(fila) > 8:
                fila = input("Fila no válida. Intente nuevamente: ").strip()[0]
            fila = int(fila) - 1
            casillas[fila][columna] = True
            for l in range(8):
                casillas_disponibles[fila][l] = True
                casillas_disponibles[l][columna] = True
                for k in range(8):
                    if l - k == fila - columna or l + k == fila + columna:
                        casillas_disponibles[l][k] = True

                
            print(casillas_disponibles)
            tablero_str = "\n    1    2    3    4    5    6    7    8"
            for m in range(8):
                tablero_str += "\n" + str(m + 1) + " "
                índice = 0
                for n in casillas[m]:
                    if n:
                        tablero_str += " [♕ ]"
                    elif casillas_disponibles[m][índice]:
                        tablero_str += " [ X]"
                    else:
                        tablero_str += " [  ]"
                    índice+=1
            print(tablero_str)
print("¡Gracias por participar!")
