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
                                                    "contains the correct answer."
                                                    "\n\nWhen you are ready press START.",
                                             font = "Arial 10 italic", wrap = 290,
                                             bg = background_color,
                                             padx = 10, pady = 10)
        self.quiz_instructions_label.grid(row = 1)
        
        # Start Button (row 2)
        self.quiz_start_button = Button(self.quiz_frame,
                                        text = "START",
                                        font = "Arial 16 bold", wrap = 290,
                                        bg = "cyan",
                                        padx = 10, pady = 10, command = self.question)
        self.quiz_start_button.grid(row = 2)
        
    def question(self):
        Question(self)
        
        
class Question:
    def __init__(self,partner):
         
        background_color = "cyan"
        
        # Question Frame
        self.question_frame = Frame(bg = background_color,
                                    pady = 10)
         
        # Question (row 1)
        self.quiz_question_label = Label(self.question_frame,
                                         text = "Placeholder",
                                         font = "Arial 10", wrap = 290,
                                         bg = background_color,
                                         padx = 10, pady = 10)  # Reads question from file and replaces placeholder with the question later.
        self.quiz_question_label.grid(row = 1)
     
        
class Answer:
    def __init__(self):
        
        # Answer 1 (row 3)
        self.quiz_answer_1_button = Button(self.quiz_frame,
                                           text = "Placeholder",
                                           font = "Arial 10", wrap = 290,
                                           bg = background_color,
                                           padx = 10, pady = 10, command = self.answer_1)  # Reads one possible answer from file and replaces place holder with the answer later.
        self.quiz_answer_1_button.grid(row = 3)
        
        # Answer 2 (row 4)
        self.quiz_answer_2_button = Button(self.quiz_frame,
                                           text = "Placeholder",
                                           font = "Arial 10", wrap = 290,
                                           bg = background_color,
                                           padx = 10, pady = 10, command = self.answer_2)  # Reads one possible answer from file and replaces place holder with the answer later.
        self.quiz_answer_2_button.grid(row = 4)
        
        # Answer 3 (row 5)
        self.quiz_answer_1_button = Button(self.quiz_frame,
                                           text = "Placeholder",
                                           font = "Arial 10", wrap = 290,
                                           bg = background_color,
                                           padx = 10, pady = 10, command = self.answer_3)  # Reads one possible answer from file and replaces place holder with the answer later.
        self.quiz_answer_1_button.grid(row = 5)
        
        # Answer 4 (row 6)
        self.quiz_answer_1_button = Button(self.quiz_frame,
                                           text = "Placeholder",
                                           font = "Arial 10", wrap = 290,
                                           bg = background_color,
                                           padx = 10, pady = 10, command = self.answer_4)  # Reads one possible answer from file and replaces place holder with the answer later.
        self.quiz_answer_1_button.grid(row = 6)    
    
    #def answer_1:
        #print("a")
        
    #def answer_2:
        #print("a")
        
    #def answer_3:
        #print("a")
        
    #def answer_4:
        #print("a")
        
        
        
        
        
        
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz()
    root.mainloop()