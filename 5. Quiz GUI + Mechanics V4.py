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
    def __init__(self,parent):
        
        file=open("Q.txt","r")
        for i in file.read().split("\n"): #reads the Q.txt file and appends every line individually to the questions list.
            questions.append(i)
        file.close()
        file=open("A.txt","r")
        for i in file.read().split("\n"): #reads the A.txt file and appends every line individually to the answers list.
            answers.append(i)
        questions.pop() #There is an extra empty item in the both the lists so this removes it.
        answers.pop()
        temp_answers=[]
        for i in range(len(answers)):
            correct_answers.append(answers[i].split(",")[0])
        
        print(questions)
        print(answers)
        print(correct_answers)
        
        question_index = random.randint(0,len(questions)-1)
        temp_ans = answers[question_index].split(",")
        answer = temp_ans[0]
        answer_control = temp_ans[0]
        print(questions[question_index])
        print(temp_ans)
        print(answer)        
        a_no=random.randint(0,3)
        a=temp_ans[a_no]
        del temp_ans[a_no]
        if answer_control not in temp_ans:
            answer='a' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'a' will be the answer. 
        
        b_no=random.randint(0,2)
        b=temp_ans[b_no]
        del temp_ans[b_no]
        if answer!='a':
            if answer_control not in temp_ans:
                answer='b' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'b' will be the answer.            
        
        c_no=random.randint(0,1)
        c=temp_ans[c_no]
        del temp_ans[c_no]
        if answer!='a' and answer!='b':
            if answer_control not in temp_ans:
                answer='c' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'c' will be the answer.            
        
        d_no=0
        d=temp_ans[d_no]
        del temp_ans[d_no]
        if answer==answer_control:
            answer='d' #If the answer isn't 'a' 'b' or 'c', the answer is 'd'.            
        
        print(a,b,c,d)
        
        background_color = "cyan"
        
        # disable start button
        parent.quiz_start_button.config(state = DISABLED)        
        
        # Sets up child window (ie: question box)
        self.question_box = Toplevel()
        
        # If users press cross at top, closes question box and 'releases' start button
        self.question_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_question, parent))        
        
        # Question Frame
        self.question_frame = Frame(self.question_box, width = 300, bg = "pale green")
        self.question_frame.grid()        
            
        # Set up Question Heading (row 0)
        self.question_heading = Label(self.question_frame, text = "Question "+str(len(question_number)),
                                      font = "arial 14 bold", bg = background_color, padx = 100, pady = 20, borderwidth = 5, relief = "solid")
        self.question_heading.grid(row = 0)
        
        question_index = random.randint(0,len(questions)-1)            
        
        # Question (row 1)
        self.question_label = Label(self.question_frame,
                                         text = questions[question_index],
                                         font = "Arial 12 bold", wrap = 290,
                                         bg = "pale green",
                                         padx = 100, pady = 20)
        self.question_label.grid(row = 1)
        
        # Answer 1 (row 2)
        self.question_answer_1_button = Button(self.question_frame,
                                           text = "a) "+a,
                                           font = "Arial 10", wrap = 290,
                                           bg = background_color,
                                           padx = 100, pady = 20, command = self.answer_1)
        self.question_answer_1_button.grid(row = 2, pady = 10)                   
        
        # Answer 2 (row 3)
        self.question_answer_2_button = Button(self.question_frame,
                                           text = "b) "+b,
                                           font = "Arial 10", wrap = 290,
                                           bg = "coral",
                                           padx = 100, pady = 20, command = self.answer_2)
        self.question_answer_2_button.grid(row = 3, pady = 10)            
        
        # Answer 3 (row 4)
        self.question_answer_3_button = Button(self.question_frame,
                                           text = "c) "+c,
                                           font = "Arial 10", wrap = 290,
                                           bg = background_color,
                                           padx = 100, pady = 20, command = self.answer_3)
        self.question_answer_3_button.grid(row = 4, pady = 10)            
        
        # Answer 4 (row 5)
        self.question_answer_4_button = Button(self.question_frame,
                                           text = "d) "+d,
                                           font = "Arial 10", wrap = 290,
                                           bg = "coral",
                                           padx = 100, pady = 20, command = self.answer_4)
        self.question_answer_4_button.grid(row = 5, pady = 10)        
        
        self.next_question_button = Button(self.question_frame,
                                  text = "Next",
                                  font = "Arial 10", wrap = 290,
                                  bg = "white",
                                  padx = 100, pady = 20, command = self.next_question,
                                  state = DISABLED)
        self.next_question_button.grid(row = 6, pady = 20)
        
    def next_question(self):
        if len(question_number)<10:
            question_number.append("1")
            question_index = random.randint(0,len(questions)-1)
            temp_ans = answers[question_index].split(",")
            answer = temp_ans[0]
            answer_control = temp_ans[0]                
            a_no=random.randint(0,3)
            a=temp_ans[a_no]
            del temp_ans[a_no]
            if answer_control not in temp_ans:
                answer='a' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'a' will be the answer. 
            b_no=random.randint(0,2)
            b=temp_ans[b_no]
            del temp_ans[b_no]
            if answer!='a':
                if answer_control not in temp_ans:
                    answer='b' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'b' will be the answer.            
            c_no=random.randint(0,1)
            c=temp_ans[c_no]
            del temp_ans[c_no]
            if answer!='a' and answer!='b':
                if answer_control not in temp_ans:
                    answer='c' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'c' will be the answer.            
            d_no=0
            d=temp_ans[d_no]
            del temp_ans[d_no]
            if answer==answer_control:
                answer='d' #If the answer isn't 'a' 'b' or 'c', the answer is 'd'.
            
            self.next_question_button.config(state=DISABLED)
            self.question_answer_1_button.configure(text="a) "+a, state=NORMAL)
            self.question_answer_2_button.configure(text="b) "+b, state=NORMAL)
            self.question_answer_3_button.configure(text="c) "+c, state=NORMAL)
            self.question_answer_4_button.configure(text="d) "+d, state=NORMAL)
            self.question_heading.configure(text=("Question "+str(len(question_number))))
        else:
            self.question_box.destroy()
            self.next_question_button.configure(command = self.score)
        
        def destroy_children(parent_frame):
            # Destroy all childen from a frame
            # :param parent_frame: The frame to destory all children from
            
            for child in parent_frame.winfo_children():
                child.destroy()
        
        #destroy_children(self.question_frame)

    def score(self):
        score=len(scores)
        leaderboard_scores.append(str(score))
        print("Your score is",str(score)+"/10")
        questions.clear()       
    
    
    def answer_1(self):
        q='a'
        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)
        print(q)
    
    def answer_2(self):
        q='b'
        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)        
        print(q)
    
    def answer_3(self):
        q='c'
        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)        
        print(q)
    
    def answer_4(self):
        q='d'
        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)        
        print(q)
    
    def close_question(self, parent):
        # Put start button back to normal...
        parent.quiz_start_button.config(state=NORMAL)
        self.question_box.destroy()
        
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz()
    root.mainloop()
