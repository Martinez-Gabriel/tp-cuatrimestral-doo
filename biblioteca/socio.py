class Socio:
    contador_id = 1

    def __init__(self, nombre, dni, domicilio):
        self.id_socio = Socio.contador_id
        self.nombre = nombre
        self.dni = dni
        self.domicilio = domicilio
        self.materiales_prestados = [] 
        self.habilitado = True

        Socio.contador_id += 1

    def mostrar_socio(self):
        estado = "Habilitado" if self.habilitado else "Inhabilitado"
        
        if self.materiales_prestados:
            lista_visible = "\n".join([f"  - {m.mostrar_informacion()}" for m in self.materiales_prestados])
        else:
            lista_visible = "  (Ninguno)"

        return (
            f"----------------------------------------\n"
            f"=== DATOS DEL SOCIO (ID: {self.id_socio})\n"
            f"----------------------------------------\n"
            f"Nombre: {self.nombre} | Dni: {self.dni} | Domicilio: {self.domicilio} | Estado: [{estado}]\n"
            f"Materiales prestados:\n{lista_visible}\n"
            f"======================="
        )
    
    def to_dict(self):
        return {
            "id_socio": self.id_socio,
            "nombre": self.nombre,
            "dni": self.dni,
            "domicilio": self.domicilio,
            "habilitado": self.habilitado,
            
            # Guardamos solo los IDs de los libros que tiene bajo su brazo
            "materiales_prestados": [m.id_material for m in self.materiales_prestados]
        }