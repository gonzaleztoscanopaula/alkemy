#CREAR UNA CLASE PORDUCTO QUE TENGA 3 HIJOS

#LA CLASE DEBE TENER 3 ATRIBUTOS
#METODO MOSTRAR PRODUCTO
#Y LOS HIJOS DEBEN TENER 2 ATRIBUTOS CADA UNO
#LIBRO - PELICULA - DISCO



class Producto:
    def __init__(self, categoria, precio, cantidadEnStock):
        self.categoria = categoria
        self.precio = precio
        self.cantidadEnStock = cantidadEnStock
    
    def mostrarProducto(self):
        pass


class Libro(Producto):

    def __init__(self,categoria, precio, cantidadEnStock, nombre, autor):
        super().__init__(categoria, precio, cantidadEnStock)
        self.nombre = nombre
        self.autor = autor

    def mostrarProducto(self):
        return print(f"La categoria del libro es {self.categoria}, su precio es {self.precio}, la cantidad en stock disponible es {self.cantidadEnStock}, el nombre del libro es {self.nombre}, el autor de la obra es {self.autor}")

    
class Pelicula(Producto):

    def __init__(self,categoria, precio, cantidadEnStock, nombre, genero, sagas):
        super().__init__(categoria, precio, cantidadEnStock)
        self.nombre = nombre
        self.genero = genero
        self.sagas = sagas

    def mostrarProducto(self):
        return print(f"La categoria de la película es {self.categoria}, su precio es {self.precio}, la cantidad en stock disponible es {self.cantidadEnStock}, el nombre dela película es {self.nombre}, el genero de la pelicula es {self.genero}, y esta pelicula tiene {self.sagas} sagas.")
    
class Disco(Producto):

    def __init__(self,categoria, precio, cantidadEnStock, artista, genero, año):
        super().__init__(categoria, precio, cantidadEnStock)
        self.artista = artista
        self.genero = genero
        self.año = año

    def mostrarProducto(self):
        return print(f"La categoria de la música es {self.categoria}, su precio es {self.precio}, la cantidad en stock disponible es {self.cantidadEnStock}, el artista del disco es {self.artista}, el genero de la cancion es {self.genero}, y el año del lanzamiento {self.año}")



libro1 = Libro("Ficción", 20.99, 50, "El Señor de los Anillos", "J.R.R. Tolkien")


pelicula1 = Pelicula("Acción", 15.50, 100, "Matrix", "Ciencia Ficción", "3")


disco1 = Disco("Rock", 12.99, 30, "Queen", "Rock", 1980)


print (libro1.mostrarProducto())
print (pelicula1.mostrarProducto())
print (disco1.mostrarProducto())
