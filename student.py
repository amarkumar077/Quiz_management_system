from quiz import start_quiz


def student_menu(student_name):

    while True:

        print("\n" + "=" * 50)
        print(f"      WELCOME {student_name.upper()}")
        print("=" * 50)

        print("1. Start Quiz")
        print("2. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            start_quiz()

        elif choice == "2":

            print("\nLogout Successful")
            break

        else:

            print("\nInvalid Choice!")