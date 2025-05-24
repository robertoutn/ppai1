class OrdenInspeccion:
    def __init__(self, numero, fecha_generacion, fecha_inicio, fecha_cierre, observaciones, encargado):
        self.numero = numero
        self.fecha_generacion = fecha_generacion
        self.fecha_inicio = fecha_inicio
        self.fecha_cierre = fecha_cierre
        self.observaciones = observaciones
        self.encargado = encargado
        self.tareas = []