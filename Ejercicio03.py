while True:
    try:
        N = int(input("Ingrese un número N (≥ 3): "))
        if N >= 3:
            break
        else:
            print("El número debe ser mayor o igual a 3.")
    except ValueError:
        print("Debe ingresar un número entero válido.")
matriz = [[0] * N for _ in range(N)]
valor = 1
arriba, abajo = 0, N - 1
izquierda, derecha = 0, N - 1
while valor <= N*N:
    for col in range(izquierda, derecha + 1):
        matriz[arriba][col] = valor
        valor += 1
    arriba += 1
    for fila in range(arriba, abajo + 1):
        matriz[fila][derecha] = valor
        valor += 1
    derecha -= 1
    if arriba <= abajo:
        for col in range(derecha, izquierda - 1, -1):
            matriz[abajo][col] = valor
            valor += 1
        abajo -= 1
    if izquierda <= derecha:
        for fila in range(abajo, arriba - 1, -1):
            matriz[fila][izquierda] = valor
            valor += 1
        izquierda += 1
print("\nMatriz espiral:")
for fila in matriz:
    print(fila)
