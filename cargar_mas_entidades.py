from inspeccion.models import *
from django.utils import timezone
import random

# Obtener datos existentes
empleados = list(Empleado.objects.all())
ordenes = list(OrdenInspeccion.objects.all())
tipos_trabajo = list(TipoTrabajo.objects.all())

# Poblar tareas asignadas para cada orden
for orden in ordenes:
    for _ in range(random.randint(1, 3)):
        empleado = random.choice(empleados)
        tipo_trabajo = random.choice(tipos_trabajo)
        TareaAsignada.objects.get_or_create(
            orden=orden,
            empleado=empleado,
            tipo_trabajo=tipo_trabajo,
            defaults={
                'fecha_inicio': timezone.now(),
                'fecha_fin': None,
                'observaciones': f'Tarea asignada a {empleado.nombre} para {tipo_trabajo.nombre}'
            }
        )

# Poblar muestras sísmicas y detalles
for i in range(1, 11):
    muestra = MuestraSismica.objects.create(
        fecha_hora=timezone.now(),
        serie_temporal=f'[{random.random():.2f}, {random.random():.2f}, {random.random():.2f}]'
    )
    for tipo in TipoDato.objects.all():
        DetalleMuestraSismica.objects.create(
            valor=random.uniform(0.1, 1.0),
            tipo_dato=tipo,
            muestra=muestra
        )

# Poblar reparaciones
for i in range(1, 6):
    Reparacion.objects.get_or_create(
        nro=f'R-{i:03d}',
        defaults={
            'fecha_inicio': timezone.now(),
            'comentarios': f'Reparación de prueba {i}',
            'resolucion': 'Resuelto'
        }
    )

print('Tareas, muestras, detalles y reparaciones de prueba creadas.')
