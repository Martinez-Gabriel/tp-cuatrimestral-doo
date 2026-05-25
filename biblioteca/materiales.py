class Material:
    """Clase (madre)"""
    def __init__(self, id_material, titulo, autor):
        self.id_material = id_material
        self.titulo = titulo
        self.autor = autor
        self.disponible = True  # si te parece, lo arrancamos por defecto así, y despues le damos cambio de estado cuando se preste o se devuelva el material

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"ID: {self.id_material} | Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}"


class Libro(Material):
    """Especialización de Material para Libros"""
    def __init__(self, id_material, titulo, autor, isbn, num_paginas):
        super().__init__(id_material, titulo, autor)  # Llamamo al constructor de Material
        self.isbn = isbn
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"[LIBRO] {info_base} | ISBN: {self.isbn} | Páginas: {self.num_paginas}"


class Revista(Material):
    """Especialización de Material para Revistas"""
    def __init__(self, id_material, titulo, autor, nro_edicion, fecha_publicacion):
        super().__init__(id_material, titulo, autor)  # volvemo a llamar al constructor
        self.nro_edicion = nro_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"[REVISTA] {info_base} | Edición Nro: {self.nro_edicion} | Fecha: {self.fecha_publicacion}"