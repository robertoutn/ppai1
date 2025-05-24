from inspeccion.models import *
from django.utils import timezone

# Eliminar datos previos para evitar duplicados
Fabricante.objects.all().delete()
ModeloSismografo.objects.all().delete()
EstacionSismologica.objects.all().delete()
Sismografo.objects.all().delete()
Permiso.objects.all().delete()
Perfil.objects.all().delete()
Empleado.objects.all().delete()
TipoTrabajo.objects.all().delete()
OrdenInspeccion.objects.all().delete()
TareaAsignada.objects.all().delete()
TipoDato.objects.all().delete()
MuestraSismica.objects.all().delete()
DetalleMuestraSismica.objects.all().delete()
ClasificacionSismo.objects.all().delete()
Reparacion.objects.all().delete()

# Fabricantes
fab1 = Fabricante.objects.create(razon_social='SismoTech')
fab2 = Fabricante.objects.create(razon_social='GeoWave')

# Modelos de Sismógrafo
modelo1 = ModeloSismografo.objects.create(nombre='ST-1000', caracteristicas='Alta sensibilidad', fabricante=fab1)
modelo2 = ModeloSismografo.objects.create(nombre='GW-200', caracteristicas='Portátil', fabricante=fab2)

# Estaciones Sismológicas
estacion1 = EstacionSismologica.objects.create(codigo='ES001', nombre='Estación Central', latitud=-34.6, longitud=-58.4)
estacion2 = EstacionSismologica.objects.create(codigo='ES002', nombre='Estación Norte', latitud=-34.5, longitud=-58.3)

# Sismógrafos
sismografo1 = Sismografo.objects.create(identificador='SG-001', modelo=modelo1, estacion=estacion1)
sismografo2 = Sismografo.objects.create(identificador='SG-002', modelo=modelo2, estacion=estacion2)

# Perfiles y Permisos
permiso1 = Permiso.objects.create(nombre='Ver órdenes', clave='ver_orden')
permiso2 = Permiso.objects.create(nombre='Cerrar órdenes', clave='cerrar_orden')
perfil1 = Perfil.objects.create(nombre='Técnico', descripcion='Perfil técnico')
perfil2 = Perfil.objects.create(nombre='Supervisor', descripcion='Perfil supervisor')
perfil1.permisos.add(permiso1, permiso2)
perfil2.permisos.add(permiso1)

# Empleados
emp1 = Empleado.objects.create(nombre='Juan Pérez', email='juan@example.com', rol='Técnico', telefono='123456789', perfil=perfil1)
emp2 = Empleado.objects.create(nombre='Ana Gómez', email='ana@example.com', rol='Supervisor', telefono='987654321', perfil=perfil2)

# Tipos de Trabajo
tipo1 = TipoTrabajo.objects.create(codigo='TT01', descripcion='Monitoreo del área', nombre='Monitoreo')
tipo2 = TipoTrabajo.objects.create(codigo='TT02', descripcion='Calibración de equipos', nombre='Calibración')

# Órdenes de Inspección
orden1 = OrdenInspeccion.objects.create(numero='OI-001', fecha_generacion=timezone.now(), encargado=emp1, estacion=estacion1)
orden2 = OrdenInspeccion.objects.create(numero='OI-002', fecha_generacion=timezone.now(), encargado=emp2, estacion=estacion2)

# Tareas Asignadas
TareaAsignada.objects.create(fecha_inicio=timezone.now(), fecha_fin=None, observaciones='Revisar sensores', empleado=emp1, tipo_trabajo=tipo1, orden=orden1)
TareaAsignada.objects.create(fecha_inicio=timezone.now(), fecha_fin=None, observaciones='Calibrar sismógrafo', empleado=emp2, tipo_trabajo=tipo2, orden=orden2)

# Tipos de Dato
tipo_dato1 = TipoDato.objects.create(denominacion='Aceleración', unidad_medida='g', valor_umbral=0.5)
tipo_dato2 = TipoDato.objects.create(denominacion='Velocidad', unidad_medida='cm/s', valor_umbral=10)

# Muestras Sísmicas
muestra1 = MuestraSismica.objects.create(fecha_hora=timezone.now(), serie_temporal='[0.1, 0.2, 0.3]')
muestra2 = MuestraSismica.objects.create(fecha_hora=timezone.now(), serie_temporal='[0.4, 0.5, 0.6]')

# Detalles de Muestra
DetalleMuestraSismica.objects.create(valor=0.12, tipo_dato=tipo_dato1, muestra=muestra1)
DetalleMuestraSismica.objects.create(valor=0.45, tipo_dato=tipo_dato2, muestra=muestra2)

# Clasificación de Sismo
ClasificacionSismo.objects.create(profundidad_desde=0, profundidad_hasta=70, magnitud=5.5, origen='Tectónico', alcance='Local')
ClasificacionSismo.objects.create(profundidad_desde=71, profundidad_hasta=300, magnitud=6.2, origen='Volcánico', alcance='Regional')

# Reparaciones
Reparacion.objects.create(nro='R-001', fecha_inicio=timezone.now(), comentarios='Cambio de sensor', resolucion='Sensor reemplazado')
Reparacion.objects.create(nro='R-002', fecha_inicio=timezone.now(), comentarios='Ajuste de calibración', resolucion='Calibración ajustada')

print('Datos de prueba cargados correctamente.')
