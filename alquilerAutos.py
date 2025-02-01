#!/usr/bin/python3

# Crear a base de clases un alquilador de autos, donde se presten los autos y se cobre x tarifa
# Cuando se alquile un auto deberá desaparecer de la lista en la cual estaba guardado

class Auto:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True
    def __str__(self):
        return f"Auto(Matricula = {self.matricula} Modelo = {self.modelo} Disponible: { 'Si' if self.disponible else 'No'})"

    def prestado(self):
        self.disponible = False
    
    def devolver(self):
        self.disponible = True
class Flota(): 

    def __init__(self):
        self.autos = [] #Lista de objetos

    def agregar_auto(self, auto):
        self.autos.append(auto)

    def alquilar_auto(self, modelo):
        for auto in self.autos:
            if auto.modelo == modelo:
                auto.prestado()
                break
            else:
                print("NO se ha encontrado ese modelo disponible")

    def devolver_auto(self, modelo):
        for auto in self.autos:
            if auto.modelo == modelo:
                auto.devolver()
                break
            else:
                print("EL auto sigue prestado")

    def __str__(self):
        return  "\n".join(str(auto) for auto in self.autos)
 

if __name__ == '__main__':

    flota = Flota()
    auto1 = Auto("A1213", "Skyline")
    auto2 = Auto("P2324", "Infernus")
    auto3 = Auto("B2312", "Sabre GT")

    flota.agregar_auto(auto1)
    flota.agregar_auto(auto2)
    flota.agregar_auto(auto3)
    print("\n [+] Flota incial")
    print(flota) 
    flota.alquilar_auto("Sabre GT")
    flota.alquilar_auto("Skyline")
    flota.alquilar_auto("Infernus")
    print("\n[!] Verificación si se ha prestado el auto \n")
    print(flota)
    flota.devolver_auto("Sabre GT")
    print("\n[!] Verificación si se ha devuelto el auto \n")
    print(flota)

    


