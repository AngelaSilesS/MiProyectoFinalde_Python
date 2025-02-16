
class Pelicula:       # Definimos la clase Película, que contiene sus atributos.
    
    def __init__(self, id, titulo, duracion, genero):  # Método constructor, inicializa los atributos de Película.
        self.__id = id         # Atributo privado (con doble guión bajo), que no es accesible directamente desde fuera de la clase.
        self._titulo = titulo  
        self._duracion = duracion   # Atributo protegido (con un solo guión bajo), sugiere no modificarse fuera de la clase.
        self._genero = genero

    @property  # Getter: Permite obtener el valor de un atributo privado o protegido de una clase. Se usa cuando no queremos acceder directamente al atributo, sino a través de un método que pueda aplicar validaciones o procesamientos antes de devolverlo.
    def id(self):
        return self.__id        # Devuelve el valor del ID. (atributo privado)
    
    @property         
    def titulo(self):
        return self._titulo            # Getter para obtener el título de la película.
    
    @titulo.setter  # Setter: Permite modificar el valor de un atributo, asegurando que cumpla ciertas condiciones antes de asignarlo. Cuando queremos restringir, validar o transformar datos antes de guardarlos en el atributo.
    def titulo(self, tituloreal):
        self._titulo = tituloreal

    @property              
    def duracion(self):         # Getter para obtener la duración de la película.
        return self._duracion
    
    @duracion.setter           
    def duracion(self, duracionreal):          # Setter para modificar la duración de la película.
        self._duracion = duracionreal

    @property        
    def genero(self):        # Getter para obtener el género de la película.
        return self._genero
    
    @genero.setter          
    def genero(self, generoreal):    # Setter para modificar el género de la película.
        self._genero = generoreal

    def __str__(self):      # Método __str__, devuelve una representación en cadena del objeto Pelicula.
        return (                   # Nos está retornando los 4 valores que estamos solitando de cada película.
            f"ID: {self.id} | " 
            f"Título: {self.titulo} | "
            f"Duración: {self.duracion} min | "
            f"Género: {self.genero}"
        )