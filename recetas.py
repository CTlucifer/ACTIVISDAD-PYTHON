
import os

# Clase que representa una receta.
class Receta:
    def __init__(self, proteina, acompanante, ensalada):
        self.proteina = proteina
        self.acompanante = acompanante
        self.ensalada = ensalada

    # Convierte la receta a una cadena de texto con el formato "proteína|acompañante|ensalada"
    def to_text(self):
        return f"{self.proteina}|{self.acompanante}|{self.ensalada}"

    # Actualiza los datos de la receta. Si algún campo es None, se conserva el valor actual.
    def update(self, proteina=None, acompanante=None, ensalada=None):
        if proteina is not None:
            self.proteina = proteina
        if acompanante is not None:
            self.acompanante = acompanante
        if ensalada is not None:
            self.ensalada = ensalada

    # Método estático para crear una receta a partir de una línea de texto.
    @staticmethod
    def from_text(line):
        partes = line.strip().split("|")
        if len(partes) == 3:
            return Receta(partes[0], partes[1], partes[2])
        else:
            return None

# Clase que maneja el conjunto de recetas y las operaciones de guardado y lectura en el archivo .txt.
class Recetario:
    def __init__(self, filename="Archivo.txt"):
        self.filename = filename
        self.recetas = []
        self.load_recetas()

    # Carga las recetas desde el archivo de texto.
    def load_recetas(self):
        self.recetas = []
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    for line in file:
                        receta = Receta.from_text(line)
                        if receta:
                            self.recetas.append(receta)
            except Exception as e:
                print(f"Error al leer el archivo: {e}")

    # Guarda todas las recetas en el archivo de texto sobrescribiendo su contenido.
    def save_recetas(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                for receta in self.recetas:
                    file.write(receta.to_text() + "\n")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    # Agrega una nueva receta y actualiza el archivo.
    def agregar_receta(self, receta):
        self.recetas.append(receta)
        self.save_recetas()

    # Modifica una receta existente dado su índice.
    def modificar_receta(self, index, proteina=None, acompanante=None, ensalada=None):
        if 0 <= index < len(self.recetas):
            self.recetas[index].update(proteina, acompanante, ensalada)
            self.save_recetas()
        else:
            print("Índice de receta inválido.")

    # Busca recetas que tengan como proteína el valor indicado (sin distinguir mayúsculas/minúsculas).
    def buscar_recetas_por_proteina(self, proteina):
        resultado = []
        for idx, receta in enumerate(self.recetas):
            if receta.proteina.lower() == proteina.lower():
                resultado.append((idx, receta))
        return resultado

# Función principal que ejecuta el menú de la aplicación.
def main():
    recetario = Recetario()
    while True:
        print("\n---- Menú de Recetas ----")
        print("1. Agregar receta")
        print("2. Modificar receta")
        print("3. Buscar recetas por proteína")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Solicitar datos para crear una nueva receta.
            proteina = input("Ingrese la proteína: ")
            acompanante = input("Ingrese el acompañante: ")
            ensalada = input("Ingrese la ensalada: ")
            receta = Receta(proteina, acompanante, ensalada)
            recetario.agregar_receta(receta)
            print("Receta agregada exitosamente.")

        elif opcion == "2":
            # Mostrar todas las recetas con su índice para elegir cuál modificar.
            if recetario.recetas:
                print("\nListado de recetas:")
                for idx, receta in enumerate(recetario.recetas):
                    print(f"{idx}. {receta.to_text()}")
                try:
                    indice = int(input("Ingrese el índice de la receta a modificar: "))
                except ValueError:
                    print("El índice debe ser un número entero.")
                    continue
                # Solicitar nuevos datos; si se deja en blanco se conserva el valor actual.
                print("Ingrese nuevos datos (deje en blanco para mantener el valor actual):")
                nueva_proteina = input("Nueva proteína: ")
                nuevo_acompanante = input("Nuevo acompañante: ")
                nueva_ensalada = input("Nueva ensalada: ")
                recetario.modificar_receta(
                    indice,
                    proteina=nueva_proteina if nueva_proteina.strip() != "" else None,
                    acompanante=nuevo_acompanante if nuevo_acompanante.strip() != "" else None,
                    ensalada=nueva_ensalada if nueva_ensalada.strip() != "" else None
                )
                print("Receta modificada exitosamente.")
            else:
                print("No hay recetas para modificar.")

        elif opcion == "3":
            # Buscar recetas por proteína.
            proteina_buscar = input("Ingrese la proteína a buscar: ")
            resultados = recetario.buscar_recetas_por_proteina(proteina_buscar)
            if resultados:
                print(f"\nRecetas con proteína '{proteina_buscar}':")
                for num, (indice, receta) in enumerate(resultados, 1):
                    print(f"{num}- {receta.to_text()}")
            else:
                print("No se encontraron recetas con esa proteína.")

        elif opcion == "4":
            print("Saliendo del menú.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
