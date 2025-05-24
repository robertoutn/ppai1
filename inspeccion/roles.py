# Roles identificados en los documentos:
# - Analista en sismos
# - Supervisor
# - Técnico de mantenimiento
# - Administrador
#
# Se recomienda crear grupos de Django para estos roles y asignar permisos según corresponda.
#
# Ejemplo de script para crear los grupos automáticamente:

from django.contrib.auth.models import Group

def crear_roles():
    roles = [
        'Analista en sismos',
        'Supervisor',
        'Técnico de mantenimiento',
        'Administrador',
    ]
    for rol in roles:
        Group.objects.get_or_create(name=rol)

# Puedes ejecutar este código en un archivo de migración o en el shell de Django.
