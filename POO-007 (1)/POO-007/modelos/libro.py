class Libro:
    def __init__(self, titulo, autor, anio, genero):
        # Atributos privados (convención con guion bajo)
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._genero = genero
        self._disponible = True

    # Métodos públicos (interfaz)
    def mostrar_informacion(self):
        estado = "Disponible" if self._disponible else "Prestado"
        return f"Título: {self._titulo}, Autor: {self._autor}, Año: {self._anio}, Género: {self._genero}, Estado: {estado}"

    def prestar(self):
        if self._disponible:
            self._disponible = False
            return f"El libro '{self._titulo}' ha sido prestado."
        else:
            return f"El libro '{self._titulo}' no está disponible."

    def devolver(self):
        self._disponible = True
        return f"El libro '{self._titulo}' ha sido devuelto y está disponible."

    # Getters y setters controlados
    def get_titulo(self):
        return self._titulo

    def set_titulo(self, nuevo_titulo):
        if nuevo_titulo.strip() != "":
            self._titulo = nuevo_titulo
            return f"Título actualizado a: {self._titulo}"
        else:
            return "El título no puede estar vacío."

    def get_autor(self):
        return self._autor

    def set_autor(self, nuevo_autor):
        if nuevo_autor.strip() != "":
            self._autor = nuevo_autor
            return f"Autor actualizado a: {self._autor}"
        else:
            return "El autor no puede estar vacío."
