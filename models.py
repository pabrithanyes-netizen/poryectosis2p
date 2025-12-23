#CLASE ESTUDIANTES

class Estudiante:
    def __init__(self, id, nombre, edad, cedula):
        self.datos = {
            "id": int(id),
            "nombre": nombre,
            "edad": int(edad),
            "cedula": cedula
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['nombre']}|{d['edad']}|{d['cedula']}"

    @staticmethod
    def from_line(linea):
        partes = linea.strip().split("|")
        return {
            "id": int(partes[0]),
            "nombre": partes[1],
            "edad": int(partes[2]),
            "cedula": partes[3]
        }


#CLASES PROFESORES
class Profesor:
    def __init__(self, id, nombre, especialidad, telefono):
        self.datos = {
            "id": int(id),
            "nombre": nombre,
            "especialidad": especialidad,
            "telefono": telefono
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['nombre']}|{d['especialidad']}|{d['telefono']}"

    @staticmethod
    def from_line(linea):
        partes = linea.strip().split("|")
        return {
            "id": int(partes[0]),
            "nombre": partes[1],
            "especialidad": partes[2],
            "telefono": partes[3]
        }

#CLASE MATERIA
class Materia:
    def __init__(self, id, nombre, creditos, horas):
        self.datos = {
            "id": int(id),
            "nombre": nombre,
            "creditos": int(creditos),
            "horas": int(horas)
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['nombre']}|{d['creditos']}|{d['horas']}"

    @staticmethod
    def from_line(linea):
        partes = linea.strip().split("|")
        return {
            "id": int(partes[0]),
            "nombre": partes[1],
            "creditos": int(partes[2]),
            "horas": int(partes[3])
        }

#CLASE CURSO
class Curso:
    def __init__(self, id, nivel, paralelo):
        self.datos = {
            "id": int(id),
            "nivel": nivel,
            "paralelo": paralelo
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['nivel']}|{d['paralelo']}"

    @staticmethod
    def from_line(linea):
        partes = linea.strip().split("|")
        return {
            "id": int(partes[0]),
            "nivel": partes[1],
            "paralelo": partes[2]
        }

#CLASE MATRICULA CON NOMBRE DE ESTUDIANTE
class Matricula:
    def __init__(self, id, id_estudiante, id_curso, fecha):
        self.datos = {
            "id": int(id),
            "id_estudiante": int(id_estudiante),
            "id_curso": int(id_curso),
            "fecha": fecha
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['id_estudiante']}|{d['id_curso']}|{d['fecha']}"

    @staticmethod
    def from_line(linea):
        partes = linea.strip().split("|")
        return {
            "id": int(partes[0]),
            "id_estudiante": int(partes[1]),
            "id_curso": int(partes[2]),
            "fecha": partes[3]
        }

# CLASE CALIFICACION
class Calificacion:
    def __init__(self, id, id_estudiante, id_materia, id_profesor, nota):
        self.datos = {
            "id": int(id),
            "id_estudiante": int(id_estudiante),
            "id_materia": int(id_materia),
            "id_profesor": int(id_profesor),
            "nota": float(nota),
            "estado": "APROBADO" if float(nota) >= 7 else "REPROBADO"
        }

    def to_line(self):
        d = self.datos
        return f"{d['id']}|{d['id_estudiante']}|{d['id_materia']}|{d['id_profesor']}|{d['nota']}|{d['estado']}"

    @staticmethod
    def from_line(linea):
        p = linea.strip().split("|")
        return {
            "id": int(p[0]),
            "id_estudiante": int(p[1]),
            "id_materia": int(p[2]),
            "id_profesor": int(p[3]),
            "nota": float(p[4]),
            "estado": p[5]
        }

#REPORTE MAESTRO
class ReporteMaestro:
    def __init__(self, estudiante_dict, profesor_dict, materia_dict, curso_dict, nota_dict):
        self.datos = {
            "alumno": estudiante_dict.get("nombre", "N/A"),
            "profesor": profesor_dict.get("nombre", "N/A"),
            "materia": materia_dict.get("nombre", "N/A"),
            "curso": f"{curso_dict.get('nivel', 'N/A')} {curso_dict.get('paralelo', '')}",
            "calificacion": nota_dict.get("nota", 0.0),
            "estado": nota_dict.get("estado", "N/A")
        }

    def imprimir_linea(self):
        d = self.datos
        print(f"{d['alumno']:<18} | {d['profesor']:<15} | {d['materia']:<12} | {d['curso']:<10} | {d['calificacion']:<5} | {d['estado']}")