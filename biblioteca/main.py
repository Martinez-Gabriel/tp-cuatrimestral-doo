from biblioteca import Biblioteca
from materiales import Material, Libro, Revista

def programa_principal():
    mi_biblioteca = Biblioteca("Biblioteca Central IFTS 11")

    while True:
        print("\n==========================================")
        print("          GESTIÓN DE BIBLIOTECA IFTS 11   ")
        print("==========================================")
        print("1. Registrar material bibliográfico")
        print("2. Consultar materiales disponibles")
        print("3. Buscar materiales por distintos criterios")
        print("4. Identificar el tipo de material")
        print("------------------------------------------")
        print("5. Registrar un nuevo Socio")
        print("6. Consultar información de un Socio (por ID)")
        print("7. Listar socios habilitados para operar")
        print("------------------------------------------")
        print("8. Registrar préstamos de materiales")
        print("9. Registrar devoluciones")
        print("10. Listar préstamos activos")
        print("11. Detectar préstamos vencidos")
        print("0. Volver / Salir")
        print("==========================================")
        
        opcion = input("Seleccione una opción: ")
        pausar = True

        match opcion:

            # OPCIÓN 1: REGISTRAR MATERIAL (ID AUTOMÁTICO)
            case "1":
                print("\n[ REGISTRAR MATERIAL BIBLIOGRÁFICO ]")
                print("a. Registrar un Libro")
                print("b. Registrar una Revista")
                sub_opcion = input("👉 Seleccione el tipo de material (a/b): ").lower().strip()

                if sub_opcion not in ["a", "b"]:
                    print("❌ Opción inválida. Cancelando registro.")
                    continue

                titulo = input("👉 Título: ").strip()
                autor = input("👉 Autor: ").strip()

                if not titulo or not autor:
                    print("❌ Error: El título y el autor son obligatorios.")
                    continue

                if sub_opcion == "a":
                    isbn = input("👉 ISBN: ").strip()
                    try:
                        paginas = int(input("👉 Cantidad de páginas: "))
                        nuevo_material = Libro(titulo, autor, isbn, paginas)
                    except ValueError:
                        print("❌ Error: Las páginas deben ser un número entero.")
                        continue
                else:
                    try:
                        nro_edicion = int(input("👉 Número de edición: "))
                    except ValueError:
                        print("❌ Error: El número de edición debe ser un entero.")
                        continue
                    fecha_pub = input("👉 Fecha de publicación (DD/MM/AAAA): ").strip()
                    nuevo_material = Revista(titulo, autor, nro_edicion, fecha_pub)

                mi_biblioteca.registrar_material(nuevo_material)

            # OPCIÓN 2: CONSULTAR DISPONIBLES
            case "2":
                mi_biblioteca.consultar_materiales_disponibles()

            # OPCIÓN 3: BUSCAR POR CRITERIOS (TÍTULO)
            case "3":
                print("\n[ BUSCAR MATERIAL ]")
                criterio = input("👉 Ingrese el título (o parte del título) a buscar: ").strip()
                if criterio:
                    mi_biblioteca.buscar_por_titulo(criterio)
                else:
                    print("❌ Error: Debe ingresar un texto para buscar.")

            # OPCIÓN 4: IDENTIFICAR TIPO DE MATERIAL
            case "4":
                print("\n[ IDENTIFICAR TIPO DE MATERIAL ]")
                try:
                    id_buscar = int(input("👉 Ingrese el ID del material a identificar: "))
                except ValueError:
                    print("❌ Error: El ID debe ser un número entero.")
                    continue

                material_encontrado = mi_biblioteca.buscar_material_por_id(id_buscar)

                if material_encontrado:
                    print(f"El material con ID {id_buscar} es de tipo:")
                    print(f"{material_encontrado.mostrar_informacion()}")
                else:
                    print(f"❌ Error: No existe ningún material con el ID {id_buscar}.")

            # OPCIÓN 5: REGISTRAR SOCIO
            case "5":
                print("\n[ FORMULARIO: REGISTRAR SOCIO ]")
                nombre = input("👉 Ingrese Nombre completo: ")
                dni = input("👉 Ingrese DNI (sin puntos): ")
                domicilio = input("👉 Ingrese Domicilio: ")
                
                if nombre.strip() == "" or dni.strip() == "":
                    print("❌ Error: Nombre y DNI son campos obligatorios.")
                    continue
                
                mi_biblioteca.registrar_socio(nombre, dni, domicilio)

            # OPCIÓN 6: CONSULTAR SOCIO
            case "6":
                print("\n[ CONSULTAR FICHA DE SOCIO ]")
                try:
                    id_buscar = int(input("👉 Ingrese el ID del socio a consultar: "))
                    mi_biblioteca.consultar_informacion_socio(id_buscar)
                except ValueError:
                    print("❌ Error: El ID debe ser un número entero.")

            # OPCIÓN 7: MOSTRAR SOCIOS HABILITADOS
            case "7":
                mi_biblioteca.listar_socios_habilitados()

            # OPCIÓN 8: REGISTRAR PRESTAMOS DE MATERIALES
            case "8":
                print("\n[ REGISTRAR NUEVO PRÉSTAMO ]")
                try:
                    id_socio = int(input("👉 Ingrese el ID del socio: "))
                    id_material = int(input("👉 Ingrese el ID del material a prestar: "))
                except ValueError:
                    print("❌ Error: Los IDs deben ser números enteros.")
                    continue
                
                mi_biblioteca.registrar_prestamo(id_socio, id_material)

            # OPCIÓN: REGISTRAR DEVOLUCIÓN
            case "9":
                print("\n[ REGISTRAR DEVOLUCIÓN ]")
                try:
                    id_material = int(input("👉 Ingrese el ID del material que devuelven: "))
                except ValueError:
                    print("❌ Error: El ID debe ser un número entero.")
                    continue
                    
                mi_biblioteca.registrar_devolucion(id_material)

            # OPCIÓN: LISTAR PRÉSTAMOS ACTIVOS
            case "10":
                mi_biblioteca.listar_prestamos_activos()

            # OPCIÓN: DETECTAR PRÉSTAMOS VENCIDOS
            case "11":
                mi_biblioteca.listar_prestamos_vencidos()

            # OPCIÓN 0: SALIR
            case "0":
                print("\n👋 Saliendo de Gestion de Biblioteca IFTS 11...")
                pausar = False # No pausamos si el usuario ya se quiere ir
                break

            case _:
                print("❌ Opción inválida. Intente de nuevo.")
                pausar = False

        if pausar:
            print("\n------------------------------------------")
            input("Oprima ENTER para continuar...")

if __name__ == "__main__":
    programa_principal()