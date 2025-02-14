import os
from ClasePelicula import Pelicula

class CatalogoPelicula:
    def init(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo
        self.peliculas = []
        self.cargar_peliculas()

    def agregar(self, pelicula):  
     if self.buscar_pelicula(pelicula.id):  
        print(f"✕  Ya existe una película con el ID {pelicula.id}. No se puede agregar.")
        return
     self.peliculas.append(pelicula)
     self.guardar_datos()
     print(f"Película con ID {pelicula.id} agregada correctamente.")  

    def listar(self): 
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            for pelicula in self.peliculas:
                print(pelicula)

    def eliminar(self):  
        self.peliculas = []
        try:
            os.remove(self.ruta_archivo)
            print("Catálogo eliminado correctamente.")
        except FileNotFoundError:
            print("El archivo no existe.")

    def buscar_pelicula(self, id):  
        return next((p for p in self.peliculas if p.id == id), None)     

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