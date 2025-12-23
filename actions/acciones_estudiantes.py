import os
from menus.menu_estudiantes import mostrar_menu_estudiantes
from file_manager import FileManagerEstudiante

def ejecutar_menu_estudiantes():
    fm = FileManagerEstudiante()
    
    # Este bucle 'while' es el que evita que el menú desaparezca
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        mostrar_menu_estudiantes() # Muestra tus prints
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            estudiantes = fm.get_all()
            print("\n--- LISTA DE ESTUDIANTES ---")
            if not estudiantes:
                print("No hay registros.")
            for e in estudiantes:
                print(f"ID: {e['id']} | Nombre: {e['nombre']} | Cédula: {e['cedula']}")
            input("\nPresione Enter para volver al submenú...")
            
        elif opcion == "2":
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            cedula = input("Cédula: ")
            fm.insert(nombre, int(edad), cedula)
            print("\n[!] Estudiante registrado con éxito.")
            input("Presione Enter para continuar...")
            
        elif opcion == "5":
            # Al dar 'break', salimos del bucle y RECIÉN AHÍ regresamos al main
            break 
        
        else:
            print("\n[!] Opción no válida.")
            input("Presione Enter para intentar de nuevo...")