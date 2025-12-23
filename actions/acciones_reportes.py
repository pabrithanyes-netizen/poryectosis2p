import os
from file_manager import FileManagerReporte
from models import ReporteMaestro

def ejecutar_reporte_maestro():
    os.system("cls" if os.name == "nt" else "clear")
    fm = FileManagerReporte()
    fm.obtener_reporte_completo()
    input("Presione Enter para salir...")