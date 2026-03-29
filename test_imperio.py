import pytest
from sistema_imperio import Repuesto, Almacen

def test_creacion_repuesto():
    # Comprobamos que se inicializa y se lee bien
    rep = Repuesto("Cristal", "Mina 1", 100, 50.5)
    assert rep.nombre == "Cristal"
    assert rep.get_cantidad() == 100

def test_modificar_stock_valido():
    rep = Repuesto("Cristal", "Mina 1", 100, 50.5)
    rep.set_cantidad(80)
    assert rep.get_cantidad() == 80

def test_excepcion_stock_negativo():
    # Comprobamos que salta ValueError al intentar poner stock negativo
    rep = Repuesto("Cristal", "Mina 1", 100, 50.5)
    with pytest.raises(ValueError):
        rep.set_cantidad(-10)

def test_almacen_sacar_repuesto_exito():
    almacen = Almacen("A1", "Tatooine")
    rep = Repuesto("Tornillo", "Ferretería Imperio", 50, 1.0)
    almacen.agregar_repuesto(rep)
    
    # Sacamos 10 tornillos
    almacen.sacar_repuesto("Tornillo", 10)
    assert rep.get_cantidad() == 40

def test_almacen_sacar_repuesto_insuficiente():
    # Comprobamos que salta la excepción si pedimos más de lo que hay
    almacen = Almacen("A1", "Tatooine")
    rep = Repuesto("Tornillo", "Ferretería Imperio", 5, 1.0)
    almacen.agregar_repuesto(rep)
    
    with pytest.raises(ValueError):
        almacen.sacar_repuesto("Tornillo", 20)

def test_almacen_repuesto_no_existe():
    # Comprobamos que salta KeyError si buscamos algo que no está
    almacen = Almacen("A1", "Tatooine")
    with pytest.raises(KeyError):
        almacen.sacar_repuesto("Hiperimpulsor", 1)