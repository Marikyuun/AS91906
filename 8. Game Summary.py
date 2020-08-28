from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import sys
import os
leaderboard_names=[]
leaderboard_scores=[]
questions=[]
answers=[]
scores=[]
question_number=["1"]
correct_answers=[]
highscore_list=[]

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
                                        font = "calibri 16 bold", bg = background_color,
                                        padx = 10, pady = 10)
        self.quiz_heading_label.grid(row = 0)
        
        # Start Button (row 2)
        self.question_button = Button(self.quiz_frame,
                                        text = "Start",
                                        font = "calibri 16 bold", wrap = 290,
                                        bg = "cyan", width = 10,
                                        padx = 50, pady = 5, command = self.question)
        self.question_button.grid(row = 2, padx = 20, pady = 10)
    
    def question(self):
        Question(self)


class Question:
    
    def __init__(self,parent):
        
        background_color = "cyan"
        
        # disable start button
        parent.question_button.config(state = DISABLED)
        
        # Sets up child window (ie: question box)
        self.question_box = Toplevel()
        
        # Question Frame
        self.question_frame = Frame(self.question_box, width = 300, bg = "pale green")
        self.question_frame.grid()
        
        # Set up Question Heading (row 0)
        self.question_heading = Label(self.question_frame, text = "Question "+str(len(question_number)),
                                      font = "calibri 14 bold", bg = background_color, padx = 200, pady = 20, borderwidth = 5, relief = "solid")
        self.question_heading.grid(row = 0)
        
        self.game_summary()
    
    def destroy_children(self,parent_frame):
        # Destroy all children from a frame
        # :param parent_frame: The frame to destory all children from
        
        for child in parent_frame.winfo_children():
            child.destroy()    
    
    def game_summary(self):
        Game_Summary(self)

class Game_Summary:
    
    def __init__(self,parent):
        
        parent.destroy_children(parent.question_frame)
        
        self.summary_label = Label(parent.question_frame, font = "calibri 20 bold underline",bg = 'coral', width = 35,
                                   text = "Quiz Summary", pady = 10)
        self.summary_label.grid(row = 0)        
        
        self.score_button = Button(parent.question_frame,
                                  text = "View Score",
                                  font = "calibri 12", wrap = 290,
                                  bg = "cyan", width = 30,
                                  padx = 100, pady = 20, command = lambda : self.score(parent))
        self.score_button.grid(row = 1, pady = 20, padx = 20)
        
        self.question_summary_button = Button(parent.question_frame,
                                  text = "Question Summary",
                                  font = "calibri 12", wrap = 290,
                                  bg = "cyan", width = 30,
                                  padx = 100, pady = 20, command = lambda : self.question_summary(parent))
        self.question_summary_button.grid(row = 2, pady = 20, padx = 20)
        
        self.leaderboard_button = Button(parent.question_frame,
                                  text = "Leaderboard",
                                  font = "calibri 12", wrap = 290,
                                  bg = "cyan", width = 30,
                                  padx = 100, pady = 20, command = lambda : self.leaderboard(parent))
        self.leaderboard_button.grid(row = 3, pady = 20, padx = 20)
        
        self.quit_button = Button(parent.question_frame,
                                  text = "Quit",
                                  font = "calibri 12",
                                  bg = "red", width = 10,
                                  command = self.quit)
        self.quit_button.grid(pady = 10, row = 4, column = 0)
        
        self.restart_button = Button(parent.question_frame,
                                     text = "Restart",
                                     font = "calibri 12",
                                     bg = "green", width = 10,
                                     command = lambda : self.restart(parent))
        self.restart_button.grid(pady = 10, row = 4, column = 0) 

    
    def score(self,parent):
        parent.destroy_children(parent.question_frame)
        
        self.score_label = Label(parent.question_frame,
                                 text = "Total Score",
                                 font = "calibri 20 bold underline",
                                 bg = "coral", width = 35, pady = 10)
        self.score_label.grid(row = 0,)
        
        self.your_score_label = Label(parent.question_frame,
                                 text = "Your Score Is: " + str(len(scores)) + "/10",
                                 font = "calibri 20 bold",
                                 bg = "pale green", width = 35, pady = 10)
        self.your_score_label.grid(row = 1, pady = 20)
        
        self.restart_button = Button(parent.question_frame,
                                     text = "Back",
                                     font = "calibri 12",
                                     bg = "coral", width = 10,
                                     command = parent.game_summary)
        self.restart_button.grid(pady = 10, row = 2) 
    
    def question_summary(self,parent):
        parent.destroy_children(parent.question_frame)
        
        self.score_label = Label(parent.question_frame,
                                 text = "Question Summary",
                                 font = "calibri 20 bold underline",
                                 bg = "coral", width = 35, pady = 10)
        self.score_label.grid(row = 0,)
        
        self.your_score_label = Label(parent.question_frame,
                                 text = "Placeholder",
                                 font = "calibri 20 bold",
                                 bg = "pale green", width = 35, pady = 10)
        self.your_score_label.grid(row = 1, pady = 20)
        
        self.restart_button = Button(parent.question_frame,
                                     text = "Back",
                                     font = "calibri 12",
                                     bg = "coral", width = 10,
                                     command = parent.game_summary)
        self.restart_button.grid(pady = 10, row = 2) 
    
    def leaderboard(self,parent):
        parent.destroy_children(parent.question_frame)
        
        self.score_label = Label(parent.question_frame,
                                 text = "Leaderboard",
                                 font = "calibri 20 bold underline",
                                 bg = "coral", width = 35, pady = 10)
        self.score_label.grid(row = 0,)
        
        self.your_score_label = Label(parent.question_frame,
                                 text = "Placeholder",
                                 font = "calibri 20 bold",
                                 bg = "pale green", width = 35, pady = 10)
        self.your_score_label.grid(row = 1, pady = 20)
        
        self.restart_button = Button(parent.question_frame,
                                     text = "Back",
                                     font = "calibri 12",
                                     bg = "coral", width = 10,
                                     command = parent.game_summary)
        self.restart_button.grid(pady = 10, row = 2) 
    
    def quit(self):
        sys.exit()
    
    def restart(self,parent):
        a

    def destroy_children(self,parent_frame):
        # Destroy all children from a frame
        # :param parent_frame: The frame to destory all children from
        
        for child in parent_frame.winfo_children():
            child.destroy()  

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz()
    root.mainloop()
