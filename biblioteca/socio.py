class Socio:
    def __init__(self, id_socio, nombre, dni, domicilio):
        self.id_socio = id_socio
        self.nombre = nombre
        self.dni = dni
        self.domicilio = domicilio
        self.materiales_prestados = [] 
        self.habilitado = True

    def mostrar_socio(self):
        estado = "Habilitado" if self.habilitado else "Inhabilitado"
        
        if self.materiales_prestados:
            lista_visible = "\n".join([f"  - {m.mostrar_informacion()}" for m in self.materiales_prestados])
        else:
            lista_visible = "  (Ninguno)"

        return (
            f"=== DATOS DEL SOCIO ===\n"
            f"ID: {self.id_socio} | Nombre: {self.nombre} | Estado: [{estado}]\n"
            f"Materiales prestados:\n{lista_visible}\n"
            f"======================="
        )