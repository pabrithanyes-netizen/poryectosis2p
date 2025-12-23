import os
from file_manager import FileManagerMateria
from models import Materia
from menus.menu_materias import mostrar_menu_materias

def ejecutar_menu_materias():
    fm = FileManagerMateria()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_materias()
        op = input("Seleccione: ")

        if op == "1":
            for m in fm.get_all():
                print(f"ID: {m['id']} | {m['nombre']} | Créditos: {m['creditos']}")
            input("\nPresione Enter...")
        elif op == "2":
            nom = input("Nombre Materia: ")
            cre = int(input("Créditos: "))
            hrs = int(input("Horas: "))
            fm.insert(nom, cre, hrs)
        elif op == "3":
            id_m = int(input("ID a editar: "))
            nom = input("Nombre: ")
            cre = int(input("Créditos: "))
            hrs = int(input("Horas: "))
            fm.update(id_m, nom, cre, hrs)
        elif op == "4":
            id_m = int(input("ID a eliminar: "))
            fm.delete(id_m)
        elif op == "5":
            break