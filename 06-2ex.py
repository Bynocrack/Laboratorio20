import numpy as np

def normalizar(lista, modo):
    lista = np.array(lista)
    if len(lista) == 0:
        print("Debe digitar algun elemento")
        return
    
    match modo:
        case "minmax":
          return (lista - lista.min()) / (lista.max() - lista.min())

        case "zscore":
            return (lista - lista.min() / lista.std())

        case "unit":
            return lista / np.linalg.norm(lista)

        case _:
            print("Modo no valido")
            return

while True:
    lista = []
    while True:
        num = float(input("Digite un numero para agregar a la lista: "))
        lista.append(num)

        salida = input("Desea seguir agregando numeros?(S/n): ").lower()
        if salida == "n":
            break
    
    modo = input("Digite el modo de normalizacion: ")
    resultado = normalizar(lista, modo)
    if resultado is not None:
        print("Lista normalizada:", resultado)

    salida = input("Desea seguir normalizando listas?(S/n): ").lower()
    if salida == "n":
        break