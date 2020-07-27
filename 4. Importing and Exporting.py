from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import sys
import time
import os
leaderboard_names=[]
leaderboard_scores=[]
leaderboard_times=[]
questions=[]
answers=[]
highscore_list=[]

class Importing:
    reading=[]
    f=open("Scores.txt","r")
    for i in f.read().split("\n"): #Reads the scores.txt file and separates each line by splittng '\n'. Each line is then appended to reading to be used to append to leaderboard lists.
        reading.append(i)
    reading.pop()
    for i in reading:
        leaderboard_names.append(i.split(",")[0]) #Splits each item in reading at ',' and takes the first item.
        leaderboard_scores.append(i.split(",")[1]) #Splits each item in reading at ',' and takes the second item.
        leaderboard_times.append(i.split(",")[2]) #Splits each item in reading at ',' and takes the third item.
    f.close()
    

class Exporting:
    f=open("Scores.txt","w")
    for i in range(len(leaderboard_names)-1):
        f.write(leaderboard_names[i]+","+str(leaderboard_scores[i])+","+str(leaderboard_times[i])+"\n") #Writes back old scores into 'Scores.txt' file to keep previous data.
    f.write(leaderboard_names[-1]+","+str(leaderboard_scores[-1])+","+str(leaderboard_times[-1])+"\n") #Writes in the current users scores into 'Scores.txt' to record new data.
    f.close()
