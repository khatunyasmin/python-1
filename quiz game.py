class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define your list of questions
questions = [
    Question("What is the capital of France?\n(a) Paris\n(b) London\n(c) Berlin\n", "a"),
    Question("Which planet is known as the Red Planet?\n(a) Mars\n(b) Venus\n(c) Jupiter\n", "a"),
    Question("What is the largest mammal in the world?\n(a) Elephant\n(b) Giraffe\n(c) Blue Whale\n", "c"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer.lower() == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is: {}\n".format(question.answer))

    print("You got {}/{} questions correct.".format(score, len(questions)))

if __name__ == "__main__":
    print("Welcome to the Quiz Game!\n")
    run_quiz(questions)
