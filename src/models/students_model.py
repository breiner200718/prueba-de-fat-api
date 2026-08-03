import json
import os
DATABASE_FILE = os.path.join(os.path.dirname(__file__),"..","..","data","students.json")
students = []

def load_data():
    """Carga los datos de estudiantes desde un archivo JSON."""
    global students
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r", encoding="utf-8") as file:
            students = json.load(file)
            try:
                students = json.load(file)
            except json.JSONDecodeError:
                students = []
    else:
        students = []

def save_data():
    """Guarda los datos de estudiantes en un archivo JSON."""
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


def get_all():
    """Obtiene todos los estudiantes registrados."""
    return students


def search_by_document(document):
    """Busca un estudiante por su documento."""

    for student in students:
        if student["documento"] == document:
            return student

    return None


def register_student(new_student):
    """Registra un nuevo estudiante."""

    if search_by_document(new_student["documento"]):
        return False

    students.append(new_student)
    save_data()
    return True

def edit_student(document, updated_student):
    """Edita los datos del estudiante encontrado."""

    student = search_by_document(document)

    if student is None:
        return False

    student.update(updated_student)

    save_data()

    return True

def search_by_name(name):
    """Busca estudiantes por nombre."""

    results = []

    for student in students:
        if student["nombre"].lower() == name.lower():
            results.append(student)

    return results


def delete_student(document):
    """Elimina un estudiante por su documento."""

    student = search_by_document(document)

    if student is None:
        return False

    students.remove(student)

    save_data()

    return True