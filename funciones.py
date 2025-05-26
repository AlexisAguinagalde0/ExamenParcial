from datos import *
from validaciones import *

cantidad_estudiantes = 30
cantidad_materias = 5



def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    """
    Crea una matriz con un valor inicial definido en todas sus posiciones.

    Argumentos:
        cantidad_filas (int): Número de filas de la matriz.
        cantidad_columnas (int): Número de columnas de la matriz.
        valor_inicial (any): Valor con el que se inicializa cada celda de la matriz.

    Retorna:
        Matriz de tamaño cantidad_filas x cantidad_columnas con todos los elementos inicializados.    
    """
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        
        matriz += [fila]
    return matriz


def generar_datos_estudiantes(modo: str):
    """
    Genera los datos de los estudiantes (nombres, géneros, legajos y calificaciones) de forma manual o hardcodeada.

    Argumentos:
        modo (str): Modo de carga de datos. Puede ser "manual" o "hard"(hardcodead).

    Retorna:
        - matriz_calificaciones: Matriz de calificaciones de los estudiantes.
        - nombres: Lista de nombres de los estudiantes.
        - generos: Lista de géneros de los estudiantes.
        - legajos: Lista de legajos de los estudiantes.
    """
    nombres = [""] * cantidad_estudiantes
    generos = [""] * cantidad_estudiantes                       #Se generan las listas para los datos de los estudiantes
    legajos = [0] * cantidad_estudiantes
    matriz_calificaciones = inicializar_matriz(cantidad_estudiantes, cantidad_materias, 0)

    if modo == "manual":
        print("CARGA MANUAL DE DATOS")                              #Se separo la carga manual y hardcodeada de datos.
        for i in range(cantidad_estudiantes):                                                   
            print(f"\nEstudiante {i + 1}:")                                                     #Se recorre a cada estudiante de la cantidad de estudiantes dada para solicitar los datps                
            nombres[i] = validar_nombre(input("Nombre:"))           
            generos[i] = validar_genero(input("Género (M/F/X): "))                                      
            legajos[i] = validar_legajo(input("Legajo (5 cifras): "), legajos)                  #Se pide y valiad todos los datos de los estudiantes 
            for j in range(cantidad_materias):
                matriz_calificaciones[i][j] = validar_nota(j + 1, nombres[i])                   #Para cada materia se pide y valida la nota del estudiante

    elif modo == "hard":                                            #modo hardcodeado, ya con los datos ya definidos en el archivo datos.py                                                           
        contador_aux = 0
        
        for i in range(cantidad_estudiantes):
            nombres[i] = nombres_hardcodeados[i]                    #Se copian todos los datos ya definidos a las listas
            generos[i] = generos_hardcodeados[i]
            legajos[i] = legajos_hardcodeados[i]

            fila_base = calificaciones_base[contador_aux]
            for j in range(cantidad_materias):                     #Se asignan las calificaciones definidas a cada estudiante
                matriz_calificaciones[i][j] = fila_base[j]

            contador_aux += 1
            if contador_aux == len(calificaciones_base):           #Aumenta los indices hasta llegar al final de lista de calidicaciones base(si ya recorrio todos los indices) 
                contador_aux = 0
    else:
        print("Modo inválido. Use 'manual' o 'hardcodeado'.")
    return matriz_calificaciones, nombres, generos, legajos

calificaciones, nombres, generos, legajos = generar_datos_estudiantes("hard")   #llama a la funcion de generar datos estuidiantes modo hardcodeado y asigna cada dato del return a cada variable dada

promedios = [0] * len(nombres)                     #Se crea una lista para los promedios


def mostrar_un_estudiante(i):
    """
    Muestra por consola los datos de un estudiante específico (nombre, género, legajo y calificaciones).

    Argumento:
        i (int): Índice del estudiante a mostrar.

    Retorna:
        No retorna, imprmie por consola los datos del estudiante
    """
    
    print("NOMBRE\t\tGÉNERO\tLEGAJO\tCALIFICACIONES")

    if len(nombres[i]) < 8:
        print(f"{nombres[i]}\t\t{generos[i]}\t{legajos[i]}", end="\t")
    else:                                                                           #Se imprimen nombre, gnero y legajo alineado
        print(f"{nombres[i]}\t{generos[i]}\t{legajos[i]}", end="\t")        

    for j in range(len(calificaciones[i])):
        print(f"{calificaciones[i][j]}", end=" ")                                   #Se imprimern las calificaciones en una linea 
    
    print("\n" + "-" * 50)


