from templates.students_templates import create_student
from models.students_model import register_student, get_all
from views.students_view import input_student, show_students


def main():

    while True:

        datos = input_student()

        student = create_student(*datos)

        if register_student(student):
            print("\nEstudiante registrado correctamente.")
        else:
            print("\nEse documento ya está registrado.")

        continuar = input("\n¿Registrar otro estudiante? (S/N): ").upper()

        if continuar != "S":
            break

    show_students(get_all())


if __name__ == "__main__":
    main()


