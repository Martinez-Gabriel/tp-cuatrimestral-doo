class Material:
    contador_id = 1

    """Clase (madre)"""
    def __init__(self, titulo, autor):
        self.id_material = Material.contador_id
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  

        Material.contador_id += 1 

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ID: {self.id_material} | Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"

    def to_dict(self):
        return {
            "id_material": self.id_material,
            "titulo": self.titulo,
            "autor": self.autor,
            "disponible": self.disponible
        }

class Libro(Material):
    """Especialización de Material para Libros"""
    def __init__(self, titulo, autor, isbn, num_paginas):
        super().__init__(titulo, autor)
        self.isbn = isbn
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"[LIBRO] {info_base} | ISBN: {self.isbn} | Páginas: {self.num_paginas}"
    
    def to_dict(self):
        d = super().to_dict()
        d["tipo"] = "Libro"
        d["isbn"] = self.isbn
        d["num_paginas"] = self.num_paginas
        return d

class Revista(Material):
    """Especialización de Material para Revistas"""
    def __init__(self, titulo, autor, nro_edicion, fecha_publicacion): 
        super().__init__(titulo, autor)  
        self.nro_edicion = nro_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"[REVISTA] {info_base} | Edición Nro: {self.nro_edicion} | Fecha: {self.fecha_publicacion}"
    
    def to_dict(self):
        d = super().to_dict()
        d["tipo"] = "Revista"
        d["nro_edicion"] = self.nro_edicion
        d["fecha_publicacion"] = self.fecha_publicacion
        return d