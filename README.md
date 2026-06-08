# Biblioteca IFTS 11 - Trabajo Cuatrimestral

## Descripción

Este proyecto es una aplicación de consola para gestionar una biblioteca.
Permite registrar materiales bibliográficos (libros y revistas), administrar socios,
registrar préstamos y devoluciones, y consultar el estado actual de la biblioteca.

Los datos se almacenan en un archivo JSON dentro de `biblioteca/json/biblioteca_datos.json`.

## Cómo ejecutar

Ejecutar el programa principal:
   - `python biblioteca/main.py`

> Nota: Requiere Python 3.10 o superior para la sintaxis `match/case`.

## Funcionalidades

- Registrar libros y revistas con ID automático.
- Consultar materiales disponibles.
- Buscar materiales por título.
- Identificar el tipo de material por su ID.
- Registrar socios y consultar sus datos.
- Listar socios habilitados para operar.
- Registrar préstamos y devoluciones.
- Listar préstamos activos y vencidos.

## Estructura principal

- `biblioteca/main.py`: menú e interacción con el usuario.
- `biblioteca/biblioteca.py`: lógica principal de la biblioteca.
- `biblioteca/materiales.py`: clases `Material`, `Libro` y `Revista`.
- `biblioteca/socio.py`: clase `Socio`.
- `biblioteca/prestamo.py`: clase `Prestamo`.
- `biblioteca/persistencia.py`: guardado y carga de datos en JSON.

## Autores

- Mauricio Oscar Tófalo
- Gabriel Martinez
