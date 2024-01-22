def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    user_answer = input("Your choice (enter the option number): ")
    return int(user_answer)

def run_quiz(questions):
    score = 0
    for question, options, correct_option in questions:
        user_answer = display_question(question, options)
        if user_answer == correct_option:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_option}: {options[correct_option - 1]}\n")

    print(f"You scored {score}/{len(questions)} points!")

# Define quiz questions, options, and correct answers
quiz_questions = [
    ("What is the capital of France?", ["Paris", "Berlin", "London", "Madrid"], 1),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], 2),
    ("What is the largest mammal in the world?", ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], 2)
]

# Run the quiz
run_quiz(quiz_questions)
