def normalizar(lista, modo):
    if len(lista) == 0:
        print("Debe digitar algun elemento")
        return
    
    max = lista[0]
    min = lista[0]
    media = 0
    norma = 0
    desviacion = 0

    for i in lista:
        if i > max:
            max = i
        if i < min:
            min = i
        media += i/len(lista)
        norma += i**2
    
    for i in lista:
        desviacion += ((i-media)**2)/(len(lista))

    desviacion = desviacion**0.5
    norma = norma**0.5
    
    salida = []
    match modo:
        case "minmax":
          for i in lista:
               normal = (i-min)/(max-min)
               salida.append(normal)

        case "zscore":
            for i in lista:
                normal = (i-media)/desviacion
                salida.append(normal)

        case "unit":
            for i in lista:
                normal = i/norma
                salida.append(normal)

        case _:
            print("Modo no valido")
            return
    
    return salida

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
    if resultado != None:
        print("Lista normalizada:", resultado)

    salida = input("Desea seguir normalizando listas?(S/n): ").lower()
    if salida == "n":
        break