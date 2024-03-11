#Ejemplo de POLIMORFISMO
#Diferencias minimas entre las clases

#Publicas - pueden ser leidos sin un getter - métodos
#_privadas - solo pueden ser leidos con un getter - atributos

class Producto:
    def __init__(self, _id, _titulo, _autor, _precio, _tipoProducto):
        self._id = _id
        self._titulo = _titulo
        self._autor = _autor
        self._precio = _precio
        self._tipoProducto = _tipoProducto

    def getTitulo(self):
        return self._titulo
    
    def agregarAlCarrito(self):
        print(f"{self.getTitulo()} agregado al carrito")


class Libro():
    def __init__(self, _editorial, _generoLiterario):
        self._editorial = _editorial
        self._cantPaginas = _generoLiterario

class Pelicula():
    def __init__(self, _duracion, _generoCine):
        self._duracion = _duracion
        self._generoCine = _generoCine

class Musica ():
    def __init__(self, _duracion, _generoMusica):
        self._duracion = _duracion
        self._generoMusica = _generoMusica


