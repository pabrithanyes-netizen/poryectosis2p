import os
from datetime import datetime
#FILEMANAGER ESTUDIANTES
class FileManagerEstudiante:
    def __init__(self, filename="data/estudiantes.txt", counter_file="data/cont_estudiantes.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            actual = int(f.read().strip() or 0)
        nuevo_id = actual + 1
        with open(self.counter_file, "w") as f:
            f.write(str(nuevo_id))
        return nuevo_id

    def _read_file(self) -> list:
        estudiantes = []
        if not os.path.exists(self.filename): return estudiantes
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    estudiantes.append(Estudiante.from_line(linea))
        return estudiantes

    def _write_file(self, lista_estudiantes: list):
        with open(self.filename, "w") as f:
            for est in lista_estudiantes:
                f.write(f"{est['id']}|{est['nombre']}|{est['edad']}|{est['cedula']}\n")

    def insert(self, nombre: str, edad: int, cedula: str) -> dict:
        nuevo_id = self._get_next_id()
        nuevo_est = {"id": nuevo_id, "nombre": nombre, "edad": edad, "cedula": cedula}
        linea = f"{nuevo_id}|{nombre}|{edad}|{cedula}\n"
        with open(self.filename, "a") as f:
            f.write(linea)
        return nuevo_est

    def update(self, id_est: int, nombre: str, edad: int, cedula: str) -> bool:
        estudiantes = self._read_file()
        encontrado = False
        for est in estudiantes:
            if est['id'] == id_est:
                est['nombre'] = nombre
                est['edad'] = edad
                est['cedula'] = cedula
                encontrado = True
                break
        if encontrado:
            self._write_file(estudiantes)
        return encontrado

    def delete(self, id_est: int) -> bool:
        estudiantes = self._read_file()
        inicial = len(estudiantes)
        estudiantes = [e for e in estudiantes if e['id'] != id_est]
        if len(estudiantes) < inicial:
            self._write_file(estudiantes)
            return True
        return False

    def get_all(self) -> list:
        return self._read_file()

    def _read_file(self) -> list:
        # AGREGA ESTA LÍNEA AQUÍ ABAJO:
        from models import Estudiante 
        
        estudiantes = []
        if not os.path.exists(self.filename): 
            return estudiantes
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    # Ahora sí reconocerá qué es 'Estudiante'
                    estudiantes.append(Estudiante.from_line(linea))
        return estudiantes


#FILEMANAGER PROFESOR
class FileManagerProfesor:
    def __init__(self, filename="data/profesores.txt", counter_file="data/cont_profesores.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            actual = int(f.read().strip() or 0)
        nuevo_id = actual + 1
        with open(self.counter_file, "w") as f:
            f.write(str(nuevo_id))
        return nuevo_id

    def _read_file(self) -> list:
        profesores = []
        if not os.path.exists(self.filename): return profesores
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    profesores.append(Profesor.from_line(linea))
        return profesores

    def _write_file(self, lista_profesores: list):
        with open(self.filename, "w") as f:
            for prof in lista_profesores:
                f.write(f"{prof['id']}|{prof['nombre']}|{prof['especialidad']}|{prof['telefono']}\n")

    def insert(self, nombre: str, especialidad: str, telefono: str) -> dict:
        nuevo_id = self._get_next_id()
        nuevo_prof = {
            "id": nuevo_id, 
            "nombre": nombre, 
            "especialidad": especialidad, 
            "telefono": telefono
        }
        linea = f"{nuevo_id}|{nombre}|{especialidad}|{telefono}\n"
        with open(self.filename, "a") as f:
            f.write(linea)
        return nuevo_prof

    def update(self, id_prof: int, nombre: str, especialidad: str, telefono: str) -> bool:
        profesores = self._read_file()
        encontrado = False
        for prof in profesores:
            if prof['id'] == id_prof:
                prof['nombre'] = nombre
                prof['especialidad'] = especialidad
                prof['telefono'] = telefono
                encontrado = True
                break
        if encontrado:
            self._write_file(profesores)
        return encontrado

    def delete(self, id_prof: int) -> bool:
        profesores = self._read_file()
        inicial = len(profesores)
        profesores = [p for p in profesores if p['id'] != id_prof]
        if len(profesores) < inicial:
            self._write_file(profesores)
            return True
        return False

    def get_all(self) -> list:
        return self._read_file()

    def _read_file(self) -> list:
        # Importamos la clase Profesor desde el archivo models.py
        from models import Profesor 
        
        profesores = []
        if not os.path.exists(self.filename): 
            return profesores
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    # Usamos el método estático de la clase Profesor
                    profesores.append(Profesor.from_line(linea))
        return profesores
        


#FILEMANAGER MATERIA
class FileManagerMateria:
    def __init__(self, filename="data/materias.txt", counter_file="data/cont_materias.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            actual = int(f.read().strip() or 0)
        nuevo_id = actual + 1
        with open(self.counter_file, "w") as f:
            f.write(str(nuevo_id))
        return nuevo_id

    def _read_file(self) -> list:
        materias = []
        if not os.path.exists(self.filename): return materias
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    materias.append(Materia.from_line(linea))
        return materias

    def _write_file(self, lista_materias: list):
        with open(self.filename, "w") as f:
            for mat in lista_materias:
                f.write(f"{mat['id']}|{mat['nombre']}|{mat['creditos']}|{mat['horas']}\n")

    def insert(self, nombre: str, creditos: int, horas: int) -> dict:
        nuevo_id = self._get_next_id()
        nueva_mat = {
            "id": nuevo_id, 
            "nombre": nombre, 
            "creditos": creditos, 
            "horas": horas
        }
        linea = f"{nuevo_id}|{nombre}|{creditos}|{horas}\n"
        with open(self.filename, "a") as f:
            f.write(linea)
        return nueva_mat

    def update(self, id_mat: int, nombre: str, creditos: int, horas: int) -> bool:
        materias = self._read_file()
        encontrado = False
        for mat in materias:
            if mat['id'] == id_mat:
                mat['nombre'] = nombre
                mat['creditos'] = creditos
                mat['horas'] = horas
                encontrado = True
                break
        if encontrado:
            self._write_file(materias)
        return encontrado

    def delete(self, id_mat: int) -> bool:
        materias = self._read_file()
        inicial = len(materias)
        materias = [m for m in materias if m['id'] != id_mat]
        if len(materias) < inicial:
            self._write_file(materias)
            return True
        return False

    def get_all(self) -> list:
        return self._read_file()


    def _read_file(self) -> list:
        # Importamos la clase Materia desde el archivo models.py
        from models import Materia 
        
        materias = []
        if not os.path.exists(self.filename): 
            return materias
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    # Usamos el método de la clase Materia para procesar la línea
                    materias.append(Materia.from_line(linea))
        return materias



#FILEMANAGER CURSO
class FileManagerCurso:
    def __init__(self, filename="data/cursos.txt", counter_file="data/cont_cursos.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            actual = int(f.read().strip() or 0)
        nuevo_id = actual + 1
        with open(self.counter_file, "w") as f:
            f.write(str(nuevo_id))
        return nuevo_id

    def _read_file(self) -> list:
        cursos = []
        if not os.path.exists(self.filename): return cursos
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    cursos.append(Curso.from_line(linea))
        return cursos

    def _write_file(self, lista_cursos: list):
        with open(self.filename, "w") as f:
            for cur in lista_cursos:
                f.write(f"{cur['id']}|{cur['nivel']}|{cur['paralelo']}\n")

    def insert(self, nivel: str, paralelo: str) -> dict:
        nuevo_id = self._get_next_id()
        nuevo_cur = {
            "id": nuevo_id, 
            "nivel": nivel, 
            "paralelo": paralelo
        }
        linea = f"{nuevo_id}|{nivel}|{paralelo}\n"
        with open(self.filename, "a") as f:
            f.write(linea)
        return nuevo_cur

    def update(self, id_cur: int, nivel: str, paralelo: str) -> bool:
        cursos = self._read_file()
        encontrado = False
        for cur in cursos:
            if cur['id'] == id_cur:
                cur['nivel'] = nivel
                cur['paralelo'] = paralelo
                encontrado = True
                break
        if encontrado:
            self._write_file(cursos)
        return encontrado

    def delete(self, id_cur: int) -> bool:
        cursos = self._read_file()
        inicial = len(cursos)
        cursos = [c for c in cursos if c['id'] != id_cur]
        if len(cursos) < inicial:
            self._write_file(cursos)
            return True
        return False

    def get_all(self) -> list:
        return self._read_file()

    def _read_file(self) -> list:
        # Importamos la clase Curso desde el archivo models.py
        from models import Curso 
        
        cursos = []
        if not os.path.exists(self.filename): 
            return cursos
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    # Usamos el método estático de la clase Curso
                    cursos.append(Curso.from_line(linea))
        return cursos


#FILEMANAGER MATRICULA
class FileManagerMatricula:
    def __init__(self, filename="data/matriculas.txt", counter_file="data/cont_matriculas.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            actual = int(f.read().strip() or 0)
        nuevo_id = actual + 1
        with open(self.counter_file, "w") as f:
            f.write(str(nuevo_id))
        return nuevo_id

    def _read_file(self) -> list:
        matriculas = []
        if not os.path.exists(self.filename): return matriculas
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    # Usamos el metodo del modelo para convertir la linea en diccionario
                    matriculas.append(Matricula.from_line(linea))
        return matriculas

    def insert(self, id_estudiante: int, id_curso: int) -> dict:
        nuevo_id = self._get_next_id()
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Punto 3: Se maneja como diccionario
        nueva_mat = {
            "id": nuevo_id,
            "id_estudiante": id_estudiante,
            "id_curso": id_curso,
            "fecha": fecha_actual
        }
        
        linea = f"{nuevo_id}|{id_estudiante}|{id_curso}|{fecha_actual}\n"
        with open(self.filename, "a") as f:
            f.write(linea)
        return nueva_mat

    def get_all(self) -> list:
        return self._read_file()

    def delete(self, id_mat: int) -> bool:
        matriculas = self._read_file()
        inicial = len(matriculas)
        matriculas = [m for m in matriculas if m['id'] != id_mat]
        
        if len(matriculas) < inicial:
            with open(self.filename, "w") as f:
                for m in matriculas:
                    f.write(f"{m['id']}|{m['id_estudiante']}|{m['id_curso']}|{m['fecha']}\n")
            return True
        return False

    def _read_file(self) -> list:
        # Importamos la clase Matricula desde el archivo models.py
        from models import Matricula 
        
        matriculas = []
        if not os.path.exists(self.filename): 
            return matriculas
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    # Usamos el método estático de la clase Matricula
                    matriculas.append(Matricula.from_line(linea))
        return matriculas

#FILEMANAGER CALIFICACION
# file_manager.py

class FileManagerCalificacion:
    def __init__(self, filename="data/calificaciones.txt", counter_file="data/cont_calificaciones.txt"):
        self.filename = filename
        self.counter_file = counter_file
        self._inicializar_archivos()

    def _inicializar_archivos(self):
        import os
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f: f.write("")
        if not os.path.exists(self.counter_file):
            with open(self.counter_file, "w") as f: f.write("0")

    def _get_next_id(self) -> int:
        with open(self.counter_file, "r") as f:
            actual = int(f.read().strip() or 0)
        nuevo_id = actual + 1
        with open(self.counter_file, "w") as f:
            f.write(str(nuevo_id))
        return nuevo_id

    # --- SOLO UNA VERSIÓN DE _READ_FILE CON EL IMPORT ADENTRO ---
    def _read_file(self) -> list:
        import os
        from models import Calificacion 
        
        notas = []
        if not os.path.exists(self.filename): 
            return notas
        
        with open(self.filename, "r") as f:
            for linea in f:
                if linea.strip():
                    # Aquí ya reconocerá Calificacion porque la importamos arriba
                    notas.append(Calificacion.from_line(linea))
        return notas

    def insert(self, id_est, id_mat, id_prof, nota_val) -> dict:
        from models import Calificacion
        nuevo_id = self._get_next_id()
        
        # Se crea el objeto para usar la logica del "estado" automatico
        obj = Calificacion(nuevo_id, id_est, id_mat, id_prof, nota_val)
        
        linea = obj.to_line() + "\n"
        with open(self.filename, "a") as f:
            f.write(linea)
        return obj.datos

    def get_all(self) -> list:
        return self._read_file()

    def update(self, id_cal, nueva_nota) -> bool:
        from models import Calificacion
        notas = self._read_file() 
        encontrado = False
        
        for n in notas:
            if n['id'] == id_cal:
                # Re-instanciamos para recalcular APROBADO/REPROBADO
                obj = Calificacion(n['id'], n['id_estudiante'], n['id_materia'], n['id_profesor'], nueva_nota)
                n.update(obj.datos)
                encontrado = True
                break
        
        if encontrado:
            with open(self.filename, "w") as f:
                for n in notas:
                    # Usamos el formato del modelo para guardar
                    f.write(f"{n['id']}|{n['id_estudiante']}|{n['id_materia']}|{n['id_profesor']}|{n['nota']}|{n['estado']}\n")
        return encontrado

#FILEMANAGER MAESTRO
class FileManagerReporte:
    def __init__(self):
        # Usamos las clases definidas arriba en este mismo archivo
        self.fm_est = FileManagerEstudiante()
        self.fm_prof = FileManagerProfesor()
        self.fm_mat = FileManagerMateria()
        self.fm_cur = FileManagerCurso()
        self.fm_not = FileManagerCalificacion()
        self.fm_matri = FileManagerMatricula()

    def obtener_reporte_completo(self):
        from models import ReporteMaestro
        notas = self.fm_not.get_all()
        estudiantes = self.fm_est.get_all()
        profesores = self.fm_prof.get_all()
        materias = self.fm_mat.get_all()
        cursos = self.fm_cur.get_all()
        matriculas = self.fm_matri.get_all()

        if not notas:
            print("\n>>> No hay calificaciones registradas para generar el reporte.")
            return

        print("\n" + "="*85)
        print(f"{'ESTUDIANTE':<18} | {'PROFESOR':<15} | {'MATERIA':<12} | {'CURSO':<10} | {'NOTA':<5} | {'ESTADO'}")
        print("-" * 85)

        for n in notas:
            est = next((e for e in estudiantes if e['id'] == n['id_estudiante']), {})
            mat = next((m for m in materias if m['id'] == n['id_materia']), {})
            prof = next((p for p in profesores if p['id'] == n['id_profesor']), {})
            m_alumno = next((ma for ma in matriculas if ma['id_estudiante'] == n['id_estudiante']), {})
            cur = next((c for c in cursos if c['id'] == m_alumno.get('id_curso')), {})

            fila = ReporteMaestro(est, prof, mat, cur, n)
            fila.imprimir_linea()
        
        print("="*85 + "\n")