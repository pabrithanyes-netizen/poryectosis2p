import os
from file_manager import FileManagerCalificacion
from menus.menu_notas import mostrar_menu_notas
# Quitamos el import de Calificacion de aquí para evitar conflictos circulares

def ejecutar_menu_notas():
    fm = FileManagerCalificacion()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_notas()
        op = input("Seleccione: ")

        if op == "1":
            notas = fm.get_all()
            print("\n--- LISTADO DE CALIFICACIONES ---")
            if not notas:
                print("No hay notas registradas.")
            for n in notas:
                # Usamos los nombres de llaves exactos que definiste en el modelo
                print(f"ID: {n['id']} | Est: {n['id_estudiante']} | Nota: {n['nota']} | Estado: {n['estado']}")
            input("\nPresione Enter para continuar...")

        elif op == "2":
            try:
                id_e = int(input("ID Estudiante: "))
                id_m = int(input("ID Materia: "))
                id_p = int(input("ID Profesor: "))
                val = float(input("Nota (0-20): "))
                
                fm.insert(id_e, id_m, id_p, val)
                print("\n[!] Nota registrada exitosamente.")
            except ValueError:
                print("\n[!] Error: Ingrese solo números.")
            input("Presione Enter para continuar...")

        elif op == "3":
            try:
                id_n = int(input("ID Calificación a corregir: "))
                val = float(input("Nueva Nota: "))
                if fm.update(id_n, val):
                    print("\n[!] Nota actualizada.")
                else:
                    print("\n[!] No se encontró el ID.")
            except ValueError:
                print("\n[!] Datos inválidos.")
            input("Presione Enter para continuar...")

        elif op == "4":
            break