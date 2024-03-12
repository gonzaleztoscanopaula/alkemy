import datetime

class Empleado:
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContrato):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anioIngreso = anioIngreso
        self.tipoContrato = tipoContrato

    def calcularSalario(self):
        pass

    def mostrarSalario(self):
        pass

class EmpSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContrato, salarioFijo):
        super().__init__(dni, nombre, apellido, anioIngreso, tipoContrato)
        self.salarioFijo = salarioFijo

    def calcularSalario(self):
        anio_actual = datetime.datetime.now().year
        anios_antiguedad = anio_actual - self.anioIngreso
        if anios_antiguedad < 2:
            salario_total = self.salarioFijo
        elif 2 <= anios_antiguedad <= 5:
            salario_total = (self.salarioFijo * 1.05)
        else:
            salario_total = (self.salarioFijo * 1.1)
        return salario_total

    def mostrarSalario(self):
        print(f"{self.nombre} {self.apellido} - Salario: {self.calcularSalario()}")

class EmpAComision(Empleado):
    def __init__(self, dni, nombre, apellido, anioIngreso, tipoContrato, salarioMinimo, clientesCaptados, montoxCliente):
        super().__init__(dni, nombre, apellido, anioIngreso, tipoContrato)
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoxCliente = montoxCliente

    def calcularSalario(self):
        salario_comision = self.clientesCaptados * self.montoxCliente
        if salario_comision < self.salarioMinimo:
            return self.salarioMinimo
        else:
            return salario_comision

    def mostrarSalario(self):
        print(f"{self.nombre} {self.apellido} - Salario: {self.calcularSalario()}")


empleado1 = EmpSalarioFijo("320000001", "Juan", "Perez", 2018, "Salario Fijo", 2000)
empleado2 = EmpSalarioFijo("320000002", "Maria", "Gomez", 2019, "Salario Fijo", 2200)
empleado3 = EmpSalarioFijo("320000003", "Carlos", "Lopez", 2017, "Salario Fijo", 2500)
empleado4 = EmpSalarioFijo("320000004", "Laura", "Rodriguez", 2016, "Salario Fijo", 2100)

empleado5 = EmpAComision("320000005", "Ana", "Martinez", 2015, "A Comisión", 1500, 15, 100)
empleado6 = EmpAComision("320000006", "Pedro", "Gonzalez", 2018, "A Comisión", 1600, 20, 80)
empleado7 = EmpAComision("320000007", "Sofia", "Sanchez", 2019, "A Comisión", 1700, 18, 90)
empleado8 = EmpAComision("320000008", "Diego", "Fernandez", 2017, "A Comisión", 1800, 25, 70)

empleado9 = EmpSalarioFijo("320000009", "Elena", "Diaz", 2016, "Salario Fijo", 2300)
empleado10 = EmpSalarioFijo("320000010", "Lucas", "Molina", 2015, "Salario Fijo", 2400)

print(f"DNI: {empleado1.dni}, Nombre: {empleado1.nombre} {empleado1.apellido}, Tipo de Contrato: {empleado1.tipoContrato}, Salario: {empleado1.calcularSalario()}")
print(f"DNI: {empleado2.dni}, Nombre: {empleado2.nombre} {empleado2.apellido}, Tipo de Contrato: {empleado2.tipoContrato}, Salario: {empleado2.calcularSalario()}")
print(f"DNI: {empleado3.dni}, Nombre: {empleado3.nombre} {empleado3.apellido}, Tipo de Contrato: {empleado3.tipoContrato}, Salario: {empleado3.calcularSalario()}")
print(f"DNI: {empleado4.dni}, Nombre: {empleado4.nombre} {empleado4.apellido}, Tipo de Contrato: {empleado4.tipoContrato}, Salario: {empleado4.calcularSalario()}")