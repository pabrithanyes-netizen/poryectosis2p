import os
import sys

# Forzamos a Python a reconocer la carpeta actual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    print("Cargando módulos...")
    # Importamos el diseño del menú principal
    from menus.menu_principal import mostrar_menu_principal
    
    # IMPORTANTE: Debemos incluir el nombre de la carpeta 'actions.' antes del archivo
    from actions.acciones_estudiantes import ejecutar_menu_estudiantes
    from actions.acciones_profesores import ejecutar_menu_profesores
    from actions.acciones_materias import ejecutar_menu_materias
    from actions.acciones_cursos import ejecutar_menu_cursos
    from actions.acciones_matriculas import ejecutar_menu_matriculas
    from actions.acciones_notas import ejecutar_menu_notas
    from actions.acciones_reportes import ejecutar_reporte_maestro

    print("Módulos cargados con éxito.")
except Exception as e:
    print(f"ERROR CRÍTICO AL CARGAR MÓDULOS: {e}")
    print("\n[Consejo]: Asegúrate de que los archivos dentro de 'actions' tengan las funciones 'ejecutar_menu_...'")
    input("Presione Enter para salir...")
    exit()

def main():
    while True:
        try:
            # Limpiar pantalla
            os.system("cls" if os.name == "nt" else "clear")
            
            mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                ejecutar_menu_estudiantes()
            elif opcion == "2":
                ejecutar_menu_profesores()
            elif opcion == "3":
                ejecutar_menu_materias()
            elif opcion == "4":
                ejecutar_menu_cursos()
            elif opcion == "5":
                ejecutar_menu_matriculas()
            elif opcion == "6":
                ejecutar_menu_notas()
            elif opcion == "7":
                ejecutar_reporte_maestro()
            elif opcion == "8":
                print("\nSaliendo del SISTEMA DE CONTROL ESCOLAR. ¡Hasta pronto!")
                break
            else:
                print("\n[!] Opción inválida.")
                input("Presione Enter para continuar...")
        except Exception as e:
            print(f"\n[!] Ocurrió un error en el programa: {e}")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()