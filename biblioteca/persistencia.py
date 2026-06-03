import json
import os
from datetime import datetime
from materiales import Libro, Revista
from socio import Socio
from prestamo import Prestamo

ARCHIVO_DB = "json/biblioteca_datos.json"

def guardar_todo(lista_materiales, diccionario_socios, lista_prestamos):
    """Guarda todo delegando el desarme en el método .to_dict() de cada objeto."""
    carpeta = os.path.dirname(ARCHIVO_DB)
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta)

    data_final = {
        "materiales": [m.to_dict() for m in lista_materiales],
        "socios": [s.to_dict() for s in diccionario_socios.values()],
        "prestamos": [p.to_dict() for p in lista_prestamos]
    }

    with open(ARCHIVO_DB, "w", encoding="utf-8") as f:
        json.dump(data_final, f, indent=4, ensure_ascii=False)


def cargar_todo():
    """Lee el JSON y reconstruye las entidades cruzando los IDs."""
    if not os.path.exists(ARCHIVO_DB):
        return [], {}, []

    try:
        with open(ARCHIVO_DB, "r", encoding="utf-8") as f:
            data = json.load(f)

        # --------------------------------------------------
        # A. RECONSTRUIR MATERIALES (Ajustado a ID automático)
        # --------------------------------------------------
        materiales = []
        for d in data.get("materiales", []):
            if d["tipo"] == "Libro":
                instancia = Libro(d["titulo"], d["autor"], d["isbn"], d["num_paginas"])
            else:
                instancia = Revista(d["titulo"], d["autor"], d["nro_edicion"], d["fecha_publicacion"])
            
            instancia.id_material = d["id_material"]
            instancia.disponible = d["disponible"]
            materiales.append(instancia)

        # --------------------------------------------------
        # B. RECONSTRUIR SOCIOS
        # --------------------------------------------------
        socios = {}
        for d in data.get("socios", []):
            socio_obj = Socio(d["nombre"], d["dni"], d["domicilio"])
            socio_obj.id_socio = d["id_socio"]
            socio_obj.habilitado = d["habilitado"]
            socios[socio_obj.id_socio] = socio_obj

        for d_socio_viejo in data.get("socios", []):
            socio_actual = socios[d_socio_viejo["id_socio"]]
            for id_mat in d_socio_viejo.get("materiales_prestados", []):
                mat_real = next((m for m in materiales if m.id_material == id_mat), None)
                if mat_real:
                    socio_actual.materiales_prestados.append(mat_real)

        # --------------------------------------------------
        # C. RECONSTRUIR PRÉSTAMOS
        # --------------------------------------------------
        prestamos = []
        for d_pres in data.get("prestamos", []):
            socio_vinculado = socios.get(d_pres["id_socio"])
            material_vinculado = next((m for m in materiales if m.id_material == d_pres["id_material"]), None)
            
            if socio_vinculado and material_vinculado:
                # Se crea el préstamo pasando los objetos de memoria vinculados
                prestamo_obj = Prestamo(socio_vinculado, material_vinculado)
                prestamo_obj.id_prestamo = d_pres["id_prestamo"]
                prestamo_obj.fecha_prestamo = datetime.fromisoformat(d_pres["fecha_prestamo"])
                prestamo_obj.fecha_limite = datetime.fromisoformat(d_pres["fecha_limite"])
                if d_pres["fecha_devolucion"]:
                    prestamo_obj.fecha_devolucion = datetime.fromisoformat(d_pres["fecha_devolucion"])
                
                prestamos.append(prestamo_obj)

        return materiales, socios, prestamos

    except Exception as e:
        print(f"⚠️ Error crítico al cargar base de datos: {e}")
        return [], {}, []