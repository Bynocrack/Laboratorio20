def agregar(lista):
    nombre = input("Digite el nombre: ")
    for e in lista:
        if (e["nombre"] == nombre):
            print("Ese nombre ya esta en el registro!")
            return lista
    while True:
        try:
            edad = int(input("Digite la edad: "))
            break
        except:
            print("Debe ser un entero!")

    while True:
        try:
            promedio = float(input("Digite el promedio: "))
            break
        except:
            print("Debe ser un numero real!")
    
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
    lista.append(estudiante)
    return lista

def mostrar(lista):
    if len(lista) == 0:
        print("No hay estudiantes!")
        return
    
    for e in lista:
        print("Nombre:", e["nombre"], "\nEdad:", e["edad"], "\nPromedio:", e["promedio"])
        print("========================================================================")

def promedio(lista):
    if len(lista) == 0:
        print("No hay estudiantes!")
        return
    
    mejor = lista[0]
    for e in lista:
        if (e["promedio"] > mejor["promedio"]):
            mejor = e
    
    print("Nombre:", mejor["nombre"], "\nEdad:", mejor["edad"], "\nPromedio:", mejor["promedio"])

def buscar(lista):
    nombre = input("Digite el nombre del estudiante a buscar: ")
    for e in lista:
        if (e["nombre"] == nombre):
            print("Nombre:", e["nombre"], "\nEdad:", e["edad"], "\nPromedio:", e["promedio"])
            return
    
    print("No se encontro el estudiante!")

def eliminar(lista):
    nombre = input("Digite el nombre del estudiante a eliminar: ")
    for e in lista:
        if (e["nombre"] == nombre):
            lista.remove(e)
            return lista
    
    print("No se encontro el estudiante!")

estudiantes = []
while True:
    print("\n1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Mostrar estudiante con mejor promedio")
    print("4. Buscar estudiante por nombre")
    print("5. Eliminar estudiante por nombre")
    print("0. Salir\n")
    while True:
        try:
            opcion = int(input("Digite su eleccion: "))
            break
        except:
            print("Debe ser entero!")
    
    match opcion:
        case 0:
            break
        case 1:
            estudiantes = agregar(estudiantes)
        case 2:
            mostrar(estudiantes)
        case 3:
            promedio(estudiantes)
        case 4:
            buscar(estudiantes)
        case 5:
            estudiantes = eliminar(estudiantes)