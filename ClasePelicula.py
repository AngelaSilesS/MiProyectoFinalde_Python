class Pelicula:
    def init(self, id, titulo, duracion, genero):
        self.__id = id  
        self._titulo = titulo
        self._duracion = duracion
        self._genero = genero

    @property
    def id(self):
        return self.__id  
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, tituloreal):
        self._titulo = tituloreal

    @property
    def duracion(self):
        return self._duracion
    
    @duracion.setter
    def duracion(self, duracionreal):
        self._duracion = duracionreal

    @property
    def genero(self):
        return self._genero
    
    @genero.setter
    def genero(self, generoreal):
        self._genero = generoreal

    def str(self):
        return (
            f"ID: {self.id} | " 
            f"Título: {self.titulo} | "
            f"Duración: {self.duracion} min | "
            f"Género: {self.genero}"
        )