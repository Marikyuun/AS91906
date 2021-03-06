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
import_once = ['1']  # One element in the list that will be deleted so that the import function happens only once
question_summary_store=[]
answer_summary_store=[]
question_summary_index = 0

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
        self.quiz_start_button = Button(self.quiz_frame,
                                        text = "START",
                                        font = "calibri 16 bold", wrap = 290,
                                        bg = "cyan", width = 10,
                                        padx = 50, pady = 5, command = self.name)
        self.quiz_start_button.grid(row = 2, padx = 20, pady = 10)
        
        # Help Button (row 3)
        self.help_button = Button(self.quiz_frame, text = "Help",
                                  font = "calibri 16 bold", wrap = 290,
                                  bg = "cyan", width = 10,
                                  padx = 50, pady = 5, command = self.help)
        self.help_button.grid(row = 3, padx = 20, pady = 10)
    
    def name(self):
        Name(self)
    
    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text = "Click on the button that "
                                            "contains the correct answer."
                                            "\n\nWhen you are ready press START.",)

class Help:
    
    def __init__(self,parent):
        
        background = "cyan"
        
        # disable start button
        parent.quiz_start_button.config(state = DISABLED)        
        
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
        parent.quiz_start_button.config(state=NORMAL)
        self.help_box.destroy()


