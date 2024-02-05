tareas = []

def agregarTarea(descripcion):
    tarea = {"descripcion": descripcion, "completada": False}
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' añadida.")

def eliminarTarea(indice):
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada.")
    else:
        print("Índice de tarea no válido.")

def mostrarTareas():
    if not tareas:
        print("No hay tareas.")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas):
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - {estado}")

def marcarCompletada(indice):
    if 0 <= indice < len(tareas):
        tareas[indice]['completada'] = True
        print(f"Tarea '{tareas[indice]['descripcion']}' marcada como completada.")
    else:
        print("Id de tarea no válido.")

def main():
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar Tarea")
        print("2. Eliminar Tarea")
        print("3. Mostrar Tareas")
        print("4. Marcar como Completada")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregarTarea(descripcion)
        elif opcion == "2":
            indice = int(input("Ingrese el ID de la tarea a eliminar: "))
            eliminarTarea(indice - 1)
        elif opcion == "3":
            mostrarTareas()
        elif opcion == "4":
            indice = int(input("Ingrese el Id de la tarea a marcar como completada: "))
            marcarCompletada(indice - 1)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
