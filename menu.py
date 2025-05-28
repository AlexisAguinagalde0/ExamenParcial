from funciones import * 

def menu(opciones: str) -> int:
    print(opciones)
    entrada = input("Ingrese la opción: ")
    opcion = pedir_opcion_menu(entrada)
    return opcion

texto_menu = """
--- MENÚ DE OPCIONES ---
1) Cargar datos (manual o hardcodeado)
2) Mostrar todos los datos
3) Calcular promedios
4) Ordenar por promedio DESC
5) Mostrar materia/s con mayor promedio
6) Buscar estudiante por legajo
7) Mostrar las repeticiones de una materia
8) Salir
"""

def ejecutar_menu():
    datos_cargados = False
    promedios_calculados = False

    while True:
        opcion = menu(texto_menu)
        print("\n")

        match opcion:
            case 1:
                modo = pedir_modo_valido()
                resultado = generar_datos_estudiantes(modo)
                if resultado != None:
                    calificaciones, nombres, generos, legajos = resultado
                    datos_cargados = True
                    promedios_calculados = False
                    print("Datos cargados correctamente.")
            case 2:
                if datos_cargados:
                    mostrar_todos()
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case 3:
                if datos_cargados:
                    calcular_promedios()
                    promedios_calculados = True
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case 4:
                if datos_cargados:
                    if promedios_calculados:
                        ordenar_por_promedio(descendente=False)
                        mostrar_todos()
                    else:
                        print("Primero se debe calcular los promedios (punto 3)")
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case 5:
                if datos_cargados:
                    materia_con_mayor_promedio()
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case 6:
                if datos_cargados:
                    buscar_por_legajo()
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case 7:
                if datos_cargados:
                    materia = input("Ingrese el número de la materia (1 a 5): ")
                    validacion = validar_materia(materia)
                    resultado = contar_calificaciones_por_materia(calificaciones, validacion)
                    for i in range(len(resultado)):
                        cantidad = resultado[i]
                        print(f"Nota {i+1}: {cantidad} veces")
                else: 
                    print("Primero debe cargar los datos (opción 1).")
            case 8:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción inválida. Ingrese un número del 1 al 8.")

if __name__ == "__main__":
    ejecutar_menu()