class Name:
    
    def __init__(self, parent):
        
        background = "cyan"
        
        # disable start button
        parent.quiz_start_button.config(state = DISABLED)
        
        # disable help button
        parent.help_button.config(state = DISABLED)        
        
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
        global name
        name = self.name_entry.get()
        self.question(parent)
    
    def close_name_entry(self, parent):
        # Put help button back to normal...
        parent.help_button.config(state = NORMAL)
        parent.quiz_start_button.config(state = NORMAL)
        self.name_box.destroy()
    
    def question(self, parent):
        self.name_box.destroy()
        Question(parent)
    

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
        question_summary_store.append(questions[question_index])
        answer_summary_store.append(temp_ans[0])
        
        print(questions[question_index])
        print(temp_ans)
        print(answer)
        
        a_no=random.randint(0,3)
        global a
        a=temp_ans[a_no]
        del temp_ans[a_no]
        if answer_control not in temp_ans:
            answer='a' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'a' will be the answer. 
        
        b_no=random.randint(0,2)
        global b
        b=temp_ans[b_no]
        del temp_ans[b_no]
        if answer!='a':
            if answer_control not in temp_ans:
                answer='b' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'b' will be the answer.            
        
        c_no=random.randint(0,1)
        global c
        c=temp_ans[c_no]
        del temp_ans[c_no]
        if answer!='a' and answer!='b':
            if answer_control not in temp_ans:
                answer='c' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'c' will be the answer.            
        
        d_no=0
        global d
        d=temp_ans[d_no]
        del temp_ans[d_no]
        if answer==answer_control:
            answer='d' #If the answer isn't 'a' 'b' or 'c', the answer is 'd'.
        
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
                                      font = "calibri 14 bold", bg = background_color, padx = 210, pady = 20, borderwidth = 2, relief = "solid")
        self.question_heading.grid(row = 0)        
        
        # Question (row 1)
        self.question_label = Label(self.question_frame,
                                         text = questions[question_index],
                                         font = "calibri 14 bold", wrap = 290,
                                         bg = "pale green", width = 30,
                                         padx = 100, pady = 20)
        self.question_label.grid(row = 1)
        
        del questions[question_index]
        del answers[question_index]
        
        # Answer 1 (row 2)
        self.question_answer_1_button = Button(self.question_frame,
                                           text = "a) "+a,
                                           font = "calibri 12", wrap = 290,
                                           bg = background_color, width = 30,
                                           padx = 100, pady = 20, command = self.answer_1)
        self.question_answer_1_button.grid(row = 2, pady = 10)
        
        # Answer 2 (row 3)
        self.question_answer_2_button = Button(self.question_frame,
                                           text = "b) "+b,
                                           font = "calibri 12", wrap = 290,
                                           bg = "coral", width = 30,
                                           padx = 100, pady = 20, command = self.answer_2)
        self.question_answer_2_button.grid(row = 3, pady = 10)
        
        # Answer 3 (row 4)
        self.question_answer_3_button = Button(self.question_frame,
                                           text = "c) "+c,
                                           font = "calibri 12", wrap = 290,
                                           bg = background_color, width = 30,
                                           padx = 100, pady = 20, command = self.answer_3)
        self.question_answer_3_button.grid(row = 4, pady = 10)            
        
        # Answer 4 (row 5)
        self.question_answer_4_button = Button(self.question_frame,
                                           text = "d) "+d,
                                           font = "calibri 12", wrap = 290,
                                           bg = "coral", width = 30,
                                           padx = 100, pady = 20, command = self.answer_4)
        self.question_answer_4_button.grid(row = 5, pady = 10)
        
        self.next_question_button = Button(self.question_frame,
                                  text = "Next",
                                  font = "calibri 12", wrap = 290,
                                  bg = "white",
                                  padx = 100, pady = 20, command = self.next_question,
                                  state = DISABLED)
        self.next_question_button.grid(row = 6, pady = 20, padx = 20)

    def next_question(self):
        
        if len(question_number)<1:  # CHANGE BACK TO 10 LATER
            question_number.append("1")
            question_index = random.randint(0,len(questions)-1)
            temp_ans = answers[question_index].split(",")
            answer = temp_ans[0]
            answer_control = temp_ans[0]
            question_summary_store.append(questions[question_index])
            answer_summary_store.append(temp_ans[0])            
            
            print(questions[question_index])
            print(answer)
            
            a_no=random.randint(0,3)
            global a
            a=temp_ans[a_no]
            del temp_ans[a_no]
            if answer_control not in temp_ans:
                answer='a' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'a' will be the answer. 
            b_no=random.randint(0,2)
            global b
            b=temp_ans[b_no]
            del temp_ans[b_no]
            if answer!='a':
                if answer_control not in temp_ans:
                    answer='b' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'b' will be the answer.            
            c_no=random.randint(0,1)
            global c
            c=temp_ans[c_no]
            del temp_ans[c_no]
            if answer!='a' and answer!='b':
                if answer_control not in temp_ans:
                    answer='c' #It deletes the random answer that was printed and checks the list to see if the answer is still in the list. If the answer has been deleted, then 'c' will be the answer.            
            d_no=0
            global d
            d=temp_ans[d_no]
            del temp_ans[d_no]
            
            if answer==answer_control:
                answer='d' #If the answer isn't 'a' 'b' or 'c', the answer is 'd'.
            
            self.next_question_button.config(state=DISABLED)
            self.question_answer_1_button.configure(text="a) "+a, state=NORMAL)
            self.question_answer_2_button.configure(text="b) "+b, state=NORMAL)
            self.question_answer_3_button.configure(text="c) "+c, state=NORMAL)
            self.question_answer_4_button.configure(text="d) "+d, state=NORMAL)
            self.question_label.configure(text = questions[question_index])
            self.question_heading.configure(text = ("Question "+str(len(question_number))))
            del questions[question_index]
            del answers[question_index]
            
        else:
            self.game_summary()
            
        
    def destroy_children(self,parent_frame):
        # Destroy all children from a frame
        # :param parent_frame: The frame to destory all children from
        
        for child in parent_frame.winfo_children():
            child.destroy()
        
        #destroy_children(self.question_frame)

    def score(self):
        score=len(scores)
        leaderboard_scores.append(str(score))
        print("Your score is",str(score)+"/10")
    
    def answer_1(self):
        if a in correct_answers:
            scores.append("1")
        print("Score: " + str((len(scores))))
        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)
    
    def answer_2(self):
        if b in correct_answers:
            scores.append("1")
        print("Score: " + str((len(scores))))
        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)        
    
    def answer_3(self):
        if c in correct_answers:
            scores.append("1")
        print("Score: " + str((len(scores))))
        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)        
    
    def answer_4(self):
        if d in correct_answers:
            scores.append("1")
        print("Score: " + str((len(scores))))
        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)
    
    def game_summary(self):
        Game_Summary(self)
    
    def close_question(self, parent):
        # Put start button back to normal...
        parent.quiz_start_button.config(state=NORMAL)
        parent.quiz_start_button.config(state = NORMAL)
        self.question_box.destroy()

