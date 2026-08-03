import re
import csv
import os
from models import students_model


def validar_numerico(mensaje):
    while True:
        dato = input(mensaje)

        if dato.isdigit():
            return dato

        print("Error. Solo se permiten números.")


def validar_alfabetico(mensaje):
    while True:
        dato = input(mensaje)

        if dato.replace(" ", "").isalpha():
            return dato.title()

        print("Error. Solo se permiten letras.")


def validar_correo(mensaje):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    while True:
        correo = input(mensaje)

        if re.match(patron, correo):
            return correo

        print("Correo electrónico no válido.")


def init_app_data():
    """Inicializa los datos de la aplicación."""
    students_model.load_data()


def input_student():

    print("\n=== REGISTRO DE ESTUDIANTE ===")

    tipo_doc = validar_alfabetico("Tipo de documento: ")
    documento = validar_numerico("Documento: ")
    nombre = validar_alfabetico("Nombre: ")
    apellidos = validar_alfabetico("Apellidos: ")
    ficha = validar_numerico("Ficha: ")
    programa = validar_alfabetico("Programa: ")
    correo = validar_correo("Correo electrónico: ")

    return (
        tipo_doc,
        documento,
        nombre,
        apellidos,
        ficha,
        programa,
        correo
    )


def input_edit_student():

    print("\n=== EDITAR ESTUDIANTE ===")

    documento = input("Documento del estudiante a editar: ")

    tipo_doc = validar_alfabetico("Nuevo tipo de documento: ")
    nombre = validar_alfabetico("Nuevo nombre: ")
    apellidos = validar_alfabetico("Nuevos apellidos: ")
    ficha = validar_numerico("Nueva ficha: ")
    programa = validar_alfabetico("Nuevo programa: ")
    correo = validar_correo("Nuevo correo electrónico: ")

    return (
        documento,
        tipo_doc,
        nombre,
        apellidos,
        ficha,
        programa,
        correo
    )


def input_search_student():

    print("\n=== BUSCAR ESTUDIANTE ===")

    nombre = validar_alfabetico(
        "Nombre del estudiante a buscar: "
    )

    return nombre


def show_search_results(students):

    if not students:
        print("\nNo se encontraron estudiantes.")
        return

    print("\n=== RESULTADOS DE LA BÚSQUEDA ===")

    for i, student in enumerate(students, start=1):

        print(f"\nEstudiante {i}")
        print(f"Tipo documento: {student['tipo_documento']}")
        print(f"Documento: {student['documento']}")
        print(f"Nombre: {student['nombre']}")
        print(f"Apellidos: {student['apellidos']}")
        print(f"Ficha: {student['ficha']}")
        print(f"Programa: {student['programa']}")
        print(f"Correo: {student['correo']}")


def show_students(students):

    print("\n=== ESTUDIANTES REGISTRADOS ===")

    for i, student in enumerate(students, start=1):

        print(f"\nEstudiante {i}")
        print(f"Tipo documento: {student['tipo_documento']}")
        print(f"Documento: {student['documento']}")
        print(f"Nombre: {student['nombre']}")
        print(f"Apellidos: {student['apellidos']}")
        print(f"Ficha: {student['ficha']}")
        print(f"Programa: {student['programa']}")
        print(f"Correo: {student['correo']}")

def input_delete_student():
    print("\n=== ELIMINAR ESTUDIANTE ===")

    documento = validar_numerico(
        "Documento del estudiante a eliminar: "
    )

    return documento


def export_students_csv(students):
    """Exporta los estudiantes a un archivo CSV."""

    export_file = os.path.join(
        os.path.dirname(__file__),
        "..",
        "..",
        "data",
        "students.csv"
    )

    with open(
        export_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "tipo_documento",
                "documento",
                "nombre",
                "apellidos",
                "ficha",
                "programa",
                "correo"
            ]
        )

        writer.writeheader()
        writer.writerows(students)

    print("\nEstudiantes exportados correctamente.")
    print(f"Archivo creado en: {export_file}")