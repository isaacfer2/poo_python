#!/usr/bin/python3

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False

    def alimentar(self):
        self.alimentado = True

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {'Alimentado' if self.alimentado else 'Hambriento'}"



class TiendaAnimales:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def alimentar_animales(self): #¿cómo cambio todas la variables de false a true?
        for animal in self.animales:
            animal.alimentar()

    def vender_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                self.animales.remove(animal)
                return 


if __name__ == '__main__':


    tienda = TiendaAnimales("Tienda Animales")

    gato = Animal('Chester', 'Gato')
    perro = Animal('Oreo', 'Perro')

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)
    
    tienda.mostrar_animales()
    tienda.alimentar_animales()
    print("\n [+] Mostrando animales una vez que han sido alimentados \n")
    tienda.mostrar_animales()

    tienda.vender_animal("Chester")
    print("[?] Se ha efectuado la compra \n")
    tienda.mostrar_animales()



