from inspeccion.models import *
from django.utils import timezone

# Crear datos de prueba mínimos para poder cerrar una orden de inspección
fab = Fabricante.objects.create(razon_social='SismoTech')
modelo = ModeloSismografo.objects.create(nombre='ST-1000', caracteristicas='Alta sensibilidad', fabricante=fab)
estacion = EstacionSismologica.objects.create(codigo='ES001', nombre='Estación Central', latitud=-34.6, longitud=-58.4)
sismografo = Sismografo.objects.create(identificador='SG-001', modelo=modelo, estacion=estacion)
perfil = Perfil.objects.create(nombre='Técnico', descripcion='Perfil técnico')
emp = Empleado.objects.create(nombre='Juan Pérez', email='juan@example.com', rol='Técnico', telefono='123456789', perfil=perfil)
orden = OrdenInspeccion.objects.create(numero='OI-001', fecha_generacion=timezone.now(), encargado=emp, estacion=estacion)
print('Orden de inspección creada con id:', orden.id)
