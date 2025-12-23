import os
from file_manager import FileManagerCurso
from models import Curso
from menus.menu_cursos import mostrar_menu_cursos

def ejecutar_menu_cursos():
    fm = FileManagerCurso()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_cursos()
        op = input("Seleccione: ")

        if op == "1":
            for c in fm.get_all():
                print(f"ID: {c['id']} | Nivel: {c['nivel']} | Paralelo: {c['paralelo']}")
            input("\nPresione Enter...")
        elif op == "2":
            niv = input("Nivel: ")
            par = input("Paralelo: ")
            fm.insert(niv, par)
        elif op == "3":
            id_c = int(input("ID a editar: "))
            niv = input("Nivel: ")
            par = input("Paralelo: ")
            fm.update(id_c, niv, par)
        elif op == "4":
            break