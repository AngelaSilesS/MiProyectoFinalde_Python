import os             # Importamos el módulo os para trabajar con archivos y rutas.
from ClasePelicula import Pelicula          # Importamos la clase Pelicula desde el archivo ClasePelicula.py. 

class CatalogoPelicula:    # Definimos la clase CatalogoPelicula que gestiona una lista de películas y sus operaciones.

    def __init__(self, nombre, ruta_archivo):     # Constructor de la clase: inicializa el nombre del catálogo, la ruta del archivo y carga las películas existentes.
        self.nombre = nombre        # Nombre del catálogo.
        self.ruta_archivo = ruta_archivo    # Ruta del archivo donde se guardan las películas.
        self.peliculas = []               # Lista para almacenar objetos de tipo Pelicula.
        self.cargar_peliculas()    # Carga las películas desde el archivo al iniciar el catálogo.

    def agregar(self, pelicula):    # Método para agregar una película al catálogo.
     if self.buscar_pelicula(pelicula.id):    # Si ya existe una película con el mismo ID, no se agrega y retorna el siguiente mensaje.
        print(f"✕  Ya existe una película con el ID {pelicula.id}. No se puede agregar.")
        return
     self.peliculas.append(pelicula)       # Se agrega la película a la lista.
     self.guardar_datos()               # Se actualiza el archivo con los nuevos datos.
     print(f"Película con ID {pelicula.id} agregada correctamente.")  

    def listar(self):      # Método para listar todas las películas en el catálogo.
        if not self.peliculas:
            print("El catálogo está vacío.")     # Si la lista está vacía, se retorna el siguiente mensaje.
        else:
            for pelicula in self.peliculas:       # Se recorren las películas y se imprime.
                print(pelicula)

    def eliminar(self):  # Método para eliminar el catálogo de películas.
        self.peliculas = []  # Se vacía la lista.
        try:
            os.remove(self.ruta_archivo)        # Se intenta eliminar el archivo del catálogo e imprime el mensaje.
            print("Catálogo eliminado correctamente.")
        except FileNotFoundError:           # Pero si el archivo no existe muestra este otro mensaje.
            print("El archivo no existe.")

    def buscar_pelicula(self, id):       # Método para buscar una película por su ID.
        return next((p for p in self.peliculas if p.id == id), None)     # Retorna la película si existe, de lo contrario 'None'.

    def guardar_datos(self): 
        try:
            with open(self.ruta_archivo, 'w', encoding='utf-8') as f: 
                for pelicula in self.peliculas:
                    f.write(f"{pelicula.id},{pelicula.titulo},{pelicula.duracion},{pelicula.genero}\n")
        except Exception as e:
            print(f"✕  Error al guardar datos: {e}")

    def cargar_peliculas(self):
        if not os.path.exists(self.ruta_archivo):
            open(self.ruta_archivo, 'w', encoding='utf-8').close()      
            return
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as f:     
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        try:
                            id = int(datos[0])
                            titulo = datos[1]
                            duracion = int(datos[2])
                            genero = datos[3]
                            self.peliculas.append(Pelicula(id, titulo, duracion, genero))
                        except ValueError:
                            print(f"✕  Error en los datos: {linea.strip()}")
        except Exception as e:
            print(f"✕  Los datos no se pueden cargar: {e}")

def iniciar_programa():               
    archivo = input("Ingrese el nombre del catálogo de películas: ")
    if not archivo.endswith(".txt"):
        archivo += ".txt"

    if not os.path.exists(archivo):        
       print(f" →  El catálogo {archivo} no existía y ha sido creado.")
    else:
       print(f" →  El catálogo {archivo} ya existe.")

    catalogo = CatalogoPelicula("Mi Catálogo", archivo)
    menu(catalogo)

def menu(catalogo): 
    while True:
        print("\nMenú de opciones:")
        print("1 →  Agregar película.")
        print("2 →  Listar películas.")
        print("3 →  Eliminar catálogo de películas.")
        print("4 →  Salir.")
        opcion = input("Opción a elegir: ")

        if opcion == "1":
            try:
                print("\n  🔹 Por favor, ingrese:")
                id = int(input(" →  ID de la película: "))
                titulo = input(" →  Título de la película: ")
                duracion = int(input(" →  Duración (en min): "))
                genero = input(" →  Género: ")
                pelicula = Pelicula(id, titulo, duracion, genero)
                catalogo.agregar(pelicula)
            except ValueError:
                print("✕  Ingrese solo NÚMEROS para ID y la duración.")

        elif opcion == "2":
            print("\nListado del catálogo de películas:")
            catalogo.listar()

        elif opcion == "3":
            confirmar = input("¿Está seguro de eliminar el catálogo? → (S/N): ").strip().lower()
            if confirmar == "s":
                catalogo.eliminar()
            elif confirmar == "n":
                menu (catalogo)
            else:
                print("✕  Ingrese 's' o 'n' para validar la respuesta.")

        elif opcion == "4":
            print("\nEl programa finalizó. ¡Nos vemos pronto!😄")
            break
        else:
            print("✕  Incorrecto, agregue una opción entre 1 - 4.")

print("—" * 70)
print("      🎬      ¡Bienvenido a nuestro Catálogo de Películas!      🎥      ")
print("—" * 70)
iniciar_programa()