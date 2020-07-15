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

class Quiz_Mechanics:
    file=open("Q.txt","r")
    for i in file.read().split("\n"): #reads the Q.txt file and appends every line individually to the questions list.
        questions.append(i)
    file.close()
    file=open("A.txt","r")
    for i in file.read().split("\n"): #reads the A.txt file and appends every line individually to the answers list.
        answers.append(i)
    questions.pop() #There is an extra empty item in the both the lists so this removes it.
    answers.pop()
    score=0
    time.sleep(0.5)
    print(""" _    _         ___             _   _               
| |  | |       / _ \           | \ | |              
| |  | | ___  / /_\ \_ __ ___  |  \| | _____      __
| |/\| |/ _ \ |  _  | '__/ _ \ | . ` |/ _ \ \ /\ / /
\  /\  /  __/ | | | | | |  __/ | |\  | (_) \ V  V / 
 \/  \/ \___| \_| |_/_|  \___| \_| \_/\___/ \_/\_/  
                                                    
                                                    
      _____ _             _   _             _       
     /  ___| |           | | (_)           | |      
     \ `--.| |_ __ _ _ __| |_ _ _ __   __ _| |      
      `--. \ __/ _` | '__| __| | '_ \ / _` | |      
     /\__/ / || (_| | |  | |_| | | | | (_| |_|      
     \____/ \__\__,_|_|   \__|_|_| |_|\__, (_)      
                                       __/ |        
                                      |___/         """)
    time.sleep(0.5)
    start=time.time() #Starts the timer.
    for i in range(10):
        print("Question "+str(i+1))
        one=random.randint(0,len(questions)-1)
        print(questions[one])
        temp_ans=answers[one].split(",")
        answer=temp_ans[0]
        b1=answer
        a=random.randint(0,3)
        print("a) "+temp_ans[a])
        del temp_ans[a] 
        if answer not in temp_ans:
            answer='a' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'a' will be the answer.
        b=random.randint(0,2)
        print("b) "+temp_ans[b])
        del temp_ans[b]
        if answer!='a':
            if answer not in temp_ans:
                answer='b' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'b' will be the answer.
        c=random.randint(0,1)
        print("c) "+temp_ans[c])
        del temp_ans[c]
        if answer!='a' and answer!='b':
            if answer not in temp_ans:
                answer='c' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'c' will be the answer.
        d=random.randint(0,0)
        print("d) "+temp_ans[d])
        del temp_ans[d]
        if answer==b1:
            answer='d' #If the answer isn't 'a' 'b' or 'c', the answer is 'd'.
        q=input("Your answer: ")
        valid=('a','b','c','d',b1.lower())
        while True:
            if q.lower() not in valid: #makes sure that the input is yes or no
                print('Please input your answer again.', end='\n')
                q=input("Your answer: ")
            else:
                break
        if q.lower()==answer.lower() or q.lower()==b1.lower():
            score=score+1
            print("You are correct!!!!!")
        else:
            print("You are incorrect.....")
            print("The answer was "+answer+") "+b1)
        print("---------------------------------------------")
        del questions[one]
        del answers[one]
    total_time=time.time()-start #Calculates the time taken to finish the quiz.
    leaderboard_times.append(round(total_time,2))
    leaderboard_scores.append(str(score))
    print("Your score is",str(score)+"/10")
    questions.clear()    


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz_Mechanics()
    root.mainloop()