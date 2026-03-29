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
# Creamos una jerarquía de clases. UnidadCombate es la clase "Base".
# De esta forma, evitamos repetir los atributos id_combate y clave_cifrada en todas las naves.
class UnidadCombate:
    def __init__(self, id_combate, clave_cifrada):
        self.id_combate = id_combate
        self.clave_cifrada = clave_cifrada
        
    def __str__(self):
        return f"[ID: {self.id_combate}]"

# Nave hereda de UnidadCombate (Herencia simple)
class Nave(UnidadCombate):
    def __init__(self, id_combate, clave_cifrada, nombre, catalogo_repuestos):
        super().__init__(id_combate, clave_cifrada)
        self.nombre = nombre
        self.catalogo_repuestos = catalogo_repuestos # Lista de texto

    def __str__(self):
        return super().__str__() + f" Nave: {self.nombre}"

# Las naves específicas heredan de Nave, especializando sus atributos
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


# ALMACENES Y REPUESTOS
class Repuesto:
    def __init__(self, nombre, proveedor, cantidad, precio):
        self.nombre = nombre
        self.proveedor = proveedor
        # Encapsulamiento: Hacemos la cantidad privada (__) para evitar que se modifique desde fuera sin control.
        # Solo se puede acceder o modificar a través de los métodos get y set.
        self.__cantidad = cantidad
        self.precio = precio

    def get_cantidad(self):
        return self.__cantidad

    def set_cantidad(self, valor):
        if valor < 0:
            # Lanzamos excepción si intenta poner un stock negativo
            raise ValueError("Error: La cantidad de repuestos no puede ser negativa.")
        self.__cantidad = valor

    def __str__(self):
        return f"{self.nombre} (Stock: {self.__cantidad})"

class Almacen:
    def __init__(self, nombre, localizacion):
        self.nombre = nombre
        self.localizacion = localizacion
        self.lista_repuestos = []

    def agregar_repuesto(self, repuesto):
        self.lista_repuestos.append(repuesto)

    def sacar_repuesto(self, nombre_repuesto, cantidad):
        # Comprobamos las condiciones lógicas antes de operar.
        # Errores específicos (ValueError, KeyError) si algo falla.
        for repuesto in self.lista_repuestos:
            if repuesto.nombre == nombre_repuesto:
                if repuesto.get_cantidad() < cantidad:
                    raise ValueError(f"Error: No hay suficiente stock de '{nombre_repuesto}' para sacar {cantidad} unidades.")
                repuesto.set_cantidad(repuesto.get_cantidad() - cantidad)
                return True
        raise KeyError(f"Error: El repuesto '{nombre_repuesto}' no existe en este almacén.")

    def __str__(self):
        cadena = f"Almacen {self.nombre} en {self.localizacion}. Repuestos: "
        for r in self.lista_repuestos:
            cadena += str(r) + ", "
        return cadena

class MiImperio:
    def __init__(self, flota, almacenes):
        self.flota = flota
        self.almacenes = almacenes
        
    def __str__(self):
        return f"Sistema MiImperio: Naves registradas: {len(self.flota)}, Almacenes: {len(self.almacenes)}"


# CÓDIGO BÁSICO DE PRUEBA

if __name__ == "__main__":
    print("INICIANDO SISTEMA MiIMPERIO")
    
    # Crear Naves
    estacion1 = EstacionEspacial("EST-01", 1234, "Estrella de la Muerte", ["Panel", "Tubo"], 342953, 843342, Ubicacion.ENDOR)
    caza1 = CazaEstelar("TIE-99", 5678, "TIE Fighter Alpha", ["Motor iónico", "Cristal láser"], 1)
    
    # Crear Repuestos y Almacenes
    repuesto1 = Repuesto("Panel Solar", "Sienar Fleet Systems", 50, 1500.0)
    repuesto2 = Repuesto("Motor iónico", "Kuat Drive Yards", 10, 8500.0)
    
    almacen_principal = Almacen("Almacén Central", "Coruscant")
    almacen_principal.agregar_repuesto(repuesto1)
    almacen_principal.agregar_repuesto(repuesto2)
    
    # Crear el Sistema
    sistema = MiImperio([estacion1, caza1], [almacen_principal])
    
    # Mostrar por pantalla
    print("\nFLOTA")
    for nave in sistema.flota:
        print(nave)
        
    print("\nALMACENES")
    for almacen in sistema.almacenes:
        print(almacen)
        
    print("\nPRUEBA DE GESTIÓN DE EXCEPCIONES")
    almacen_principal.sacar_repuesto("Motor iónico", 20)
    almacen_principal.sacar_repuesto("Cañón de plasma", 1)