from models import students_model
from templates import students_templates

def create_student(
    tipo_doc,
    documento,
    nombre,
    apellidos,
    ficha,
    programa,
    correo
):

    return {
        "tipo_documento": tipo_doc,
        "documento": documento,
        "nombre": nombre,
        "apellidos": apellidos,
        "ficha": ficha,
        "programa": programa,
        "correo": correo
    }

def edit_student():
    """Controla la edición de un estudiante."""

    datos = students_templates.input_edit_student()

    documento = datos[0]

    updated_student = {
        "tipo_documento": datos[1],
        "nombre": datos[2],
        "apellidos": datos[3],
        "ficha": datos[4],
        "programa": datos[5],
        "correo": datos[6]
    }

    if students_model.edit_student(documento, updated_student):
        print("\nEstudiante actualizado correctamente.")
    else:
        print("\nNo se encontró un estudiante con ese documento.")


def search_student():
    """Controla la búsqueda de estudiantes por nombre."""

    nombre = students_templates.input_search_student()

    students = students_model.search_by_name(nombre)

    students_templates.show_search_results(students)


def delete_student():
    """Controla la eliminación de un estudiante."""

    documento = students_templates.input_delete_student()

    if students_model.delete_student(documento):
        print("\nEstudiante eliminado correctamente.")
    else:
        print("\nNo se encontró un estudiante con ese documento.")


def export_students():
    """Controla la exportación de los estudiantes."""

    students = students_model.get_all()

    if not students:
        print("\nNo hay estudiantes para exportar.")
        return

    students_templates.export_students_csv(students)    