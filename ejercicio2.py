class Animal:
    def __init__(self, cantidad_patas, tipo):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def moverse(self):
        pass

class Perro(Animal):
    def __init__(self, cantidad_patas, tipo, nombre, raza):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def moverse(self):
        return "Estoy corriendo"

class Aguila(Animal):
    def moverse(self):
        return "Estoy volando"


perro1 = Perro(4, "Vertebrado", "Pedrito", "Caniche")
aguila1 = Aguila(2, "Vertebrado")

print(f"Cantidad de patas: {perro1.cantidad_patas}, Tipo: {perro1.tipo}, Nombre: {perro1.nombre}, Raza: {perro1.raza}")


print(perro1.moverse())

print(aguila1.moverse())