class Game_Summary:
    
    def __init__(self,parent):
        
        parent.destroy_children(parent.question_frame)
        
        self.summary_label = Label(parent.question_frame, font = "calibri 20 bold underline",bg = 'coral', width = 35,
                                   text = "Quiz Summary", pady = 10, borderwidth = 1, relief = "solid")
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
        self.quit_button.grid(pady = 10, row = 4)
        
        if len(import_once) == 1:
            import_once.clear()
            self.importing()        

    
    def score(self,parent):
        parent.destroy_children(parent.question_frame)
        
        self.score_label = Label(parent.question_frame,
                                 text = "Total Score", borderwidth = 1, relief = "solid",
                                 font = "calibri 20 bold underline",
                                 bg = "coral", width = 35, pady = 10)
        self.score_label.grid(row = 0,)
        
        self.your_score_label = Label(parent.question_frame,
                                 text = "Your Score Is: " + str(len(scores)) + "/10",
                                 font = "calibri 20 bold",
                                 bg = "pale green", width = 35, pady = 10)
        self.your_score_label.grid(row = 1, pady = 10)
        
        self.back_button = Button(parent.question_frame,
                                     text = "Back",
                                     font = "calibri 12",
                                     bg = "coral", width = 10,
                                     command = parent.game_summary)
        self.back_button.grid(pady = 10, row = 2) 
    
    def question_summary(self,parent):
        
        print(question_summary_index+1)
        print(question_summary_store[question_summary_index])
        print(answer_summary_store[question_summary_index])
        
        parent.destroy_children(parent.question_frame)
        
        self.score_label = Label(parent.question_frame,
                                 text = "Question Summary", borderwidth = 1, relief = "solid",
                                 font = "calibri 20 bold underline",
                                 bg = "coral", width = 35, pady = 10)
        self.score_label.grid(row = 0, columnspan = 2)
        
        self.question_number_label = Label(parent.question_frame,
                                 text = "Question " + str(question_summary_index+1), wrap = 290,
                                 font = "calibri 14 bold", borderwidth = 1, relief = "solid",
                                 bg = "pale green", width = 35, pady = 10)
        self.question_number_label.grid(row = 1, pady = 20, columnspan = 2)
        
        self.question_label = Label(parent.question_frame,
                                 text = "Q: "+question_summary_store[question_summary_index], wrap = 290,
                                 font = "calibri 12", borderwidth = 1, relief = "solid",
                                 bg = "pale green", width = 43, pady = 10)
        self.question_label.grid(row = 2, pady = 20, columnspan = 2)
        
        self.answer_label = Label(parent.question_frame,
                                 text = "A: "+answer_summary_store[question_summary_index], wrap = 290,
                                 font = "calibri 12", borderwidth = 1, relief = "solid",
                                 bg = "pale green", width = 43, pady = 10)
        self.answer_label.grid(row = 3, pady = 20, columnspan = 2)
        
        self.previous_question_button = Button(parent.question_frame,
                                  text = "Previous Question",
                                  font = "calibri 12", wrap = 290,
                                  bg = "white",
                                  padx = 30, pady = 10, command = lambda : self.previous_question(parent))
        self.previous_question_button.grid(row = 4, column = 0, pady = 5, padx = 3)
        
        self.next_question_button = Button(parent.question_frame,
                                  text = "Next Question",
                                  font = "calibri 12", wrap = 290,
                                  bg = "white",
                                  padx = 30, pady = 10, command = lambda : self.next_question(parent))
        self.next_question_button.grid(row = 4, column = 1, pady = 5, padx = 3)
        
        self.back_button = Button(parent.question_frame,
                                     text = "Back",
                                     font = "calibri 12", borderwidth = 1, relief = "solid",
                                     bg = "coral", width = 10,
                                     command = parent.game_summary)
        self.back_button.grid(pady = 15, row = 5, columnspan = 2)
        
        if question_summary_index == 0:
            self.previous_question_button.configure(state = DISABLED)
        else:
            self.previous_question_button.configure(state = NORMAL)
        
        if question_summary_index + 1 == len(question_summary_store):
            self.next_question_button.configure(state = DISABLED)
        else:
            self.next_question_button.configure(state = NORMAL)
        
        print(question_summary_store)
        print(answer_summary_store)
    
    def next_question(self, parent):
        global question_summary_index
        question_summary_index = question_summary_index + 1
        print(question_summary_index)
        x = lambda : self.question_summary(parent)
        x()

    def previous_question(self, parent):
        global question_summary_index
        question_summary_index = question_summary_index - 1
        self.question_summary
        x = lambda : self.question_summary(parent)
        x()        

    
    def leaderboard(self,parent):
        parent.destroy_children(parent.question_frame)
        
        self.score_label = Label(parent.question_frame,
                                 text = "Leaderboard", borderwidth = 1, relief = "solid",
                                 font = "calibri 20 bold underline",
                                 bg = "coral", width = 35, pady = 10)
        self.score_label.grid(row = 0,)
        
        self.top_score_label = Label(parent.question_frame,
                                 text = "Top 10 Scores",
                                 font = "calibri 20 bold underline", borderwidth = 1,
                                 bg = "cyan", width = 35, pady = 10)
        self.top_score_label.grid(row = 1, pady = 10)        
        
        self.leaderboard_score_label = Label(parent.question_frame,
                                 text = "Placeholder", justify = LEFT,
                                 font = "calibri 20 bold", borderwidth = 1,
                                 bg = "pale green", width = 35, pady = 10)
        self.leaderboard_score_label.grid(row = 2)
        
        self.back_button = Button(parent.question_frame,
                                     text = "Back",
                                     font = "calibri 12", borderwidth = 1,
                                     bg = "coral", width = 10,
                                     command = parent.game_summary)
        self.back_button.grid(pady = 10, row = 3)
        
        print(leaderboard_names)
        print(leaderboard_scores)
        
        temp_scores = sorted(leaderboard_scores, reverse=True) #Temporary list to help with later sorting.
        for i in range(0,len(temp_scores)): #Turns the temp scores into integers so that it can be sorted.
            temp_scores[i]=int(temp_scores[i])
        temp_scores=sorted(temp_scores,reverse=True)
        for i in range(0,len(temp_scores)): #Turns the temp scores into a string.
            temp_scores[i]=str(temp_scores[i])
        print(temp_scores)
        
        n = 0
        words = ""
        
        for i in temp_scores:
            n = n + 1
            if n < 11:
                print(n)
                
                leaderboard_sort = leaderboard_scores.index(int(i))
                words = words + str(temp_scores.index(i)+1)+")    "+leaderboard_names[leaderboard_sort]+" "+str(leaderboard_scores[leaderboard_sort])+"/10\n"
                self.leaderboard_score_label.configure(text = words)
                del leaderboard_names[leaderboard_sort]
                del leaderboard_scores[leaderboard_sort]
    
    def quit(self):
        sys.exit()
    
    def importing(self):
        Importing()
    
    def start(self):
        Start()
    
    def destroy_children(self,parent_frame):
        # Destroy all children from a frame
        # :param parent_frame: The frame to destory all children from
        
        for child in parent_frame.winfo_children():
            child.destroy()  

