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
        
        print(questions)
        
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
        
        start=time.time() #Starts the timer.
        for i in range(10):
            
            # Set up Question Heading (row 0)
            self.question_heading = Label(self.question_frame, text = "Question "+str(i+1),
                                          font = "arial 14 bold", bg = background_color, padx = 100, pady = 20, borderwidth = 5, relief = "solid")
            self.question_heading.grid(row = 0)
            
            question_number = random.randint(0,len(questions)-1)
            
            # Question (row 1)
            self.question_label = Label(self.question_frame,
                                             text = questions[question_number], # WILL EVENTUALLY GET QUESTION READ FROM A TEXT FILE HERE
                                             font = "Arial 12 bold", wrap = 290,
                                             bg = "pale green",
                                             padx = 100, pady = 20)  # Reads question from file and replaces placeholder with the question later.
            self.question_label.grid(row = 1)
            
            print(answers[question_number])
            temp_ans = answers[question_number].split(",")
            print(temp_ans)
            
            answer=temp_ans[0]
            b1=answer
            a=random.randint(0,3)            
            
            # Answer 1 (row 2)
            self.question_answer_1_button = Button(self.question_frame,
                                               text = "a) "+temp_ans[a],
                                               font = "Arial 10", wrap = 290,
                                               bg = background_color,
                                               padx = 100, pady = 20, command = self.answer_1)  # Reads one possible answer from file and replaces place holder with the answer later.
            self.question_answer_1_button.grid(row = 2, pady = 10)
            
            del temp_ans[a]
            if answer not in temp_ans:
                answer='a' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'a' will be the answer.            
            
            b=random.randint(0,2)
                
            # Answer 2 (row 3)
            self.question_answer_2_button = Button(self.question_frame,
                                               text = "b) "+temp_ans[b],
                                               font = "Arial 10", wrap = 290,
                                               bg = "coral",
                                               padx = 100, pady = 20, command = self.answer_2)  # Reads one possible answer from file and replaces place holder with the answer later.
            self.question_answer_2_button.grid(row = 3, pady = 10)
            
            del temp_ans[b]
            if answer!='a':
                if answer not in temp_ans:
                    answer='b' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'b' will be the answer.            
            
            c=random.randint(0,1)
            
            # Answer 3 (row 4)
            self.question_answer_3_button = Button(self.question_frame,
                                               text = "c) "+temp_ans[c],
                                               font = "Arial 10", wrap = 290,
                                               bg = background_color,
                                               padx = 100, pady = 20, command = self.answer_3)  # Reads one possible answer from file and replaces place holder with the answer later.
            self.question_answer_3_button.grid(row = 4, pady = 10)
            
            del temp_ans[c]
            if answer!='a' and answer!='b':
                if answer not in temp_ans:
                    answer='c' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'c' will be the answer.            
            
            d=random.randint(0,0)
            
            # Answer 4 (row 5)
            self.question_answer_4_button = Button(self.question_frame,
                                               text = "d) "+temp_ans[d],
                                               font = "Arial 10", wrap = 290,
                                               bg = "coral",
                                               padx = 100, pady = 20, command = self.answer_4)  # Reads one possible answer from file and replaces place holder with the answer later.
            self.question_answer_4_button.grid(row = 5, pady = 10)
            
            del temp_ans[d]
            if answer==b1:
                answer='d' #If the answer isn't 'a' 'b' or 'c', the answer is 'd'.
    def answer_1(self):
        q = temp_ans[a]
        print(q)
        if q.lower()==answer.lower() or q.lower()==b1.lower():
            score=score+1
            print("You are correct!!!!!")
        else:
            print("You are incorrect.....")
            print("The answer was "+answer+") "+b1)
        print("---------------------------------------------")
        del questions[question]
        del answers[question]
        
    def answer_2(self):
        q = temp_ans[b]
        print(q)
        if q.lower()==answer.lower() or q.lower()==b1.lower():
            score=score+1
            print("You are correct!!!!!")
        else:
            print("You are incorrect.....")
            print("The answer was "+answer+") "+b1)
        print("---------------------------------------------")
        del questions[question]
        del answers[question]
        
    def answer_3(self):
        q = temp_ans[c]
        print(q)
        if q.lower()==answer.lower() or q.lower()==b1.lower():
            score=score+1
            print("You are correct!!!!!")
        else:
            print("You are incorrect.....")
            print("The answer was "+answer+") "+b1)
        print("---------------------------------------------")
        del questions[question]
        del answers[queston]     
        
    def answer_4(self):
        q = temp_ans[c]
        print(q)
        if q.lower()==answer.lower() or q.lower()==b1.lower():
            score=score+1
            print("You are correct!!!!!")
        else:
            print("You are incorrect.....")
            print("The answer was "+answer+") "+b1)
        print("---------------------------------------------")
        del questions[question]
        del answers[question]
           
        total_time=time.time()-start #Calculates the time taken to finish the quiz.
        leaderboard_times.append(round(total_time,2))
        leaderboard_scores.append(str(score))
        print("Your score is",str(score)+"/10")
        questions.clear()            
    
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