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
        
        # disable start button
        partner.quiz_start_button.config(state = DISABLED)        
        
        # Sets up child window (ie: question box)
        self.question_box = Toplevel()
        
        # If users press cross at top, closes question box and 'releases' start button
        self.question_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_question, partner))        
        
        # Question Frame
        self.question_frame = Frame(self.question_box, width = 300, bg = "pale green")
        self.question_frame.grid()
         
        # Set up Question Heading (row 0)
        self.question_heading = Label(self.question_frame, text = "Question",
                                      font = "arial 14 bold", bg = background_color, padx = 100, pady = 20, borderwidth = 5, relief = "solid")
        self.question_heading.grid(row = 0)
         
        # Question (row 1)
        self.question_label = Label(self.question_frame,
                                         text = "Placeholder for Question", # WILL EVENTUALLY GET QUESTION READ FROM A TEXT FILE HERE
                                         font = "Arial 12 bold", wrap = 290,
                                         bg = "pale green",
                                         padx = 100, pady = 20)  # Reads question from file and replaces placeholder with the question later.
        self.question_label.grid(row = 1)
        
        # Answer 1 (row 2)
        self.quiz_answer_1_button = Button(self.question_frame,
                                           text = "Placeholder for Answer 1",
                                           font = "Arial 10", wrap = 290,
                                           bg = background_color,
                                           padx = 100, pady = 20, command = self.answer_1)  # Reads one possible answer from file and replaces place holder with the answer later.
        self.quiz_answer_1_button.grid(row = 2)
        
        # Answer 2 (row 3)
        self.quiz_answer_2_button = Button(self.question_frame,
                                           text = "Placeholder for Answer 2",
                                           font = "Arial 10", wrap = 290,
                                           bg = "coral",
                                           padx = 100, pady = 20, command = self.answer_2)  # Reads one possible answer from file and replaces place holder with the answer later.
        self.quiz_answer_2_button.grid(row = 3)
        
        # Answer 3 (row 4)
        self.quiz_answer_3_button = Button(self.question_frame,
                                           text = "Placeholder for Answer 3",
                                           font = "Arial 10", wrap = 290,
                                           bg = background_color,
                                           padx = 100, pady = 20, command = self.answer_3)  # Reads one possible answer from file and replaces place holder with the answer later.
        self.quiz_answer_3_button.grid(row = 4)
        
        # Answer 4 (row 5)
        self.quiz_answer_4_button = Button(self.question_frame,
                                           text = "Placeholder for Answer 4",
                                           font = "Arial 10", wrap = 290,
                                           bg = "coral",
                                           padx = 100, pady = 20, command = self.answer_4)  # Reads one possible answer from file and replaces place holder with the answer later.
        self.quiz_answer_4_button.grid(row = 5)            
    
    def answer_1(self):
        print("a")
        
    def answer_2(self):
        print("a")
        
    def answer_3(self):
        print("a")
        
    def answer_4(self):
        print("a")    
    
    def close_question(self, partner):
        # Put start button back to normal...
        partner.quiz_start_button.config(state=NORMAL)
        self.question_box.destroy()    
     
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz()
    root.mainloop()