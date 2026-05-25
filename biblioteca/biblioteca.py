import json
import os  
from materiales import Libro, Revista

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_materiales = []
        self.archivo_datos = "json/biblioteca_datos.json"
        
        # Apenas se crea la biblioteca, intentamos cargar lo que haya guardado
        self.cargar_datos_json()

    def registrar_material(self, nuevo_material):
        self.lista_materiales.append(nuevo_material)
        print(f"Éxito: Se registró '{nuevo_material.titulo}' correctamente.")
        # Al crear algo, actualizamos el JSON
        self.guardar_datos_json()

    def consultar_materiales_disponibles(self):
        print(f"\n--- Materiales Disponibles en: {self.nombre} ---")
        hay_disponibles = False
        for m in self.lista_materiales:
            if m.disponible:
                print(m.mostrar_informacion())
                hay_disponibles = True
        if not hay_disponibles:
            print("No hay materiales disponibles en este momento.")

    def buscar_por_titulo(self, titulo_buscar):
        print(f"\n--- Resultados de búsqueda para: '{titulo_buscar}' ---")
        encontrado = False
        for m in self.lista_materiales:
            if titulo_buscar.lower() in m.titulo.lower():
                print(m.mostrar_informacion())
                encontrado = True
        if not encontrado:
            print("No se encontraron materiales con ese título.")

    
    def guardar_datos_json(self):
        """Convierte la lista de objetos a un formato de diccionario para guardarlo en el archivo JSON"""
        lista_para_guardar = []
        
        for m in self.lista_materiales:
            # diccionario base 
            datos_material = {
                "tipo": m.__class__.__name__,  # tipo de material (Libro o Revista)
                "id_material": m.id_material,
                "titulo": m.titulo,
                "autor": m.autor,
                "disponible": m.disponible
            }
            
            if isinstance(m, Libro):
                datos_material["isbn"] = m.isbn
                datos_material["num_paginas"] = m.num_paginas
            
            elif isinstance(m, Revista):
                datos_material["nro_edicion"] = m.nro_edicion
                datos_material["fecha_publicacion"] = m.fecha_publicacion
                
            lista_para_guardar.append(datos_material)

        # Desde acá, le pedí ayuda a Gemini para escribir el JSON, porque no tengo ni la menor idea de como se hace jajaja
        with open(self.archivo_datos, "w", encoding="utf-8") as f:
            json.dump(lista_para_guardar, f, indent=4, ensure_ascii=False)

    def cargar_datos_json(self):    
        """Lee el archivo JSON (si existe) y crea la carpeta contenedora si hace falta"""
        # Extraemos el nombre de la carpeta de la ruta (ej: "json")
        carpeta = os.path.dirname(self.archivo_datos)
        
        # Si definiste una carpeta y no existe en la compu, la crea automáticamente
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)
            return  # Como la carpeta es nueva, sabemos que está vacía. Cortamos acá.

        # Si la carpeta ya existía pero el archivo todavía no, no hacemos nada
        if not os.path.exists(self.archivo_datos):
            return  

        try:
            with open(self.archivo_datos, "r", encoding="utf-8") as f:
                lista_diccionarios = json.load(f)
                
            for datos in lista_diccionarios:
                # Dependiendo del tipo que guardamos, reconstruimos el objeto correcto
                if datos["tipo"] == "Libro":
                    instancia = Libro(datos["id_material"], datos["titulo"], datos["autor"], datos["isbn"], datos["num_paginas"])
                elif datos["tipo"] == "Revista":
                    instancia = Revista(datos["id_material"], datos["titulo"], datos["autor"], datos["nro_edicion"], datos["fecha_publicacion"])
                
                # Le devolvemos su estado de disponibilidad real
                instancia.disponible = datos["disponible"]
                self.lista_materiales.append(instancia)
                
        except Exception as e:
            print(f"Aviso: No se pudieron cargar los datos previos ({e}).")