from biblioteca import Biblioteca

# DESDE YA TE DIGO QUE ESTO LO ARMÓ GEMINI

def mostrar_estado_sistema():
    print("==================================================")
    print("      ESTADO ACTUAL DE LA BIBLIOTECA (TESTING)    ")
    print("==================================================")

    # 1. Instanciamos la biblioteca 
    # Al hacer esto, el __init__ ejecuta 'cargar_datos_json()' automáticamente
    mi_biblioteca = Biblioteca("Biblioteca Central IFTS 11")

    # 2. Mostramos los materiales cargados en el sistema
    print("\n>>> Colección de Materiales en Memoria (levantados del JSON):")
    mi_biblioteca.consultar_materiales_disponibles()

    print("\n==================================================")
    print("          FIN DE LA MUESTRA DE DATOS              ")
    print("==================================================")

if __name__ == "__main__":
    mostrar_estado_sistema()