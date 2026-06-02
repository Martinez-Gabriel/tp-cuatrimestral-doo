from datetime import datetime, timedelta

class Prestamo:
    contador_id = 1

    def __init__(self, socio, material):
        self.id_prestamo = Prestamo.contador_id
        self.socio = socio           
        self.material = material
        self.fecha_prestamo = datetime.now()
        self.fecha_limite = self.fecha_prestamo + timedelta(days=15)
        self.fecha_devolucion = None   

        Prestamo.contador_id += 1

    def registrar_devolucion(self):
        self.fecha_devolucion = datetime.now()

    def esta_vencido(self):
        if self.fecha_devolucion is None:
            return datetime.now() > self.fecha_limite        
        return False

    def mostrar_prestamo(self):
        formato_fecha = "%d/%m/%Y %H:%M"
        f_prestamo = self.fecha_prestamo.strftime(formato_fecha)
        f_limite = self.fecha_limite.strftime(formato_fecha)
        
        if self.fecha_devolucion:
            f_devolucion = self.fecha_devolucion.strftime(formato_fecha)
            estado = "DEVUELTO"
        else:
            f_devolucion = "PENDIENTE"
            estado = "VENCIDO" if self.esta_vencido() else "ACTIVO (EN PLAZO)"

        return (
            f"----------------------------------------\n"
            f"DETALLE DEL PRÉSTAMO (ID: {self.id_prestamo})\n"
            f"----------------------------------------\n"
            f"Socio: {self.socio.nombre} (ID: {self.socio.id_socio})\n"
            f"Material: '{self.material.titulo}' (ID: {self.material.id_material})\n"
            f"Fecha Retiro: {f_prestamo}\n"
            f"Fecha Límite: {f_limite}\n"
            f"Devolución:   {f_devolucion}\n"
            f"Estado:       {estado}\n"
            f"----------------------------------------"
        )