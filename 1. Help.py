from tkinter import *
from functools import partial  # To prevent unwanted windows

import random


class Quiz:
    def __init__(self):
        
        # Formatting variables...
        background_color = "coral"
        
        # Quiz Main Screen GUI...
        self.quiz_frame = Frame(width = 600, height = 600, bg = background_color,
                                     pady = 10)
        self.quiz_frame.grid()
        
        # Geography Quiz Heading (row 0)
        self.quiz_label = Label(self.quiz_frame, text = "Geography Quiz",
                                          font = ("Arial", "16", "bold"),
                                          bg = background_color,
                                          padx = 10, pady = 10)
        self.quiz_label.grid(row = 0)
        
        # Help Button (row 1)
        self.help_button = Button(self.quiz_frame, text = "Help",
                                  font = ("Arial", "14"),
                                  bg = "cyan",
                                  padx = 10, pady = 10, command = self.help)
        self.help_button.grid(row = 1)

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text = "Help text goes here")


class Help:
    def __init__(self,parent):
        
        background = "cyan"
        
        # disable help button
        parent.help_button.config(state = DISABLED)
        
        # Sets up child window (ie: help box)
        self.help_box = Toplevel()
        
        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, parent))        
        
        
        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width = 300, bg = background)
        self.help_frame.grid()
        
        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text = "Help / Instructions",
                                 font = "arial 14 bold", bg = background)
        self.how_heading.grid(row = 0)
        
        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text = "",
                                  justify = LEFT, width = 40, bg = background, wrap = 250)
        self.help_text.grid(row = 1)
        
        # Dismiss Button (row 2)
        self.dismiss_button = Button(self.help_frame, text = "Dismiss",
                                     width = 10, bg = "coral", font = "arial 10 bold",
                                    command = partial(self.close_help, parent))
        self.dismiss_button.grid(row = 2, pady = 10)        

    def close_help(self, parent):
        # Put help button back to normal...
        parent.help_button.config(state = NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz()
    root.mainloop()