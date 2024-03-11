#Primer ejercicio del modulo:
#Crear una clase llamada bicicleta, agegar el metodo init, agregar 3 atributos, agregar al menos 3 metodos


class Bicicleta:
    def __init__(self, marca, color, precio, rodado, talle):
        self.marca = marca
        self.color = color
        self.precio = precio
        self.rodado = rodado
        self.talle = talle
    
    def cambiarColor (self, nuevoColor):
        self.color = nuevoColor
        return print(f"El color de bicicleta elegido es {nuevoColor}")
    
    def cambiarTalle(self, nuevoTalle):
        self.talle = nuevoTalle
        return print(f"El talle de su bicicleta ahora es {nuevoTalle}")

    def acelerar(self):
        return print("Estas acelerando")


bicicleta1= Bicicleta("VENZO","NEGRO","1200","29", "S")

print(f"Marca: {bicicleta1.marca}, Color: {bicicleta1.color}, Precio: {bicicleta1.precio}, Rodado: {bicicleta1.rodado} Talle: {bicicleta1.talle}")


bicicleta1.cambiarTalle("L")

bicicleta1.cambiarColor("ROJO")

bicicleta1.acelerar()

print(f"Marca: {bicicleta1.marca}, Color: {bicicleta1.color}, Precio: {bicicleta1.precio}, Rodado: {bicicleta1.rodado} Talle: {bicicleta1.talle}")
