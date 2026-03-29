from enum import Enum

# ENUMERACIONES
class Ubicacion(Enum):
    ENDOR = 1
    CUMULO_RAIMOS = 2
    NEBULOSA_KALIIDA = 3

class ClaseNave(Enum):
    EJECUTOR = 1
    ECLIPSE = 2
    SOBERANO = 3

# CLASES BASE Y NAVES
class UnidadCombate:
    def __init__(self, id_combate, clave_cifrada):
        self.id_combate = id_combate
        self.clave_cifrada = clave_cifrada
        
    def __str__(self):
        return f"[ID: {self.id_combate}]"

class Nave(UnidadCombate):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_repuestos):
        super().__init__(id_combate, clave_cifrada)
        self.nombre = nombre
        self.catalogo_repuestos = catalogo_repuestos # Lista de texto

    def __str__(self):
        return super().__str__() + f" Nave: {self.nombre}"

class EstacionEspacial(Nave):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_repuestos, tripulacion, pasaje, ubicacion):
        super().__init__(id_combate, clave_cifrada, nombre, catalogo_repuestos)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

class NaveEstelar(Nave):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_repuestos, tripulacion, pasaje, clase):
        super().__init__(id_combate, clave_cifrada, nombre, catalogo_repuestos)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase

class CazaEstelar(Nave):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_repuestos, dotacion):
        super().__init__(id_combate, clave_cifrada, nombre, catalogo_repuestos)
        self.dotacion = dotacion