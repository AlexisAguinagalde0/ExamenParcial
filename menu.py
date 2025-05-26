from funciones import * 


def menu():
    datos_cargados = False

    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1) Cargar datos (manual o hardcodeado)")
        print("2) Mostrar todos los datos")
        print("3) Calcular promedios")
        print("4) Ordenar por promedio DESC")
        print("5) Mostrar materia/s con mayor promedio")
        print("6) Buscar estudiante por legajo")
        print("7) Salir")

        opcion = input("Seleccione una opción: ")
        print("\n")

        match opcion:
            case "1":
                modo = input("Ingrese modo de carga (manual/hardcodeado): ")
                resultado = generar_datos_estudiantes(modo)
                if resultado:
                    calificaciones, nombres, generos, legajos = resultado
                    datos_cargados = True
                    print("Datos cargados correctamente.")
            case "2":
                if datos_cargados:
                    mostrar_todos()
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case "3":
                if datos_cargados:
                    calcular_promedios()
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case "4":
                if datos_cargados:
                    calcular_promedios()
                    ordenar_por_promedio(descendente=False)
                    mostrar_todos()
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case "5":
                if datos_cargados:
                    materia_con_mayor_promedio()
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case "6":
                if datos_cargados:
                    buscar_por_legajo()
                else:
                    print("Primero debe cargar los datos (opción 1).")
            case "7":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción inválida. Ingrese un número del 1 al 7.")

menu()