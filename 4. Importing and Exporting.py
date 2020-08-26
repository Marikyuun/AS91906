from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import sys
import time
import os
leaderboard_names=[]
leaderboard_scores=[]
questions=[]
answers=[]
highscore_list=[]

class Importing:
    def __init__(self):
        
        reading=[]
        f=open("Scores.txt","r")
        for i in f.read().split("\n"): #Reads the scores.txt file and separates each line by splittng '\n'. Each line is then appended to reading to be used to append to leaderboard lists.
            reading.append(i)
        reading.pop()
        for i in reading:
            leaderboard_names.append(i.split(",")[0]) #Splits each item in reading at ',' and takes the first item.
            leaderboard_scores.append(i.split(",")[1]) #Splits each item in reading at ',' and takes the second item.
        f.close()    
        
        print(leaderboard_names)
        print(leaderboard_scores)
        
        # Exporting GUI
        self.exporting_frame = Frame(width = 600, height = 600,
                                     pady = 10)
        self.exporting_frame.grid()
        
        self.export_button = Button(self.exporting_frame, text = "Export Score",
                                    bg = "cyan", command = self.exporting, font = 'calibri 16 bold')
        self.export_button.grid(row = 0)
    
    def exporting(self):
        Exporting()

class Exporting:
    def __init__(self):
        f=open("Scores.txt","w")
        for i in range(len(leaderboard_names)-1):
            f.write(leaderboard_names[i]+","+str(leaderboard_scores[i])+","+"\n") #Writes back old scores into 'Scores.txt' file to keep previous data.
        f.write(leaderboard_names[-1]+","+str(leaderboard_scores[-1])+","+"\n") #Writes in the current users scores into 'Scores.txt' to record new data.
        f.close()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Importing()
    root.mainloop()