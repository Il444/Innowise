quiz = {"What is a capital of France? " : "Paris",
        "Who is the president of thew united states? " : "Trump",
        "Who has become the first trillionere in history? " : "Elon Musk"}

def run_quiz():
    score = 0
    print("Let's start our simple Quiz")
    for questions, correct_answers in quiz.items():
        answer = input(f"{questions} ").strip()
        if answer.lower() == correct_answers.lower():
            score += 1
        else:
            print(f"Incorrect! The correct answer was {correct_answers}.")

    print("=== Quiz Complete ====")

    if score == 3:
        print("Congrtulations, you got it all right! You got " + str(score))
    else:
        percentage = (score / len(quiz)) * 100
        print(f"You got {score} out of {len(quiz)}, which is {percentage:.0f}% of quiz")

if __name__ == "__main__":
    run_quiz()