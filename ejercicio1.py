# En el archivo ejercicio1.py

class Bicicleta:
    def __init__(self, marca, color, tipo):
        self.marca = marca
        self.color = color
        self.tipo = tipo
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        print("Velocidad anterior:",bicicleta1.velocidad)
        if self.velocidad >= decremento:
            self.velocidad -= decremento
        else:
            print("La bicicleta ya está detenida.")

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

bicicleta1 = Bicicleta("VENZO", "NEGRA", "CIUDAD")
print(f"Marca: {bicicleta1.marca}, Color: {bicicleta1.color}, Tipo: {bicicleta1.tipo}")

bicicleta1.acelerar(20)
print("Velocidad actual:", bicicleta1.velocidad)

bicicleta1.frenar(10)
print("Velocidad después de frenar:", bicicleta1.velocidad)

bicicleta1.cambiar_color("VIOLETA")
print("Nuevo color:", bicicleta1.color)

