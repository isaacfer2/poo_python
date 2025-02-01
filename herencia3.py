#!/usr/bin/python3

class Dispositivo():
    def __init__(self, marca):

        self.marca = marca
    
    def escanear_vulnerabilidades(self):
        raise NotImplementedError("Este método debe ser definido por las clases hijas")

class Pc(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[!] Se encontro una vulnerabilidad critica en el equipo {self.marca}, MAXIMA PRIORIDAD"

class Movil(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[!] Puertos abiertos en dispotivo móvil {self.marca}! Aplicación maliciosa detectada"

class Router(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[!] Configuración inicial modificada, posible intrusión en el dispositivo"

def realizar_escaneo(dispositivo):
    print(dispositivo.escanear_vulnerabilidades())
    
pc = Pc("Hp")
telefono = Movil("huawei")
router = Router("Tp-Link")

realizar_escaneo(pc)
realizar_escaneo(telefono)
realizar_escaneo(router)


