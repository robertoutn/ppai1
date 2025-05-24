class Empleado:
    def __init__(self, nombre, email, rol, telefono, perfil):
        self.nombre = nombre
        self.email = email
        self.rol = rol
        self.telefono = telefono
        self.perfil = perfil
        self.tareas = []
        self.inspecciones = []
        self.suscripciones = []