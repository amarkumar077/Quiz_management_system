from login import admin_login, student_login
from admin import admin_menu
from student import student_menu

while True:

    print("\n" + "=" * 45)
    print("      QUIZ MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Admin Login")
    print("2. Student Login")
    print("3. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":

        success = admin_login()

        if success:
            print("\nWelcome Admin!")
            admin_menu()

    elif choice == "2":

        student = student_login()

        student_menu(student)

    elif choice == "3":

        print("\nThank You!")
        break

    else:

        print("\nInvalid Choice!")