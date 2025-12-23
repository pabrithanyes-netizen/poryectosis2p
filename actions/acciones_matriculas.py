import os
from file_manager import FileManagerMatricula
from models import Matricula
from menus.menu_notas import mostrar_menu_notas # O el menu que corresponda

def ejecutar_menu_matriculas():
    fm = FileManagerMatricula()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("--- MATRICULACIÓN ---")
        print("1. Ver Inscritos\n2. Matricular Estudiante\n3. Eliminar Matrícula\n4. Volver")
        op = input("Opción: ")

        if op == "1":
            for m in fm.get_all():
                print(f"ID Mat: {m['id']} | Estudiante ID: {m['id_estudiante']} | Curso ID: {m['id_curso']}")
            input("\nContinuar...")
        elif op == "2":
            id_e = int(input("ID Estudiante: "))
            id_c = int(input("ID Curso: "))
            fm.insert(id_e, id_c)
        elif op == "3":
            id_m = int(input("ID Matrícula a eliminar: "))
            fm.delete(id_m)
        elif op == "4":
            break