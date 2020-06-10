from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Quiz:
    def __init__(self):
        
        # Formatting variables
        background_color = "coral"
        
        # Quiz Frame
        self.quiz_frame = Frame(bg = background_color,
                                pady = 10)
        self.quiz_frame.grid()
        
        # Quiz Heading (row 0)
        self.quiz_heading_label = Label(self.quiz_frame,
                                        text = "Geography Quiz",
                                        font = "Arial 16 bold", bg = background_color,
                                        padx = 10, pady = 10)
        self.quiz_heading_label.grid(row = 0)
        
        # User Instructions (row 1)
        self.quiz_instructions_label = Label(self.quiz_frame,
                                             text = "Click on the button that "
                                                    "contains the correct answer.",
                                             font = "Arial 10 italic", wrap = 290,
                                             bg = background_color,
                                             padx = 10, pady = 10)
        self.quiz_instructions_label.grid(row = 1)
        
        # Question (row 2)
        self.quiz_question_label = Label(self.quiz_frame,
                                         text = "Placeholder",
                                         font = "Arial 10", wrap = 290,
                                         bg = background_color,
                                         padx = 10, pady = 10)  # Reads question from file and replaces placeholder with the question later.
        self.quiz_question_label.grid(row = 2)
        
        
class Question:
     
     
        
class Answer:
    
    # Answer 1 (row 3)
    self.quiz_answer_1_button = Button(self.quiz_frame,
                                       text = "Placeholder",
                                       font = "Arial 10", wrap = 290,
                                       bg = background_color,
                                       padx = 10, pady = 10, command = self.answer_1)  # Reads one possible answer from file and replaces place holder with the answer later.
    self.quiz_answer_1_button.grid(row = 3)    
    
    def answer_1:
        
        
    def answer_2:
        
        
    def answer_3:
        
        
    def answer_4:
        
        
        
        
        
        
        
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz()
    root.mainloop()