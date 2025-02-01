#!/usr/bin/python3

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        return f'Hola soy {self.nombre}, mi edad es {self.edad}'

class Empleado(Persona):

    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def saludo(self):
        return f'{super().saludo()} y gano {self.sueldo}'

persona1 = Empleado("piojos", 22, 3444)
print(persona1.saludo())



