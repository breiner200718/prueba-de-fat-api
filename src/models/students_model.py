students = []


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
    return True