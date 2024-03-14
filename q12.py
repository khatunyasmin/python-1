import tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

questions = [
    Question("What is the capital of France?", ["Paris", "London", "Berlin"], "Paris"),
    Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter"], "Mars"),
    Question("What is 7 x 8?", ["56", "64", "48"], "56"),
    Question("What is the largest mammal in the world?",["Camel","Blue Whale","Hippo"] ,"Blue Whale"),
    Question("Who was the founder of Institute of Mathematical Sciences (IMSc)?",["Alladi Ramakrishnan","Ramnujan","C V Raman"],"Alladi Ramakrishnan")
    # Add more questions here
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.score = 0
        self.current_question = None
        self.question_index = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14), wraplength=400)
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(3):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda i=i: self.check_answer(i),bg="lightblue", fg="black")
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.next_question_button = tk.Button(root, text="Next Question", font=("Helvetica", 12), state=tk.DISABLED, command=self.load_next_question)
        self.next_question_button.pack(pady=20)

        self.load_next_question()

    def load_next_question(self):
        if self.question_index < len(questions):
            self.current_question = questions[self.question_index]
            self.question_label.config(text=self.current_question.question)
            random.shuffle(self.current_question.options)
            for i, button in enumerate(self.option_buttons):
                button.config(text=self.current_question.options[i])
            self.next_question_button.config(state=tk.DISABLED,bg="pink", fg="black")
        else:
            messagebox.showinfo("Quiz Complete", f"Quiz completed!\nYour score: {self.score}/{len(questions)}")
            self.root.destroy()

    def check_answer(self, selected_index):
        selected_option = self.current_question.options[selected_index]
        if selected_option == self.current_question.correct_option:
            self.score += 1
        self.question_index += 1
        self.next_question_button.config(state=tk.NORMAL,bg="green", fg="black")
        if self.question_index < len(questions):
            messagebox.showinfo("Result", f"Your answer is {'correct' if selected_option == self.current_question.correct_option else 'incorrect'}")
            self.load_next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()