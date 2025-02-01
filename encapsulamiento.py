#!/usr/bin/python3

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__km = 0

    def conducir(self, km):
        if km > 0:
            self.__km += km
        else:
            print('el km debe ser mayor a 0')
    def mostrar_kilometraje(self):
        return f"se han conducido {self.__km}"


coche = Coche("nissan", "tsuru")
coche.conducir(100)
print(coche.mostrar_kilometraje())
coche.conducir(200)
print(coche.mostrar_kilometraje())



