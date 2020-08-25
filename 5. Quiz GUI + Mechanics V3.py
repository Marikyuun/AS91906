from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import sys
import os
leaderboard_names=[]
leaderboard_scores=[]
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
        
        score = 0
        
        file=open("Q.txt","r")
        for i in file.read().split("\n"): #reads the Q.txt file and appends every line individually to the questions list.
            questions.append(i)
        file.close()
        file=open("A.txt","r")
        for i in file.read().split("\n"): #reads the A.txt file and appends every line individually to the answers list.
            answers.append(i)
        questions.pop() #There is an extra empty item in the both the lists so this removes it.
        answers.pop()
        
        print(questions)
        print(answers)
        
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
        
        global answer
        global answer_control
        global question_number
        
        for i in range(10):
            # Set up Question Heading (row 0)
            self.question_heading = Label(self.question_frame, text = "Question "+str(i+1),
                                          font = "arial 14 bold", bg = background_color, padx = 100, pady = 20, borderwidth = 5, relief = "solid")
            self.question_heading.grid(row = 0)
            
            question_number = random.randint(0,len(questions)-1)
            
            # Question (row 1)
            self.question_label = Label(self.question_frame,
                                             text = questions[question_number],
                                             font = "Arial 12 bold", wrap = 290,
                                             bg = "pale green",
                                             padx = 100, pady = 20)
            self.question_label.grid(row = 1)
            
            temp_ans = answers[question_number].split(",")
            answer = temp_ans[0]
            answer_control = temp_ans[0]
            print(questions[question_number])
            print(temp_ans)
            ########### PLACE HERE
            a=random.randint(0,3)
                         
            # Answer 1 (row 2)
            self.question_answer_1_button = Button(self.question_frame,
                                               text = "a) "+temp_ans[a],
                                               font = "Arial 10", wrap = 290,
                                               bg = background_color,
                                               padx = 100, pady = 20, command = answer_1(self))
            self.question_answer_1_button.grid(row = 2, pady = 10)            
            
            del temp_ans[a]
            if answer_control not in temp_ans:
                answer='a' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'a' will be the answer. 
            print(answer)
            
            b=random.randint(0,2)
            
            # Answer 2 (row 3)
            self.question_answer_2_button = Button(self.question_frame,
                                               text = "b) "+temp_ans[b],
                                               font = "Arial 10", wrap = 290,
                                               bg = "coral",
                                               padx = 100, pady = 20, command = answer_2(self))
            self.question_answer_2_button.grid(row = 3, pady = 10)
            
            del temp_ans[b]
            if answer!='a':
                if answer_control not in temp_ans:
                    answer='b' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'b' will be the answer.            
            print(answer)
            
            c=random.randint(0,1)
            
            # Answer 3 (row 4)
            self.question_answer_3_button = Button(self.question_frame,
                                               text = "c) "+temp_ans[c],
                                               font = "Arial 10", wrap = 290,
                                               bg = background_color,
                                               padx = 100, pady = 20, command = answer_3(self))
            self.question_answer_3_button.grid(row = 4, pady = 10)
            
            del temp_ans[c]
            if answer!='a' and answer!='b':
                if answer_control not in temp_ans:
                    answer='c' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'c' will be the answer.            
            print(answer)
            
            d=0
            
            # Answer 4 (row 5)
            self.question_answer_4_button = Button(self.question_frame,
                                               text = "d) "+temp_ans[d],
                                               font = "Arial 10", wrap = 290,
                                               bg = "coral",
                                               padx = 100, pady = 20, command = answer_4(self))
            self.question_answer_4_button.grid(row = 5, pady = 10)
            
            del temp_ans[d]
            if answer==answer_control:
                answer='d' #If the answer isn't 'a' 'b' or 'c', the answer is 'd'.            
            print(answer)
            print(question_number)
            print(len(questions))             
            
            del questions[question_number]
            del answers[question_number]            
            
            def destroy_children(parent_frame):
                # Destroy all childen from a frame
                # :param parent_frame: The frame to destory all children from
                
                for child in parent_frame.winfo_children():
                    child.destroy()
            
            destroy_children(self.question_frame)
    
        leaderboard_scores.append(str(score))
        print("Your score is",str(score)+"/10")
        questions.clear()       
    
        self.question_heading = Label(self.question_frame, text = "FINISHED",
                                          font = "arial 14 bold", bg = background_color, padx = 100, pady = 20, borderwidth = 5, relief = "solid")
        self.question_heading.grid(row = 0)
    
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
