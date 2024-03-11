#PROPIEDADES O ATRIBUTOS ¿QUE CARACTERIZA A MI OBJETO?


class Auto:

    def __init__(self, marca, modelo, color, tipoCombustible, cantPuertas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipoCombustible = tipoCombustible 
        self.cantPuertas = cantPuertas

#¿QUE COSAS PUEDE HACER UN AUTO? ACCIONES O COMPORTAMIENTOS
        #setters y getters
        #set= settear establecer un valor
        #getter= nos devuelve lo que necesitamos de ese objeto
    def getMarca(self):
        return marca
    def getModelo(self):
        return modelo
    def getColor(self):
        return color
    def getTipoCombustible(self):
        return tipoCombustible
    def getCantPuertas(self):
        return cantPuertas
    
    def mostrarAuto(self):
        print(
            self.getMarca() 
            + " " + self.getModelo()
            + " " +  self.getColor()
            + " " +   self.getTipoCombustible()
            + " " +   self.getCantPuertas()
        )
    #ESTAS SON FUNCIONES DENTRO DE NUESTRA CLASE VEHICULO

marca= input(f"ingresar marca:  ")
modelo= input(f"ingresar modelo:  ")
color= input(f"ingresar color:  ")
tipoCombustible= input(f"ingresar tipo de combustible: ")
cantPuertas= input(f"ingresar cantidad de puertas: ")

auto1= Auto(marca, modelo, color, tipoCombustible, cantPuertas)

print(auto1.mostrarAuto())
