def input_student():

    print("\n=== REGISTRO DE ESTUDIANTE ===")

    tipo_doc = input("Tipo de documento: ")
    documento = input("Documento: ")
    nombre = input("Nombre: ")
    apellidos = input("Apellidos: ")
    ficha = input("Ficha: ")
    programa = input("Programa: ")

    return tipo_doc, documento, nombre, apellidos, ficha, programa


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