def mostrar_todos():
    """
    Muestra por consola los datos de todos los estudiantes.

    Retorna:
        No retorna, imprime todos los datos de los estudiantes por consola
    """
    for i in range(len(nombres)):
        mostrar_un_estudiante(i)                             #Se utiliza la funcion anterior

def calcular_promedios():
    """
    Calcula el promedio de calificaciones de cada estudiante y los guarda en la lista llamada "promedios".

    Retorna:
        No retorna nada, guarda los promedios en la lista previamente generada llamada "promedios"
    """
    for i in range(cantidad_estudiantes):
        total = 0
        for j in range(cantidad_materias):                  #Se suma y se calcula el promedio 
            total += calificaciones[i][j]
        promedios[i] = total / cantidad_materias
    print("Promedios calculados.")
    



def ordenar_por_promedio(descendente=True):
    """
    Ordena las listas de datos de los estudiantes (nombre, género, legajo, calificaciones y promedios) según el promedio.

    Argumentos:
        descendente: Si es True, ordena de mayor a menor. Si es False, de menor a mayor.
    
    Retorna:
        No retorna, solo reordena segun criterio 
    """
    for i in range(cantidad_estudiantes - 1):                                 #Se comparan cada par de estudiantes 
        for j in range(i + 1, cantidad_estudiantes):                                
            if (promedios[i] < promedios[j] and descendente) or (promedios[i] > promedios[j] and not descendente):              #condicion para saber si hace el ord asc o desc
                promedios[i], promedios[j] = promedios[j], promedios[i]
                nombres[i], nombres[j] = nombres[j], nombres[i]
                generos[i], generos[j] = generos[j], generos[i]                          #hace swap de los datos de los dos estudiantes comparados
                legajos[i], legajos[j] = legajos[j], legajos[i]
                calificaciones[i], calificaciones[j] = calificaciones[j], calificaciones[i]
    print("Estudiantes ordenados.\n")




def materia_con_mayor_promedio():
    """
    Calcula el promedio de cada materia y muestra cuál o cuáles tienen el promedio más alto.

    Retorna:
        No retorna, imprime por pantalla la materia con el promedio mas alto encontrado
    """
    promedios_materias = [0] * cantidad_materias                #Se inicializa una lista para los promedios 

    for j in range(cantidad_materias):
        total = 0
        for i in range(cantidad_estudiantes):                   #Se calcula el promedio de cada materia sumando todas las notas y dividiendo por la cantidad de estudiantes 
            total += calificaciones[i][j]
        promedios_materias[j] = total / cantidad_estudiantes

    mayor_promedio = promedios_materias[0]
    for i in range(1, cantidad_materias):                       #Se busca el promedio mas alto entre las materias
        if promedios_materias[i] > mayor_promedio:
            mayor_promedio = promedios_materias[i]

    print("Materias con el mayor promedio general:")
    for i in range(cantidad_materias):
        if promedios_materias[i] == mayor_promedio:             #Se improme la materia que tiene el promedio mas alto encontrado
            print(f"MATERIA_{i + 1}: {promedios_materias[i]:.2f}")



def buscar_por_legajo():
    """
    Permite buscar a un estudiante ingresando su legajo. Si se encuentra, se muestra su información y promedio.

    Retorna:
        Imprime por consola el estudiante con su informacion y promedoi
    """
    if not promedios or promedios[0] == 0:                  #Revisa si los prmoedios estan calculados
        calcular_promedios()
        
    entrada = input("Ingrese el legajo del estudiante a buscar: ")
    while True:
        if es_numero_valido_ascii(entrada) and int(entrada) >= 10000:           #Se pide por input el legajo a buscar y se valida que sea un numero y qeu no sea menor a 10000
            break  
        print("Legajo inválido. Debe ser un número de al menos 5 dígitos.")
        entrada = input("Ingrese nuevamente el legajo: ")
    
    legajo_buscado = int(entrada)                   #cambia el legajo a entero
    encontrado = False                              #prepara una bandera en caso de que no se encuentre 
    
    for i in range(cantidad_estudiantes):
        if legajos[i] == legajo_buscado:
            mostrar_un_estudiante(i)                            #busca el legajo en la lista, muesta el estudiante y su promedio si el estudiante existe
            print(f"Promedio: {promedios[i]:.2f}")
            encontrado = True
            break

    if not encontrado:
        print("Estudiante no encontrado.")          #Si no se encuentra el estudiante, imprime por pantalla que no se encontro al estudiante con ese legajo