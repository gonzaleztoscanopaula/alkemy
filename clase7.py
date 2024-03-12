class Estudiante:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)    

    def promedio_calificaciones(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
#crear un estudiante
estudiante1= Estudiante("Juan", 20)

estudiante1.agregar_calificacion(8)
estudiante1.agregar_calificacion(10)
estudiante1.agregar_calificacion(7)

print ("Promedio de calificaciones:",estudiante1.nombre,estudiante1.promedio_calificaciones().__round__(2))