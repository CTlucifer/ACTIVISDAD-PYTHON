class Tarea:
    """Clase que representa una tarea con una descripción."""
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

class GestorTareas:
    """Clase que gestiona la lista de tareas almacenadas en un archivo."""
    ARCHIVO_TAREAS = "tareas.txt"  # Nombre del archivo donde se guardan las tareas

    def __init__(self):
        self.tareas = self.cargar_tareas()

    def cargar_tareas(self):
        """Carga las tareas desde el archivo. Si el archivo no existe, retorna una lista vacía."""
        try:
            with open(self.ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
                return [Tarea(linea.strip()) for linea in archivo.readlines()]
        except FileNotFoundError:
            return []  # Retorna una lista vacía si el archivo no existe
        except Exception as e:
            print(f"Error al cargar las tareas: {e}")
            return []

    def guardar_tareas(self):
        """Guarda las tareas en el archivo."""
        try:
            with open(self.ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
                for tarea in self.tareas:
                    archivo.write(f"{tarea}\n")
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")

    def agregar_tarea(self, descripcion):
        """Agrega una nueva tarea a la lista y la guarda en el archivo."""
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        self.guardar_tareas()
        print("Tarea agregada con éxito.")

    def mostrar_tareas(self):
        """Muestra todas las tareas almacenadas en la lista."""
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            print("Lista de tareas:")
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")

    def completar_tarea(self, numero):
        """Marca una tarea como completada eliminándola de la lista y del archivo."""
        if 1 <= numero <= len(self.tareas):
            self.tareas.pop(numero - 1)
            self.guardar_tareas()
            print("Tarea completada y eliminada.")
        else:
            print("Número de tarea inválido.")

def menu():
    """Muestra el menú principal del programa y gestiona las opciones del usuario."""
    gestor = GestorTareas()
    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            gestor.agregar_tarea(descripcion)
        elif opcion == "2":
            gestor.mostrar_tareas()
        elif opcion == "3":
            gestor.mostrar_tareas()
            try:
                numero = int(input("Ingrese el número de la tarea a completar: "))
                gestor.completar_tarea(numero)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
