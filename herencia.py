#!/usr/bin/python3

class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):

        pass

class Perro(Animal):
    def hablar(self):
        return f"¡Guau!"

class Gato(Animal):
    def hablar(self):
        return f"¡Miau!"

def hacer_hablar(objeto):
    print(f"{objeto.nombre} hace {objeto.hablar()}")

perro1 = Perro("piojos")
gato1 = Gato("chester")

hacer_hablar(perro1)
hacer_hablar(gato1)
        
