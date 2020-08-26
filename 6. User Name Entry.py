from tkinter import *
from functools import partial  # To prevent unwanted windows

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
        
        # User Instructions (row 1)
        self.quiz_instructions_label = Label(self.quiz_frame,
                                             text = "Click on the button that "
                                                    "contains the correct answer."
                                                    "\n\nWhen you are ready press START.",
                                             font = "calibri 10 italic", wrap = 290,
                                             bg = background_color,
                                             padx = 10, pady = 10)
        self.quiz_instructions_label.grid(row = 1)
        
        # Start Button (row 2)
        self.quiz_start_button = Button(self.quiz_frame,
                                        text = "START",
                                        font = "calibri 16 bold", wrap = 290,
                                        bg = "cyan",
                                        padx = 10, pady = 10, command = self.name)
        self.quiz_start_button.grid(row = 2)
    
    def name(self):
        Name(self)

class Name:
    def __init__(self, parent):
        
        background = "cyan"
        
        # disable start button
        parent.quiz_start_button.config(state = DISABLED)        
        
        # Sets up child window (ie: name entry box)
        self.name_box = Toplevel()
        
        # If users press cross at top, closes help and 'releases' help button
        self.name_box.protocol('WM_DELETE_WINDOW', partial(self.close_name_entry, parent))
        
        # Set up GUI Frame
        self.name_frame = Frame(self.name_box, width = 300, bg = background)
        self.name_frame.grid()
        
        # Name Entry Heading (row 0)
        self.name_label = Label(self.name_frame, font = "calibri 20 bold",bg = background, width = 30,
                                      text = "Please Enter Your Username Below")
        self.name_label.grid(row = 0)
        
        # User Name Entry Box (row 1)
        self.name_entry = Entry(self.name_frame, width = 30, bg = background, font = "calibri 16 bold", justify = 'center')	
        self.name_entry.grid(row = 1, pady = 20)
        
        # User Name Submit Box (row 2)
        self.name_submit_button = Button(self.name_frame, font= "calibri 16 bold", width = 30, pady = 5, bg = "coral",
                                         text = "Submit", command = partial(self.name_record,parent))
        self.name_submit_button.grid(row = 2, pady = 20)
    
    def name_record(self, parent):
        name = self.name_entry.get()
    
    def close_name_entry(self, parent):
        # Put help button back to normal...
        parent.quiz_start_button.config(state = NORMAL)
        self.name_box.destroy()
    

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz()
    root.mainloop()
