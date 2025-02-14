
class Pelicula:       # Definimos la clase Película, que contiene sus atributos.
    
    def __init__(self, id, titulo, duracion, genero):  # Método constructor, inicializa los atributos de Película.
        self.__id = id         # Atributo privado (con doble guión bajo), que no es accesible directamente desde fuera de la clase.
        self._titulo = titulo  
        self._duracion = duracion   # Atributo protegido (con un solo guión bajo), sugiere no modificarse fuera de la clase.
        self._genero = genero

    @property        # Decorador que convierte este método en un getter para obtener el ID de la película.
    def id(self):
        return self.__id  # Devuelve el valor del ID. (atributo privado)
    
    @property          # Getter para obtener el título de la película.
    def titulo(self):
        return self._titulo
    
    @titulo.setter      # Setter para modificar el título de la película.
    def titulo(self, tituloreal):
        self._titulo = tituloreal

    @property              # Getter para obtener la duración de la película.
    def duracion(self):
        return self._duracion
    
    @duracion.setter           # Setter para modificar la duración de la película.
    def duracion(self, duracionreal):
        self._duracion = duracionreal

    @property         # Getter para obtener el género de la película.
    def genero(self):
        return self._genero
    
    @genero.setter          # Setter para modificar el género de la película.
    def genero(self, generoreal):
        self._genero = generoreal

    def __str__(self):      # Método __str__, devuelve una representación en cadena del objeto Pelicula.
        return (                   # Nos está retornando los 4 valores que estamos solitando de cada película.
            f"ID: {self.id} | " 
            f"Título: {self.titulo} | "
            f"Duración: {self.duracion} min | "
            f"Género: {self.genero}"
        )