class Importing:
    
    def __init__(self):
        
        reading=[]
        f=open("Scores.txt","r")
        for i in f.read().split("\n"): #Reads the scores.txt file and separates each line by splittng '\n'. Each line is then appended to reading to be used to append to leaderboard lists.
            reading.append(i)
        reading.pop()
        for i in reading:
            leaderboard_names.append(i.split(",")[0]) #Splits each item in reading at ',' and takes the first item.
            leaderboard_scores.append(int(i.split(",")[1])) #Splits each item in reading at ',' and takes the second item.
        f.close()
        
        self.exporting()
    
    def exporting(self):
        Exporting()


class Exporting:
    
    def __init__(self):
        
        global name
        score = len(scores)
        leaderboard_names.append(name)
        leaderboard_scores.append(score)
        print(name)
        print(score)
        print(leaderboard_names)
        print(leaderboard_scores)
        
        
        f=open("Scores.txt","w")
        for i in range(len(leaderboard_names)-1):
            f.write(leaderboard_names[i]+","+str(leaderboard_scores[i])+","+"\n") #Writes back old scores into 'Scores.txt' file to keep previous data.
        f.write(leaderboard_names[-1]+","+str(leaderboard_scores[-1])+","+"\n") #Writes in the current users scores into 'Scores.txt' to record new data.
        f.close()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    something = Quiz()
    root.mainloop()
