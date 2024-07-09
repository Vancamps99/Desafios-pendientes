from .models import Vehiculo, Chofer, RegistroContabilidad

def crear_vehiculo(patente, marca, modelo, year, activo=False):
    vehiculo = Vehiculo.objects.create(patente=patente, marca=marca, modelo=modelo, year=year, activo=activo)
    return vehiculo

def crear_chofer(rut, nombre, apellido, licencia, activo, creacion_registro, vehiculo_patente):
    vehiculo = Vehiculo.objects.get(patente=vehiculo_patente)
    chofer = Chofer.objects.create(rut=rut, nombre=nombre, apellido=apellido, licencia=licencia, activo=activo, creacion_registro=creacion_registro, vehiculo=vehiculo)
    return chofer

def crear_registro_contable(fecha_compra, valor, vehiculo_patente):
    vehiculo = Vehiculo.objects.get(patente=vehiculo_patente)
    if RegistroContabilidad.objects.filter(vehiculo=vehiculo).exists():
        raise ValueError(f"Ya existe un registro contable para el vehículo con patente {vehiculo_patente}")
    registro = RegistroContabilidad.objects.create(fecha_compra=fecha_compra, valor=valor, vehiculo=vehiculo)
    return registro

def deshabilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = False
    chofer.save()

def deshabilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = False
    vehiculo.save()

def habilitar_chofer(rut):
    chofer = Chofer.objects.get(rut=rut)
    chofer.activo = True
    chofer.save()

def habilitar_vehiculo(patente):
    vehiculo = Vehiculo.objects.get(patente=patente)
    vehiculo.activo = True
    vehiculo.save()

def obtener_vehiculo(patente=None):
    if patente:
        vehiculo = Vehiculo.objects.get(patente=patente)
        return vehiculo
    else:
        vehiculos = Vehiculo.objects.all()
        return vehiculos

def obtener_chofer(rut=None):
    if rut:
        chofer = Chofer.objects.get(rut=rut)
        return chofer
    else:
        choferes = Chofer.objects.all()
        return choferes

from .models import Vehiculo, Chofer, RegistroContabilidad

def imprimir_datos_vehiculos():
    vehiculos = Vehiculo.objects.all()
    for vehiculo in vehiculos:
        try:
            chofer_asignado = vehiculo.chofer.nombre
        except Chofer.DoesNotExist:
            chofer_asignado = "Sin chofer asignado"

        try:
            registro = RegistroContabilidad.objects.get(vehiculo=vehiculo)
            valor_usd = registro.valor * 1.18  # Suponiendo una conversión de USD a CLP (peso chileno)
        except RegistroContabilidad.DoesNotExist:
            valor_usd = "Sin registro contable"

        print(f"Patente: {vehiculo.patente}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.year}, Chofer: {chofer_asignado}, Valor en $USD: {valor_usd}")
