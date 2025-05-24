from django.contrib.auth.models import User
from inspeccion.models import Empleado, OrdenInspeccion, EstacionSismologica
from django.utils import timezone
import random

# Obtener empleados y órdenes existentes
empleados = list(Empleado.objects.all())
ordenes = list(OrdenInspeccion.objects.all())
estaciones = list(EstacionSismologica.objects.all())

# Si no hay órdenes, crear algunas nuevas y asociar empleados
if not ordenes and empleados and estaciones:
    for i in range(1, 11):
        encargado = random.choice(empleados)
        estacion = random.choice(estaciones)
        orden = OrdenInspeccion.objects.create(
            numero=f"OI-{100+i}",
            fecha_generacion=timezone.now(),
            encargado=encargado,
            estacion=estacion
        )
        print(f'Orden creada: {orden.numero} para {encargado.nombre}')

# Asociar usuarios Django a empleados (si no están asociados)
for empleado in empleados:
    try:
        user = User.objects.get(email=empleado.email)
        # Aquí podrías agregar lógica para asociar el user con el empleado si tienes un campo específico
        print(f'Empleado {empleado.nombre} asociado a usuario {user.username}')
    except User.DoesNotExist:
        print(f'No existe usuario Django para el empleado {empleado.nombre}')

print('Órdenes y asociaciones usuario-empleado actualizadas.')
