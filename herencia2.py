#!/usr/bin/python3

class Automovil: # Quedaría mejor transporte
    def __init__(self, modelo, marca):

        self.modelo = modelo

        self.marca = marca

    def describir(self):
        return f"el {self.modelo} es de la marca {self.marca}"

class Carro(Automovil):

    def describir(self):
        return f"el modelo del carro es: {self.modelo} y de la marca {self.marca}"
        

class Moto(Automovil):
    
    def describir(self):
        return f"el modelo de la moto es: {self.modelo} y de la marca {self.marca}"

moto1 = Moto("breakout", "harley division")
carro1 = Carro("skyline", "Nissan")

def describir_vehiculo(vehiculo): #Polimorfismo
    print(vehiculo.describir())

describir_vehiculo(moto1)
describir_vehiculo(carro1)




