from tkinter import *
from quiz_brain import QuizBrain
from data import question_data

THEME_COLOR = "#423762"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 20, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=260,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, borderwidth=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, borderwidth=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        exit_image = PhotoImage(file="images/exit.png")
        self.exit_button = Button(image=exit_image, highlightthickness=0, borderwidth=0, command=self.window.destroy) 

        self.get_next_question()

        self.window.mainloop()
    
    def get_next_question(self):
         self.canvas.config(bg="white") 
         if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
         else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.score_label.config(fg=THEME_COLOR)
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz. \nYour score is:{self.quiz.score}/{self.quiz.question_number}.")
            self.true_button.destroy()
            self.false_button.destroy() 
            self.exit_button.grid(row=2, column=0)
    
    def true_pressed(self):
        answer = self.quiz.check_answer("True")
        self.update_screen_answer(answer)

    def false_pressed(self):
        answer = self.quiz.check_answer("False")
        self.update_screen_answer(answer)

    def update_screen_answer(self, answer):
        if answer:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(800, self.get_next_question)
        self.update_score()

    def update_score(self):
        score = self.quiz.get_score()
        self.score_label.config(text=f"Score: {score}")


