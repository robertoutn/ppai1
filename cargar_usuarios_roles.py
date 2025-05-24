from django.contrib.auth.models import User, Group
from inspeccion.models import Perfil, Permiso, Empleado

# Crear grupos (roles) estándar
roles = [
    'Analista en sismos',
    'Supervisor',
    'Técnico de mantenimiento',
    'Administrador',
]
for rol in roles:
    Group.objects.get_or_create(name=rol)

# Crear permisos personalizados
permiso_ver = Permiso.objects.get_or_create(nombre='Ver órdenes', clave='ver_orden')[0]
permiso_cerrar = Permiso.objects.get_or_create(nombre='Cerrar órdenes', clave='cerrar_orden')[0]

# Crear perfiles y asociar permisos
perfil_analista, _ = Perfil.objects.get_or_create(nombre='Analista en sismos', descripcion='Analiza eventos sísmicos')
perfil_analista.permisos.set([permiso_ver])
perfil_supervisor, _ = Perfil.objects.get_or_create(nombre='Supervisor', descripcion='Supervisa el sistema')
perfil_supervisor.permisos.set([permiso_ver, permiso_cerrar])
perfil_tecnico, _ = Perfil.objects.get_or_create(nombre='Técnico de mantenimiento', descripcion='Realiza tareas técnicas')
perfil_tecnico.permisos.set([permiso_ver, permiso_cerrar])
perfil_admin, _ = Perfil.objects.get_or_create(nombre='Administrador', descripcion='Administra el sistema')
perfil_admin.permisos.set([permiso_ver, permiso_cerrar])

# Crear usuarios Django y empleados vinculados a perfiles y grupos
usuarios = [
    {'username': 'analista', 'email': 'analista@example.com', 'password': 'analista123', 'first_name': 'Ana', 'last_name': 'Lista', 'perfil': perfil_analista, 'rol': 'Analista en sismos', 'group': 'Analista en sismos'},
    {'username': 'supervisor', 'email': 'supervisor@example.com', 'password': 'supervisor123', 'first_name': 'Susi', 'last_name': 'Pervisora', 'perfil': perfil_supervisor, 'rol': 'Supervisor', 'group': 'Supervisor'},
    {'username': 'tecnico', 'email': 'tecnico@example.com', 'password': 'tecnico123', 'first_name': 'Tino', 'last_name': 'Tecnico', 'perfil': perfil_tecnico, 'rol': 'Técnico de mantenimiento', 'group': 'Técnico de mantenimiento'},
    {'username': 'admin', 'email': 'admin@example.com', 'password': 'admin123', 'first_name': 'Admi', 'last_name': 'Nistrador', 'perfil': perfil_admin, 'rol': 'Administrador', 'group': 'Administrador'},
]
for u in usuarios:
    user, created = User.objects.get_or_create(username=u['username'], defaults={
        'email': u['email'],
        'first_name': u['first_name'],
        'last_name': u['last_name'],
    })
    if created:
        user.set_password(u['password'])
        user.save()
    group = Group.objects.get(name=u['group'])
    user.groups.add(group)
    Empleado.objects.get_or_create(
        nombre=f"{u['first_name']} {u['last_name']}",
        email=u['email'],
        rol=u['rol'],
        telefono='123456789',
        perfil=u['perfil']
    )

# Crear más usuarios de ejemplo
for i in range(5, 21):
    username = f"usuario{i}"
    email = f"usuario{i}@example.com"
    first_name = f"Usuario{i}"
    last_name = f"Apellido{i}"
    perfil = perfil_analista if i % 4 == 1 else perfil_supervisor if i % 4 == 2 else perfil_tecnico if i % 4 == 3 else perfil_admin
    rol = perfil.nombre
    group = Group.objects.get(name=rol)
    user, created = User.objects.get_or_create(username=username, defaults={
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
    })
    if created:
        user.set_password('usuario123')
        user.save()
    user.groups.add(group)
    Empleado.objects.get_or_create(
        nombre=f"{first_name} {last_name}",
        email=email,
        rol=rol,
        telefono='555555555',
        perfil=perfil
    )

print('Usuarios, roles, grupos y empleados creados correctamente.')
