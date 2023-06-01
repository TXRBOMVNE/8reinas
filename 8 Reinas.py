casillas: list[list[bool]] = []
letras_columnas = ["A", "B", "C", "D", "E", "F", "G", "H"]
tablero_str = "\n\n    A    B    C    D    E    F    G    H"

for i in range(8):
    casillas.append([])
    for j in range(8):
        casillas[i].append(False)
    tablero_str += "\n" + str(i + 1) + " "
    for m in casillas:
        tablero_str += " [  ]"

print(tablero_str)

while True:
    columna = input("Ingrese la letra de columna: ")
    if columna.strip():
        columna = columna[0].strip().upper()
        print("Columna: " + columna)
        columna = int(letras_columnas.index(columna))

    fila = input("Ingrese el número de fila: ")
    if fila.strip() and fila[0].isdigit():
        fila = int(fila[0].strip()) - 1

    if fila >= 0 and columna >= 0:
        casillas[fila][columna] = True

    tablero_str = "\n    A    B    C    D    E    F    G    H"
    for l in range(8):
        tablero_str += "\n" + str(l + 1) + " "
        for m in casillas[l]:
            if m:
                tablero_str += " [♕ ]"
            else:
                tablero_str += " [  ]"
    print(tablero_str)
