from materiales import Material, Libro, Revista
from socio import Socio
from prestamo import Prestamo
import persistencia 

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_materiales, self.socios, self.lista_prestamos = persistencia.cargar_todo()
        

        if self.socios:
            Socio.contador_id = max(self.socios.keys()) + 1
            
        if self.lista_materiales:
            Material.contador_id = max(m.id_material for m in self.lista_materiales) + 1
            
        if self.lista_prestamos:
            Prestamo.contador_id = max(p.id_prestamo for p in self.lista_prestamos) + 1

    def _guardar_todo(self):
        persistencia.guardar_todo(self.lista_materiales, self.socios, self.lista_prestamos)

    # SECCIÓN: MATERIALES

    def registrar_material(self, nuevo_material):
        self.lista_materiales.append(nuevo_material)
        print(f"✅ Éxito: Se registró '{nuevo_material.titulo}' con ID automático: {nuevo_material.id_material}")
        self._guardar_todo()

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

    def buscar_material_por_id(self, id_buscar):
        return next((m for m in self.lista_materiales if m.id_material == id_buscar), None)
    
    # SECCIÓN: SOCIOS
    
    def registrar_socio(self, nombre, dni, domicilio):
        nuevo_socio = Socio(nombre, dni, domicilio)
        self.socios[nuevo_socio.id_socio] = nuevo_socio
        print(f"✅ Éxito: Socio registrado. ID asignado automáticamente: {nuevo_socio.id_socio}")
        self._guardar_todo()

    def consultar_informacion_socio(self, id_socio):
        socio_encontrado = self.socios.get(id_socio)
        if socio_encontrado:
            print(socio_encontrado.mostrar_socio())
        else:
            print(f"❌ Error: No se encontró ningún socio registrado con el ID {id_socio}.")

    def listar_socios_habilitados(self):
        """Recorre el diccionario de socios y muestra los que pueden operar"""
        print(f"\n--- Socios Habilitados para Operar ---")
        hay_habilitados = False
        for s in self.socios.values():
            if s.habilitado:
                print(f"ID: {s.id_socio} | Nombre: {s.nombre} | DNI: {s.dni} | Domicilio: {s.domicilio}")
                hay_habilitados = True
        if not hay_habilitados:
            print("No hay socios habilitados en este momento.")