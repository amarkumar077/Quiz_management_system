import json
import random


def start_quiz():

    try:
        with open("questions.json", "r") as file:
            questions = json.load(file)

    except FileNotFoundError:
        print("\nQuestions file not found!")
        return

    except json.JSONDecodeError:
        print("\nQuestions file is empty or invalid!")
        return

    if len(questions) == 0:
        print("\nNo Questions Available!")
        return

    random.shuffle(questions)

    score = 0

    print("\n" + "=" * 50)
    print("           QUIZ STARTED")
    print("=" * 50)

    for i, q in enumerate(questions, start=1):

        print(f"\nQuestion {i}")
        print(q["question"])

        for index, option in enumerate(q["options"], start=1):
            print(f"{index}. {option}")

        answer = input("\nEnter Answer (1-4): ")

        if answer == q["answer"]:
            print("✅ Correct")
            score += 1
        else:
            print("❌ Wrong")
            print("Correct Answer:", q["answer"])

    print("\n" + "=" * 50)
    print("          QUIZ FINISHED")
    print("=" * 50)
    print(f"Your Score: {score}/{len(questions)}")