from templates import students_templates
from views import students_view
from models import students_model


def main():

    students_templates.init_app_data()

    while True:

        print("\n=== SISTEMA DE ESTUDIANTES ===")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Editar estudiante")
        print("4. Eliminar estudiante")
        print("5. Buscar estudiante")
        print("6. Salir")
        print("7. Exportar estudiantes")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            datos = students_templates.input_student()

            student = students_view.create_student(*datos)

            if students_model.register_student(student):
                print("\nEstudiante registrado correctamente.")
            else:
                print("\nEse documento ya está registrado.")

        elif opcion == "2":

            students_templates.show_students(
                students_model.get_all()
            )

        elif opcion == "3":

            students_view.edit_student()

        elif opcion == "4":

            students_view.delete_student()

        elif opcion == "5":

            students_view.search_student()

        elif opcion == "6":

            print("\nPrograma finalizado.")
            break

        elif opcion == "7":

            students_view.export_students()

        else:

            print("\nOpción no válida.")


if __name__ == "__main__":
    main()