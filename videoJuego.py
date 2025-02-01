#!/usr/bin/python3
#Juegos
juegos =["Persona 5", "CyberPunk 2077", "The Last Of Us"]

#Género 

generos = {
    "Persona 5" : "RPG",
    "CyberPunk 2077": "Mundo Libre",
    "The Last Of Us": "Aventura"
}

#Ventas y Stock
ventas_y_stock = {
    "Persona 5" : (200, 600),
    "CyberPunk 2077": (300, 400),
    "The Last Of Us": (100, 200)
}

# Clientes
clientes = {
    "Persona 5" : {"Piojos", "Oreo", "Extranquis"},
    "CyberPunk 2077": {"Negra", "Sutano", "Mengano"},
    "The Last Of Us" : {"Piojos", "Raymunda", "Sutano"}
}

def sumario(juego):
    #sumario
    print(f"\n[i] Resumen del juego {juego}")
    print(f"\t[+] Género del juego: {generos[juego]}")
    print(f"\t[+] Ventas del juego: {ventas_y_stock[juego][0]}")
    print(f"\t[+] Juegos en Stock: {ventas_y_stock[juego][1]}")
    print(f"\t[+] Clientes que lo han adquirido: {', '.join(clientes[juego])}")

for juego in juegos:
    if ventas_y_stock[juego][0] < 500:
        print(f"El juego con de {ventas_y_stock[juego][0]} ventas es {juego}")

ventas_totales = lambda :sum(venta for venta, _ in ventas_y_stock.values() )

print(f"[+] Las ventas totales {ventas_totales()}")
