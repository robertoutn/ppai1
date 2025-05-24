class EstacionSismologica:
    def __init__(self, codigo, nombre, latitud, longitud, fecha_cert_adm, fecha_cert_op, nro_cert_adq):
        self.codigo = codigo
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.fecha_cert_adm = fecha_cert_adm
        self.fecha_cert_op = fecha_cert_op
        self.nro_cert_adq = nro_cert_adq
        self.sismografos = []
        self.reparaciones = []
        self.planes_construccion = []
        self.ordenes_inspeccion = []