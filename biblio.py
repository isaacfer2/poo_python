#!/usr/bin/python3

class Libro():
    def __init__(self, id_libro, autor, nombre_libro):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self):
        return f"(id: {self.id_libro} autor:{self.autor} nombre del libro: {self.nombre_libro})"

    def __repr__(self):
        return self.__str__()

class Biblioteca:
    def __init__(self):
        self.libros = {} # Usamos diccionario por la capacidad de key y valor

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros:
            self.libros[libro.id_libro] = libro
        else:
            print(f'No se pudo agregar el libro')

    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado: # si true y false entonces convierte en true esta_prestado
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"[!] El libro esta prestado")

    def devolver_libro(self, id_libro):
        if id_libro in self.libros and self.libros[id_libro].esta_prestado: # si true y true entonces convierte a false esta_prestado
            self.libros[id_libro].esta_prestado = False

    @property
    def mostrar_libros(self):
        return [libros for libros in self.libros.values() if not libros.esta_prestado]

    @property 
    def mostrar_libros_prestados(self):
        return [libros for libros in self.libros.values() if libros.esta_prestado]

    
class BibliotecaInfantil(Biblioteca):
    def __init__(self):
        super().__init__()
        self.libros_para_ninos = {} 

    def agregar_libro(self, libro, es_para_ninos):
        super().agregar_libro(libro)
        self.libros_para_ninos[libro.id_libro] = es_para_ninos

    def prestar_libro(self, id_libro, es_para_ninos):
        if id_libro in self.libros and  and not self.libros[id_libro].esta_prestado: # si true y false entonces convierte en true esta_prestado
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"[!] El libro esta prestado")


if __name__ == '__main__':

    biblio = BibliotecaInfantil()

    libro1 = Libro(1, "Piojos", "Cómo ser piojoso en menos de 3 min")
    libro2 = Libro(2, "Oreo", "Hacke el pentagono en menos de 1hr")

    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)

    print(f'[+] Los libros disponibles son: {biblio.mostrar_libros}')

    biblio.prestar_libro(1)
    biblio.prestar_libro(2)
    print(f'[+] Los libros disponibles son: {biblio.mostrar_libros}')

    biblio.devolver_libro(1)
    print(f'[+] Los libros disponibles son: {biblio.mostrar_libros}')
    biblio.mostrar_libros_prestados
