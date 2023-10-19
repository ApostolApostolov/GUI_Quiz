from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TEXT_BOX_FONT = ("Ariel", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(pady=20,
                              padx=20,
                              bg=THEME_COLOR)

        self.score_label = Label(self.window,
                                 text="Score: 0",
                                 bg=THEME_COLOR,
                                 fg="white",
                                 )
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300,
                             height=250,
                             bg="white",
                             )

        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Lorem Ipsum",
                                                     fill=THEME_COLOR,
                                                     font=TEXT_BOX_FONT,
                                                     )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        button_true_img = PhotoImage(file="images/true.png")
        button_false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(self.window,
                                  image=button_true_img,
                                  highlightthickness=0,
                                  command=self.true_pressed)

        self.false_button = Button(self.window,
                                   image=button_false_img,
                                   highlightthickness=0,
                                   command=self.false_pressed
                                   )

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        if not self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)


        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def true_pressed(self, ):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.configure(bg="green")

        else:
            self.canvas.configure(bg="red")

        self.window.after(1000, self.get_next_question)
