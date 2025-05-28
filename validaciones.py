def pedir_modo_valido() -> str:
    """
    Solicita al usuario que ingrese un modo de carga válido y lo retorna normalizado.

    Además, si el usuario ingresa "hardcodeado", la función lo convierte automáticamente 
    a "hard" para estandarizar la salida.

    Retorna:
        str: El modo de carga válido, que será "manual" o "hard".
    """
    modo = input("Ingrese modo de carga (manual/hardcodeado): ")

    while True:
        if modo == "manual" or modo == "hard" or modo == "hardcodeado":
            break
        else:
            print("Modo inválido. Use 'manual' o 'hardcodeado'.")
            modo = input("Ingrese modo de carga (manual/hardcodeado): ")

    if modo == "hardcodeado":
        modo = "hard"

    return modo

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
    valido = es_nombre_valido_ascii(nombre)
    while valido is False:
        print("Nombre inválido. No debe contener números y no puede estar vacío.")
        nombre = input("Ingrese el nombre: ")
        if es_nombre_valido_ascii(nombre):
            valido = True
        else:
            valido = False
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
    while True:
        if len(genero) == 1 and es_genero_valido_ascii(genero):
            break
        print("Género inválido. Debe ser M, F o X (mayúscula o minúscula).")
        genero = input("Género (M/F/X): ")
    return genero


def validar_legajo(entrada: str, legajos_actuales: list[int]) -> int:
    """
    Solicita repetidamente un legajo hasta que sea un número de 5 cifras no repetido.

    Argumentos:
        entrada (str): Entrada inicial del legajo.
        legajos_actuales: Lista de legajos ya utilizados para evitar repeticiones.

    Retorna:
        int: Legajo validado como entero.
    """
    while True:
        if es_numero_valido_ascii(entrada) and len(entrada) == 5:
            if int(entrada) not in legajos_actuales:
                break
            else:
                print("Legajo ya existe. Ingrese un legajo diferente.")
        else:
            print("Legajo inválido. Debe ser un número de 5 cifras.")
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
    while True:
        nota_str = input(f"Ingrese la nota de MATERIA_{numero_materia} para {nombre}: ")
        if es_numero_valido_ascii(nota_str) and 1 <= int(nota_str) <= 10:
            return int(nota_str)
        print("Nota inválida. Debe estar entre 1 y 10.")



def validar_materia(entrada: str) -> int:
    """
    Solicita y valida el número de materia hasta que esté entre 1 y 5.

    Argumentos:
        entrada: Entrada inicial del número de materia.

    Retorna:
        int: Número de materia validado.
    """
    es_valido = False

    while not es_valido:
        if es_numero_valido_ascii(entrada):
            numero = int(entrada)
            if numero >= 1 and numero <= 5:
                es_valido = True
            else:
                print("Número fuera de rango. Debe estar entre 1 y 5.")
                entrada = input("Ingrese el número de la materia (1 a 5): ")
        else:
            print("Entrada inválida. Solo se permiten números del 1 al 5.")
            entrada = input("Ingrese el número de la materia (1 a 5): ")

    return int(entrada)


def pedir_opcion_menu(entrada: str) -> int:
    """
    Solicita una opción del menú y valida que esté entre 1 y 8.

    Argumentos:
        entrada (str): Entrada inicial del usuario.

    Retorna:
        int: Opción validada entre 1 y 8.
    """
    while True:
        if es_numero_valido_ascii(entrada) and 1 <= int(entrada) <= 8:
            return int(entrada)
        print("Opción inválida. Ingrese un número del 1 al 8.")
        entrada = input("Ingrese la opción: ")