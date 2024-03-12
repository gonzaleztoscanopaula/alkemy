class Fabrica:
    def __init__(self):
        self.lista_sucursales = []

    def agregar_sucursal(self, sucursal):
        self.lista_sucursales.append(sucursal)

    def listar_instrumentos(self):
        for sucursal in self.lista_sucursales:
            sucursal.mostrar_instrumentos()

    def instrumentos_por_tipo(self, tipo):
        instrumentos = []
        for sucursal in self.lista_sucursales:
            instrumentos.extend(sucursal.instrumentos_por_tipo(tipo))
        return instrumentos

    def agregar_instrumento(self, sucursal_nombre, instrumento):
        for sucursal in self.lista_sucursales:
            if sucursal.nombre == sucursal_nombre:
                sucursal.agregar_instrumento(instrumento)
                break

    def borrar_instrumento(self, instrumento_id):
        for sucursal in self.lista_sucursales:
            sucursal.borrar_instrumento(instrumento_id)

    def modificar_instrumento(self, instrumento_id, nuevo_instrumento):
        for sucursal in self.lista_sucursales:
            for instrumento in sucursal.lista_instrumentos:
                if instrumento._id == instrumento_id:
                    instrumento.nombre = nuevo_instrumento.nombre
                    instrumento.precio = nuevo_instrumento.precio
                    instrumento.tipo = nuevo_instrumento.tipo
                    break

    def porcentaje_instrumentos_por_tipo(self, nombre_sucursal):
        for sucursal in self.lista_sucursales:
            if sucursal.nombre == nombre_sucursal:
                return sucursal.porcentaje_instrumentos_por_tipo()


class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_instrumentos = []

    def mostrar_instrumentos(self):
        print(f"Instrumentos en la sucursal '{self.nombre}':")
        for instrumento in self.lista_instrumentos:
            print(f"ID: {instrumento._id}, Nombre: {instrumento.nombre}, Precio: {instrumento.precio}, Tipo: {instrumento.tipo}")

    def agregar_instrumento(self, instrumento):
        self.lista_instrumentos.append(instrumento)

    def instrumentos_por_tipo(self, tipo):
        return [instrumento for instrumento in self.lista_instrumentos if instrumento.tipo == tipo]

    def borrar_instrumento(self, instrumento_id):
        self.lista_instrumentos = [instrumento for instrumento in self.lista_instrumentos if instrumento._id != instrumento_id]

    def porcentaje_instrumentos_por_tipo(self):
        total = len(self.lista_instrumentos)
        percusion = sum(1 for instrumento in self.lista_instrumentos if instrumento.tipo == "percusion")
        viento = sum(1 for instrumento in self.lista_instrumentos if instrumento.tipo == "viento")
        cuerda = sum(1 for instrumento in self.lista_instrumentos if instrumento.tipo == "cuerda")
        return {"percusion": percusion/total * 100, "viento": viento/total * 100, "cuerda": cuerda/total * 100}


class Instrumento:
    def __init__(self, _id, nombre, precio, tipo):
        self._id = _id
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo


def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Mostrar todos los datos de los instrumentos.")
    print("2. Mostrar instrumentos de un tipo específico.")
    print("3. Agregar un nuevo instrumento.")
    print("4. Borrar un instrumento.")
    print("5. Modificar un instrumento.")
    print("6. Mostrar porcentaje de instrumentos por tipo en una sucursal.")
    print("7. Salir")


def validar_opcion(opcion):
    if opcion.isdigit():
        opcion = int(opcion)
        if 1 <= opcion <= 7:
            return opcion
    return None


def main():
    fabrica = Fabrica()

    sucursal1 = Sucursal("Sucursal A")
    sucursal1.agregar_instrumento(Instrumento("1A", "Guitarra", 200, "cuerda"))
    sucursal1.agregar_instrumento(Instrumento("2A", "Flauta", 100, "viento"))
    fabrica.agregar_sucursal(sucursal1)

    sucursal2 = Sucursal("Sucursal B")
    sucursal2.agregar_instrumento(Instrumento("1B", "Batería", 500, "percusion"))
    sucursal2.agregar_instrumento(Instrumento("2B", "Violín", 300, "cuerda"))
    fabrica.agregar_sucursal(sucursal2)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        opcion_valida = validar_opcion(opcion)
        if opcion_valida is None:
            print("Opción inválida. Intente de nuevo.")
            continue

        if opcion_valida == 1:
            fabrica.listar_instrumentos()
        elif opcion_valida == 2:
            tipo = input("Ingrese el tipo de instrumento (percusion, viento, cuerda): ")
            instrumentos = fabrica.instrumentos_por_tipo(tipo)
            for instrumento in instrumentos:
                print(f"ID: {instrumento._id}, Nombre: {instrumento.nombre}, Precio: {instrumento.precio}, Tipo: {instrumento.tipo}")
        elif opcion_valida == 3:
            sucursal_nombre = input("Ingrese el nombre de la sucursal: ")
            nombre = input("Ingrese el nombre del instrumento: ")
            precio = float(input("Ingrese el precio del instrumento: "))
            tipo = input("Ingrese el tipo de instrumento (percusion, viento, cuerda): ")
            nuevo_instrumento = Instrumento(input("Ingrese el ID del instrumento: "), nombre, precio, tipo)
            fabrica.agregar_instrumento(sucursal_nombre, nuevo_instrumento)
            print("Instrumento agregado correctamente.")
        elif opcion_valida == 4:
            instrumento_id = input("Ingrese el ID del instrumento a borrar: ")
            fabrica.borrar_instrumento(instrumento_id)
            print("Instrumento borrado correctamente.")
        elif opcion_valida == 5:
            instrumento_id = input("Ingrese el ID del instrumento a modificar: ")
            nombre = input("Ingrese el nuevo nombre del instrumento: ")
            precio = float(input("Ingrese el nuevo precio del instrumento: "))
            tipo = input("Ingrese el nuevo tipo de instrumento (percusion, viento, cuerda): ")
            nuevo_instrumento = Instrumento(instrumento_id, nombre, precio, tipo)
            fabrica.modificar_instrumento(instrumento_id, nuevo_instrumento)
            print("Instrumento modificado correctamente.")
        elif opcion_valida == 6:
            sucursal_nombre = input("Ingrese el nombre de la sucursal: ")
            porcentajes = fabrica.porcentaje_instrumentos_por_tipo(sucursal_nombre)
            for tipo, porcentaje in porcentajes.items():
                print(f"{tipo}: {porcentaje:.2f}%")
        elif opcion_valida == 7:
            print("¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
