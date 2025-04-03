# DESCRIPCION

Este proyecto es una aplicación de línea de comandos en Python para gestionar recetas de cocina. Permite agregar, modificar y buscar recetas utilizando almacenamiento en un archivo de texto (`Archivo.txt`).  

---

##  **Características**  

 Agregar nuevas recetas con proteína, acompañante y ensalada.  
 Modificar recetas existentes sin perder datos.  
 Buscar recetas por tipo de proteína.  
 Almacenar recetas en un archivo de texto para persistencia.  

---

##  **Estructura del Código**  

### 🏷 **1. Clase `Receta`**  

Esta clase representa una receta de cocina con los siguientes atributos:  

- `proteina` → Tipo de proteína del plato (Ej: Pollo, Pescado).  
- `acompanante` → Acompañamiento de la receta (Ej: Arroz, Puré).  
- `ensalada` → Ensalada incluida en el plato (Ej: César, Rusa).  

#### 🛠 **Métodos:**  

- `to_text()` → Convierte la receta en una cadena de texto (`"proteína|acompañante|ensalada"`).  
- `update(proteina, acompanante, ensalada)` → Modifica los valores de la receta.  
- `from_text(line)` *(método estático)* → Crea una receta a partir de una línea de texto del archivo.  

---

###  **2. Clase `Recetario`**  

Gestiona el conjunto de recetas y la interacción con el archivo `Archivo.txt`.  

#### 🛠 **Métodos:**  

- `load_recetas()` → Carga las recetas desde el archivo.  
- `save_recetas()` → Guarda todas las recetas en el archivo.  
- `agregar_receta(receta)` → Agrega una nueva receta y la guarda.  
- `modificar_receta(index, proteina, acompanante, ensalada)` → Modifica una receta existente.  
- `buscar_recetas_por_proteina(proteina)` → Busca recetas que contengan la proteína especificada.  

---

###  **3. Función `main()`**  

Muestra un menú interactivo para que el usuario pueda:  

1️ **Agregar una receta**  
2️ **Modificar una receta existente**  
3️ **Buscar recetas por proteína**  
4️ **Salir de la aplicación**  

---

##  **Cómo Ejecutarlo**  

1. Asegúrate de tener **Python 3** instalado.  
2. Guarda el código en un archivo `recetario.py`.  
3. Ejecuta el script en la terminal:  

   ```sh
   python recetario.py
