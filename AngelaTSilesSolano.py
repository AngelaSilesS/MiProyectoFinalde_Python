
import os             # Importamos el módulo os para que nos elimine un archivo, en este caso el archivo 'txt'.
from ClasePelicula import Pelicula          # Importamos la clase Pelicula desde el archivo ClasePelicula.py. 

class CatalogoPelicula:    # Definimos la clase CatalogoPelicula que gestiona una lista de películas y sus operaciones.

    def __init__(self, nombre, ruta_archivo):     # Constructor de la clase: inicializa el nombre del catálogo, la ruta del archivo y carga las películas existentes.
        self.nombre = nombre        # Nombre del catálogo.
        self.ruta_archivo = ruta_archivo    # Ruta del archivo donde se guardan las películas ('txt').
        self.peliculas = []               # Lista para almacenar objetos de Pelicula.
        self.cargar_peliculas()    # Carga las películas desde el archivo al iniciar el catálogo.

    def agregar(self, pelicula):    # Método para agregar una película al catálogo.
     if self.buscar_pelicula(pelicula.id):                      # Si ya existe una película con el mismo ID, no se agrega y retorna el mensaje:
        print(f"✕  Ya existe una película con el ID {pelicula.id}. No se puede agregar.")
        return
     self.peliculas.append(pelicula)       # Se agrega la película a la lista.
     self.guardar_datos()               # Se actualiza el archivo con los nuevos datos.
     print(f"Película con ID {pelicula.id} agregada correctamente.")  

    def listar(self):      # Método para 'listar' todas las películas en el catálogo.
        if not self.peliculas:             # Si la lista está vacía, se retorna el mensaje:
            print("El catálogo está vacío.")     
        else:
            for pelicula in self.peliculas:      # Se recorren las películas y se muestran al usuario.
                print(pelicula)

    def eliminar(self):      # Método para eliminar el catálogo de películas.
        self.peliculas = []  # Se vacía la lista de películas.
        try:
            os.remove(self.ruta_archivo)        # Se intenta eliminar el archivo del catálogo e imprime el mensaje:
            print("Catálogo eliminado correctamente.")
        except FileNotFoundError:           # Pero si el archivo no existe muestra:
            print("El archivo no existe.")

    def buscar_pelicula(self, id):       # Método para buscar una película por su ID.
        return next((p for p in self.peliculas if p.id == id), None)     # Retorna la película si existe, de lo contrario muestra 'None'.

    def guardar_datos(self):             # Método para guardar los datos del catálogo en un archivo 'txt'.
        try:
            with open(self.ruta_archivo, 'w', encoding='utf-8') as f: 
                for pelicula in self.peliculas:     # Se recorre las películas y se escribe en el archivo.
                    f.write(f"{pelicula.id},{pelicula.titulo},{pelicula.duracion},{pelicula.genero}\n")
        except Exception as e:             # Manejo de errores en caso de fallo al escribir el archivo.
            print(f"✕  Error al guardar datos: {e}")

    def cargar_peliculas(self):         # Método para cargar las películas desde un archivo al iniciar el programa.
        if not os.path.exists(self.ruta_archivo):     # Si el archivo no existe, lo crea vacío.
            open(self.ruta_archivo, 'w', encoding='utf-8').close()    # Usado para abrir un archivo y escribir en él, para ser retornado al usuario. 
            return
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as f:     
                for linea in f:            # Se leen las líneas del archivo 'txt'.
                    datos = linea.strip().split(',')      # Elimina espacios en blanco innecesarios y divide el string en partes usando la coma como separador.
                    if len(datos) == 4:
                        try:
                            id = int(datos[0])  # Se convierte el ID a entero.
                            titulo = datos[1]    # Estos se quedan en un string.
                            duracion = int(datos[2])    # Se convierte la duración a entero.
                            genero = datos[3]
                            self.peliculas.append(Pelicula(id, titulo, duracion, genero))    # Se añade la película a la lista.
                        except ValueError:
                            print(f"✕  Error en los datos: {linea.strip()}")
        except Exception as e:                                       # Manejo de errores en caso de fallo al leer el archivo, mostrando:
            print(f"✕  Los datos no se pueden cargar: {e}")    

def iniciar_programa():                # Función principal para iniciar el programa.
    archivo = input("Ingrese el nombre del catálogo de películas: ")       # Se solicita el nombre del archivo 'txt' o catálogo.
    if not archivo.endswith(".txt"):       # Si el usuario no agrega ".txt", se coloca automáticamente.
        archivo += ".txt"

    if not os.path.exists(archivo):        
       print(f" →  El catálogo {archivo} no existía y ha sido creado.")       # Se informa que se creó el archivo.

    else:
       print(f" →  El catálogo {archivo} ya existe.")     # Mensaje por si el archivo ya existía.
    catalogo = CatalogoPelicula("Mi Catálogo", archivo)  
    menu(catalogo)          # Se llama a la función del menú.

def menu(catalogo):        # Función que maneja el menú de opciones del usuario.
    while True:               # Bucle.
        print("\nMenú de opciones:")
        print("1 →  Agregar película.")
        print("2 →  Listar películas.")
        print("3 →  Eliminar catálogo de películas.")
        print("4 →  Salir.")
        opcion = input("Opción a elegir: ")

        if opcion == "1":    # Opción para agregar una película.
            try:
                print("\n  🔹 Por favor, ingrese:")   # Se solicitan los datos:
                id = int(input(" →  ID de la película: "))
                titulo = input(" →  Título de la película: ")
                duracion = int(input(" →  Duración (en min): "))
                genero = input(" →  Género: ")
                pelicula = Pelicula(id, titulo, duracion, genero)  # Se crea una nueva película.
                catalogo.agregar(pelicula)  # Se agrega la película al catálogo.
            except ValueError:                       
                print("✕  Ingrese solo NÚMEROS para ID y la duración.")     # Mensaje de error si ingresan datos incorrectos.

        elif opcion == "2":         # Opción para listar / mostrar las películas.
            print("\nListado del catálogo de películas:")
            catalogo.listar()

        elif opcion == "3":            # Opción para eliminar el catálogo.
            confirmar = input("¿Está seguro de eliminar el catálogo? → (S/N): ").strip().lower() # Se confirma si el usuario lo desea hacer o no.
            if confirmar == "s":
                catalogo.eliminar()
            elif confirmar == "n":
                menu (catalogo)      # Si la respuesta es 'n', se le retorna al usuario el menú principal.
            else:
                print("✕  Ingrese 's' o 'n' para validar la respuesta.")        # Mensaje de error si la entrada no es válida.

        elif opcion == "4":          # Opción para salir del programa y se cierra el bucle con el break.
            print("\nEl programa finalizó. ¡Nos vemos pronto!😄")
            break
        else:
            print("✕  Incorrecto, agregue una opción entre 1 - 4.")       # Mensaje si la opción ingresada no es válida.

print("—" * 70)
print("      🎬      ¡Bienvenido a nuestro Catálogo de Películas!      🎥      ")      # Mensaje de bienvenida al programa.
print("—" * 70)
iniciar_programa()         # Se llama a la función principal para iniciar el programa.