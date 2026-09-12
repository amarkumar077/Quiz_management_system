import json

def add_question():

    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)
    except:
        questions = []

    print("\n========== ADD QUESTION ==========")

    question = input("Enter Question : ")

    options = []

    for i in range(1, 5):
        option = input(f"Option {i} : ")
        options.append(option)

    answer = input("Correct Answer (1-4): ")

    new_question = {
        "question": question,
        "options": options,
        "answer": answer
    }

    questions.append(new_question)

    with open("questions.json", "w") as file:
        json.dump(questions, file, indent=4)

    print("\nQuestion Added Successfully!")


# ==========================
# View Questions
# ==========================

def view_questions():

    try:

        with open("questions.json", "r") as file:
            questions = json.load(file)

        if len(questions) == 0:

            print("\nNo Questions Found!")
            return

        print("\n" + "=" * 50)
        print("           ALL QUESTIONS")
        print("=" * 50)

        for i, question in enumerate(questions, start=1):

            print(f"\nQuestion {i}")
            print(question["question"])

            for index, option in enumerate(question["options"], start=1):
                print(f"{index}. {option}")

            print("Correct Answer :", question["answer"])

    except:

        print("\nError Reading File")


# ==========================
# Delete Question
# ==========================

def delete_question():

    try:

        with open("questions.json", "r") as file:
            questions = json.load(file)

        if len(questions) == 0:

            print("\nNo Questions Available!")
            return

        view_questions()

        number = int(input("\nEnter Question Number to Delete : "))

        if number < 1 or number > len(questions):

            print("\nInvalid Question Number!")
            return

        deleted = questions.pop(number - 1)

        with open("questions.json", "w") as file:
            json.dump(questions, file, indent=4)

        print(f"\n✅ '{deleted['question']}' Deleted Successfully!")

    except ValueError:

        print("\nPlease Enter Only Numbers!")

    except Exception as e:

        print("\nError :", e)

def admin_menu():

    while True:

        print("\n========== ADMIN PANEL ==========")

        print("1. Add Question")
        print("2. View Questions")
        print("3. Delete Question")
        print("4. Logout")

        choice = input("\nEnter Choice : ")

        if choice == "1":

            add_question()

        elif choice == "2":

            view_questions()

        elif choice == "3":

            delete_question()

        elif choice == "4":

            print("\nLogout Successful")
            break

        else:

            print("\nInvalid Choice")