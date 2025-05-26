
def es_numero_valido_ascii(cadena: str) -> bool:
    """
    Verifica si una cadena contiene únicamente caracteres numéricos (dígitos del 0 al 9) usando códigos ASCII.

    Argumetnos:
        cadena: Cadena a validar.

    Retorna:
        bool: True si la cadena es un número válido, False en caso contrario.
    """
    valido = True  
    if len(cadena) == 0:
        valido = False
    else:
        for caracter in cadena:
            codigo = ord(caracter)
            if codigo < 48 or codigo > 57:
                valido = False
                break  
    return valido

def es_nombre_valido_ascii(nombre: str) -> bool:
    """
    Valida que el nombre no esté vacío y no contenga números, utilizando valores ASCII.

    Argumentos:
        nombre (str): Nombre a verificar.

    Retorna:
        bool: True si el nombre es válido, False si contiene números o está vacío.
    """
    tiene_numero = False
    for c in nombre:
        ascii_val = ord(c)
        if 48 <= ascii_val <= 57:  
            tiene_numero = True
            break
    if len(nombre) == 0 or tiene_numero:
        valido = False
    else:
        valido = True
    return valido

def validar_nombre(nombre: str) -> str:
    """
    Solicita un nombre hasta que sea válido (no vacío y sin números).

    Argumentos:
        nombre (str): Nombre inicial ingresado por el usuario.

    Retorna:
        str: Nombre validado correctamente.
    """
    while not es_nombre_valido_ascii(nombre):
        print("Nombre inválido. No debe contener números y no puede estar vacío.")
        nombre = input("Ingrese el nombre: ")
    return nombre

def es_genero_valido_ascii(c: str) -> bool:
    """
    Verifica si el carácter representa un género válido: 'M', 'F' o 'X' (mayúscula o minúscula).

    Argumentos:
        c (str): Carácter a validar.

    Retorna:
        bool: True si es un género válido, False en caso contrario.
    """
    ascii_val = ord(c)
    if (ascii_val == 70 or ascii_val == 77 or ascii_val == 88 or
        ascii_val == 102 or ascii_val == 109 or ascii_val == 120):
        valido = True
    else:
        valido = False
    return valido

def validar_genero(genero: str) -> str:
    """
    Solicita hasta que el género que se ingrese sea un valor válido ('M', 'F' o 'X').

    Argumentos:
        genero (str): Género ingresado por el usuario.

    Retorna:
        str: Género validado.
    """
    while len(genero) != 1 or not es_genero_valido_ascii(genero):
        print("Género inválido. Debe ser M, F o X (mayúscula o minúscula).")
        genero = input("Género (M/F/X): ")
    return genero

def validar_legajo(entrada: str, legajos_actuales: list[int]) -> int:
    """
    Solicita repetidamente un legajo hasta que sea un número de 5 cifras no repetido.

    Argumentos:
        entrada (str): Entrada inicial del legajo.
        legajos_actuales (list[int]): Lista de legajos ya utilizados para evitar repeticiones.

    Retorna:
        int: Legajo validado como entero.
    """
    while not (es_numero_valido_ascii(entrada) and len(entrada) == 5) or int(entrada) in legajos_actuales:
        if not (es_numero_valido_ascii(entrada) and len(entrada) == 5):
            print("Legajo inválido. Debe ser un número de 5 cifras.")
        elif int(entrada) in legajos_actuales:
            print("Legajo ya existe. Ingrese un legajo diferente.")
        entrada = input("Legajo (5 cifras): ")
    return int(entrada)


def validar_nota(numero_materia: int, nombre: str) -> int:
    """
    Solicita y valida la nota de una materia para un estudiante específico. Debe estar entre 1 y 10.

    Argumentos:
        numero_materia (int): Número de la materia (índice o identificador).
        nombre (str): Nombre del estudiante al que se le está solicitando la nota.

    Retorna:
        int: Nota validada.
    """
    nota_str = input(f"Ingrese la nota de MATERIA_{numero_materia} para {nombre}: ")
    while not (es_numero_valido_ascii(nota_str) and 1 <= int(nota_str) <= 10):
        print("Nota inválida. Debe estar entre 1 y 10.")
        nota_str = input(f"Ingrese la nota de MATERIA_{numero_materia} para {nombre}: ")
    return int(nota_str)