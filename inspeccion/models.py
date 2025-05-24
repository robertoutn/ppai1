from django.db import models

class Fabricante(models.Model):
    razon_social = models.CharField(max_length=255)

class ModeloSismografo(models.Model):
    nombre = models.CharField(max_length=100)
    caracteristicas = models.TextField()
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)

class EstacionSismologica(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    fecha_cert_adm = models.DateField(null=True, blank=True)
    fecha_cert_op = models.DateField(null=True, blank=True)
    nro_cert_adq = models.CharField(max_length=50, null=True, blank=True)

class Sismografo(models.Model):
    identificador = models.CharField(max_length=50, unique=True)
    modelo = models.ForeignKey(ModeloSismografo, on_delete=models.CASCADE)
    estado_actual = models.CharField(max_length=50, null=True, blank=True)
    estacion = models.ForeignKey(EstacionSismologica, on_delete=models.SET_NULL, null=True, blank=True)

class Perfil(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    permisos = models.ManyToManyField('Permiso', blank=True)

class Permiso(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=50)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    rol = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    perfil = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True, blank=True)

class TipoTrabajo(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.TextField()
    nombre = models.CharField(max_length=100)

class OrdenInspeccion(models.Model):
    numero = models.CharField(max_length=20, unique=True)
    fecha_generacion = models.DateField()
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_cierre = models.DateField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    encargado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    estacion = models.ForeignKey(EstacionSismologica, on_delete=models.CASCADE, related_name='ordenes_inspeccion')

class TareaAsignada(models.Model):
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_fin = models.DateTimeField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_trabajo = models.ForeignKey(TipoTrabajo, on_delete=models.SET_NULL, null=True, blank=True)
    orden = models.ForeignKey(OrdenInspeccion, on_delete=models.CASCADE, related_name='tareas')

class MuestraSismica(models.Model):
    fecha_hora = models.DateTimeField()
    serie_temporal = models.TextField()

class TipoDato(models.Model):
    denominacion = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=50)
    valor_umbral = models.FloatField(null=True, blank=True)

class DetalleMuestraSismica(models.Model):
    valor = models.FloatField()
    tipo_dato = models.ForeignKey(TipoDato, on_delete=models.CASCADE)
    muestra = models.ForeignKey(MuestraSismica, on_delete=models.CASCADE, related_name='detalles')

class ClasificacionSismo(models.Model):
    profundidad_desde = models.FloatField()
    profundidad_hasta = models.FloatField()
    magnitud = models.FloatField()
    origen = models.CharField(max_length=100)
    alcance = models.CharField(max_length=100)

class Reparacion(models.Model):
    nro = models.CharField(max_length=20)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)
    resolucion = models.TextField(null=True, blank=True)
    # reclamo: relación a definir si existe modelo de reclamo

# Puedes agregar relaciones adicionales según los modelos faltantes o detalles del dominio.
