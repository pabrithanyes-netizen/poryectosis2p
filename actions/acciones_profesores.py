import os
from file_manager import FileManagerProfesor
from models import Profesor
from menus.menu_profesores import mostrar_menu_profesores

def ejecutar_menu_profesores():
    fm = FileManagerProfesor()
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        mostrar_menu_profesores()
        op = input("Seleccione: ")

        if op == "1":
            for p in fm.get_all():
                print(f"ID: {p['id']} | {p['nombre']} | Especialidad: {p['especialidad']}")
            input("\nPresione Enter...")
        elif op == "2":
            nom = input("Nombre: ")
            esp = input("Especialidad: ")
            tel = input("Teléfono: ")
            fm.insert(nom, esp, tel)
        elif op == "3":
            id_p = int(input("ID a modificar: "))
            nom = input("Nombre: ")
            esp = input("Especialidad: ")
            tel = input("Teléfono: ")
            fm.update(id_p, nom, esp, tel)
        elif op == "4":
            id_p = int(input("ID a eliminar: "))
            fm.delete(id_p)
        elif op == "5":
            break