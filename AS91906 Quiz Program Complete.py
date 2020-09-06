from tkinter import *
from functools import partial  # To prevent unwanted windows
import random
import sys
import os
leaderboard_names = []
leaderboard_scores = []
questions = []
answers = []
scores = []
question_number = ["1"]
correct_answers = []
highscore_list = []
# One element in the list that will be deleted so that the import function happens only once
import_once = ['1']
question_summary_store = []
answer_summary_store = []
question_summary_index = 0
setup_once = [1]

class Quiz:

    def __init__(self):

        # Formatting variables
        background_color = "gold"
        button_color = "SteelBlue2"
        foreground_color = "black"
        
        if len(setup_once)==1:
            # Quiz Frame
            self.quiz_frame = Frame(bg=background_color,
                                    pady=10)
            self.quiz_frame.grid(sticky=NSEW)
            self.quiz_frame.columnconfigure(0, weight=1)
            self.quiz_frame.rowconfigure(0, weight=1)
    
            # Quiz Heading (row 0)
            self.quiz_heading_label = Label(self.quiz_frame,
                                            text="Geography Quiz",
                                            font="calibri 16 bold", bg=background_color,
                                            padx=10, pady=10)
            self.quiz_heading_label.grid(row=0, sticky=NSEW)
    
            # Start Button (row 2)
            self.quiz_start_button = Button(self.quiz_frame,
                                            text="START", fg=foreground_color,
                                            font="calibri 16 bold", wrap=290,
                                            bg=button_color, width=10,
                                            padx=50, pady=5, command=self.name)
            self.quiz_start_button.grid(row=2, padx=20, pady=10, sticky=NSEW)      
    
            # Help Button (row 3)
            self.help_button = Button(self.quiz_frame, text="Help",
                                      font="calibri 16 bold", wrap=290,
                                      bg=button_color, width=10, fg=foreground_color,
                                      padx=50, pady=5, command=self.help)
            self.help_button.grid(row=3, padx=20, pady=10, sticky=NSEW)
        
        else:
            self.name()

    def name(self):
        Name(self)

    def help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Click on the button that "
                                          "contains the correct answer."
                                          "\n\nWhen you are ready press START.",)


class Help:

    def __init__(self, parent):

        background = "gold"
        button_color = "SteelBlue2"
        foreground_color = "black"

        # disable start button
        parent.quiz_start_button.config(state=DISABLED)

        # disable help button
        parent.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()
        self.help_box.columnconfigure(0, weight=1)
        self.help_box.rowconfigure(0, weight=1)

        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol(
            'WM_DELETE_WINDOW', partial(self.close_help, parent))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300, bg=background)
        self.help_frame.grid(sticky=NSEW)
        self.help_frame.columnconfigure(0, weight=1)
        self.help_frame.rowconfigure(0, weight=1)

        # Set up help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 14 bold", bg=background)
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss Button (row 2)
        self.dismiss_button = Button(self.help_frame, text="Dismiss",
                                     width=10, bg=button_color,
                                     font="arial 10 bold", fg=foreground_color,
                                     command=partial(self.close_help, parent))
        self.dismiss_button.grid(row=2, pady=10)

    def close_help(self, parent):
        # Put help button back to normal...
        parent.help_button.config(state=NORMAL)
        parent.quiz_start_button.config(state=NORMAL)
        self.help_box.destroy()


class Name:

    def __init__(self, parent):

        background = "gold"
        foreground = "white"
        button_color = "SteelBlue2"
        
        if len(setup_once) == 1:
        
            # disable start button
            parent.quiz_start_button.config(state=DISABLED)
    
            # disable help button
            parent.help_button.config(state=DISABLED)
    
            # Sets up child window (ie: name entry box)
            self.name_box = Toplevel()
            self.name_box.columnconfigure(0, weight=1)
            self.name_box.rowconfigure(0, weight=1)
    
            # If users press cross at top, closes help and 'releases' help button
            self.name_box.protocol('WM_DELETE_WINDOW', partial(
                self.close_name_entry, parent))
    
            # Set up GUI Frame
            self.name_frame = Frame(self.name_box, width=300, bg=background)
            self.name_frame.grid(sticky=NSEW)
            self.name_frame.columnconfigure(0, weight=1)
            self.name_frame.rowconfigure(0, weight=1)
    
            # Name Entry Heading (row 0)
            self.name_label = Label(self.name_frame, font="calibri 20 bold",
                                    bg=background, width=30,
                                    text="Please Enter Your Username Below")
            self.name_label.grid(row=0)
    
            # User Name Entry Box (row 1)
            self.name_entry = Entry(
                self.name_frame, width=30, bg="white",
                font="calibri 16 bold", justify='center')
            self.name_entry.grid(row=1, pady=10)
    
            self.name_error_label = Label(self.name_frame, font="calibri 14",
                                          bg=background, width=35,
                                          text="")
            self.name_error_label.grid(row=2)
    
            # User Name Submit Box (row 2)
            self.name_submit_button = Button(self.name_frame,
                                             font="calibri 16 bold", width=30,
                                             pady=5, bg=button_color,
                                             text="Submit",
                                             command=partial(self.name_record, parent))
            self.name_submit_button.grid(row=3, pady=15)
        
        else:
            self.question(parent)

    def name_record(self, parent):
        global name
        name = self.name_entry.get()
        not_valid = [""]
        if name.strip() in not_valid:
            self.name_entry.configure(bg="IndianRed1")
            self.name_error_label.config(text="Please Enter A Valid Name")
        elif len(name) > 15:
            self.name_entry.configure(bg="IndianRed1")
            self.name_error_label.config(text="Your name must not exceed 15 characters.")            
        else:
            self.question(parent)

    def close_name_entry(self, parent):
        # Put help button back to normal...
        parent.help_button.config(state=NORMAL)
        parent.quiz_start_button.config(state=NORMAL)
        self.name_box.destroy()

    def question(self, parent):
        if len(setup_once) == 1:
            self.name_box.destroy()
        Question(parent)


class Question:

    def __init__(self, parent):

        background_color = "gold"
        button_color = "SteelBlue2"
        foreground_color = "white"
        
        setup_once.clear()

        file = open("Q.txt", "r")
        # reads the Q.txt file and appends every line individually to the questions list.
        for i in file.read().split("\n"):
            questions.append(i)
        file.close()
        file = open("A.txt", "r")
        # reads the A.txt file and appends every line individually to the answers list.
        for i in file.read().split("\n"):
            answers.append(i)
        # There is an extra empty item in the both the lists so this removes it.
        questions.pop()
        answers.pop()
        temp_answers = []
        for i in range(len(answers)):
            correct_answers.append(answers[i].split(",")[0])

        question_index = random.randint(0, len(questions) - 1)
        temp_ans = answers[question_index].split(",")
        answer = temp_ans[0]
        answer_control = temp_ans[0]
        question_summary_store.append(questions[question_index])
        answer_summary_store.append(temp_ans[0])

        a_no = random.randint(0, 3)
        global a
        a = temp_ans[a_no]
        del temp_ans[a_no]
        if answer_control not in temp_ans:
            answer = 'a'  # It deletes the random answer that was printed and
            # checks the list to see if the answer is still in the list.
            # If the answer has been deleted, then 'a' will be the answer.

        b_no = random.randint(0, 2)
        global b
        b = temp_ans[b_no]
        del temp_ans[b_no]
        if answer != 'a':
            if answer_control not in temp_ans:
                answer = 'b'  # It deletes the random answer that was printed
                # and checks the list to see if the answer is still in the list.
                # If the answer has been deleted, then 'b' will be the answer.

        c_no = random.randint(0, 1)
        global c
        c = temp_ans[c_no]
        del temp_ans[c_no]
        if answer != 'a' and answer != 'b':
            if answer_control not in temp_ans:
                answer = 'c'  # It deletes the random answer that was printed
                # and checks the list to see if the answer is still in the list.
                # If the answer has been deleted, then 'c' will be the answer.

        d_no = 0
        global d
        d = temp_ans[d_no]
        del temp_ans[d_no]
        if answer == answer_control:
            # If the answer isn't 'a' 'b' or 'c', the answer is 'd'.
            answer = 'd'

        if len(setup_once) == 1:
            # disable start button
            parent.quiz_start_button.config(state=DISABLED)

        # Sets up child window (ie: question box)
        self.question_box = Toplevel()
        self.question_box.columnconfigure(0, weight=1)
        self.question_box.rowconfigure(0, weight=1)    

        # If users press cross at top, closes question box and 'releases' start button
        self.question_box.protocol('WM_DELETE_WINDOW',
                                   partial(self.close_question, parent))

        # Question Frame
        self.question_frame = Frame(
            self.question_box, width=300, bg=background_color)
        self.question_frame.grid(sticky=NSEW)

        # Set up Question Heading (row 0)
        self.question_heading = Label(self.question_frame, text="Question " + str(len(question_number)),
                                      font="calibri 16 bold",
                                      bg=background_color, padx=210, pady=20,
                                      borderwidth=2, relief="solid")
        self.question_heading.grid(row=0)

        # Question (row 1)
        self.question_label = Label(self.question_frame,
                                    text=questions[question_index],
                                    font="calibri 14 bold", wrap=290,
                                    bg=background_color, width=30,
                                    padx=100, pady=20)
        self.question_label.grid(row=1)

        del questions[question_index]
        del answers[question_index]

        # Answer 1 (row 2)
        self.question_answer_1_button = Button(self.question_frame,
                                               text="a) " + a,
                                               font="calibri 12", wrap=290,
                                               bg=foreground_color, width=30,
                                               padx=100, pady=20,
                                               command=self.answer_1)
        self.question_answer_1_button.grid(row=2, pady=10)

        # Answer 2 (row 3)
        self.question_answer_2_button = Button(self.question_frame,
                                               text="b) " + b,
                                               font="calibri 12", wrap=290,
                                               bg=foreground_color, width=30,
                                               padx=100, pady=20,
                                               command=self.answer_2)
        self.question_answer_2_button.grid(row=3, pady=10)

        # Answer 3 (row 4)
        self.question_answer_3_button = Button(self.question_frame,
                                               text="c) " + c,
                                               font="calibri 12", wrap=290,
                                               bg=foreground_color, width=30,
                                               padx=100, pady=20,
                                               command=self.answer_3)
        self.question_answer_3_button.grid(row=4, pady=10)

        # Answer 4 (row 5)
        self.question_answer_4_button = Button(self.question_frame,
                                               text="d) " + d,
                                               font="calibri 12", wrap=290,
                                               bg=foreground_color, width=30,
                                               padx=100, pady=20,
                                               command=self.answer_4)
        self.question_answer_4_button.grid(row=5, pady=10)

        self.next_question_button = Button(self.question_frame,
                                           text="Next",
                                           font="calibri 12", wrap=290,
                                           bg=button_color,
                                           padx=50, pady=10,
                                           command=self.next_question,
                                           state=DISABLED)
        self.next_question_button.grid(row=6, pady=20, padx=20)

    def next_question(self):

        foreground_color = "white"

        if len(question_number) < 2:  # CHANGE BACK TO 10 LATER
            question_number.append("1")
            question_index = random.randint(0, len(questions) - 1)
            temp_ans = answers[question_index].split(",")
            answer = temp_ans[0]
            answer_control = temp_ans[0]
            question_summary_store.append(questions[question_index])
            answer_summary_store.append(temp_ans[0])

            a_no = random.randint(0, 3)
            global a
            a = temp_ans[a_no]
            del temp_ans[a_no]
            if answer_control not in temp_ans:
                answer = 'a'  # It deletes the random answer that was printed
                # and checks the list to see if the answer is still in the list.
                # If the answer has been deleted, then 'a' will be the answer.
            b_no = random.randint(0, 2)
            global b
            b = temp_ans[b_no]
            del temp_ans[b_no]
            if answer != 'a':
                if answer_control not in temp_ans:
                    answer = 'b'  # It deletes the random answer that was printed
                    # and checks the list to see if the answer is still in the list.
                    # If the answer has been deleted, then 'b' will be the answer.
            c_no = random.randint(0, 1)
            global c
            c = temp_ans[c_no]
            del temp_ans[c_no]
            if answer != 'a' and answer != 'b':
                if answer_control not in temp_ans:
                    answer = 'c'  # It deletes the random answer that was printed
                    # and checks the list to see if the answer is still in the list.
                    # If the answer has been deleted, then 'c' will be the answer.
            d_no = 0
            global d
            d = temp_ans[d_no]
            del temp_ans[d_no]

            if answer == answer_control:
                # If the answer isn't 'a' 'b' or 'c', the answer is 'd'.
                answer = 'd'

            self.next_question_button.config(state=DISABLED)
            self.question_answer_1_button.configure(
                text="a) " + a, state=NORMAL, bg=foreground_color)
            self.question_answer_2_button.configure(
                text="b) " + b, state=NORMAL, bg=foreground_color)
            self.question_answer_3_button.configure(
                text="c) " + c, state=NORMAL, bg=foreground_color)
            self.question_answer_4_button.configure(
                text="d) " + d, state=NORMAL, bg=foreground_color)
            self.question_label.configure(text=questions[question_index])
            self.question_heading.configure(
                text=("Question " + str(len(question_number))))
            del questions[question_index]
            del answers[question_index]

        else:
            self.game_summary()

    def destroy_children(self, parent_frame):
        # Destroy all children from a frame
        # :param parent_frame: The frame to destory all children from

        for child in parent_frame.winfo_children():
            child.destroy()

        # destroy_children(self.question_frame)

    def score(self):
        score = len(scores)
        leaderboard_scores.append(str(score))

    def answer_1(self):
        if a in correct_answers:
            scores.append("1")
            self.question_answer_1_button.config(bg="pale green")
        else:
            self.question_answer_1_button.config(bg="IndianRed1")

        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)

    def answer_2(self):
        if b in correct_answers:
            scores.append("1")
            self.question_answer_2_button.config(bg="pale green")
        else:
            self.question_answer_2_button.config(bg="IndianRed1")

        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)

    def answer_3(self):
        if c in correct_answers:
            scores.append("1")
            self.question_answer_3_button.config(bg="pale green")
        else:
            self.question_answer_3_button.config(bg="IndianRed1")

        self.question_answer_1_button.configure(state=DISABLED)
        self.question_answer_2_button.configure(state=DISABLED)
        self.question_answer_3_button.configure(state=DISABLED)
        self.question_answer_4_button.configure(state=DISABLED)
        self.next_question_button.config(state=NORMAL)

    def answer_4(self):
        if d in correct_answers:
            scores.append("1")
            self.question_answer_4_button.config(bg="pale green")
        else:
            self.question_answer_4_button.config(bg="IndianRed1")

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
        # Put help button back to normal...
        parent.help_button.config(state=NORMAL)        
        self.question_box.destroy()


class Game_Summary:

    def __init__(self, parent):

        background_color = "gold"
        button_color = "SteelBlue2"
        foreground_color = "white"

        parent.destroy_children(parent.question_frame)

        self.summary_label = Label(parent.question_frame,
                                   font="calibri 20 bold underline",
                                   bg=background_color, width=38,
                                   text="Quiz Summary", pady=10,
                                   borderwidth=3, relief="solid")
        self.summary_label.grid(row=0, columnspan=2)

        self.score_button = Button(parent.question_frame,
                                   text="View Score",
                                   font="calibri 13 bold", wrap=290,
                                   bg=button_color, width=30,
                                   padx=100, pady=20,
                                   command=lambda: self.score(parent))
        self.score_button.grid(row=1, pady=20, padx=20, columnspan=2)

        self.question_summary_button = Button(parent.question_frame,
                                              text="Question Summary",
                                              font="calibri 13 bold", wrap=290,
                                              bg=button_color, width=30,
                                              padx=100, pady=20,
                                              command=lambda: self.question_summary(parent))
        self.question_summary_button.grid(row=2, pady=20, padx=20, columnspan=2)

        self.leaderboard_button = Button(parent.question_frame,
                                         text="Leaderboard",
                                         font="calibri 13 bold", wrap=290,
                                         bg=button_color, width=30,
                                         padx=100, pady=20,
                                         command=lambda: self.leaderboard(parent))
        self.leaderboard_button.grid(row=3, pady=20, padx=20, columnspan=2)

        self.quit_button = Button(parent.question_frame,
                                  text="Quit",
                                  font="calibri 12",
                                  bg="IndianRed1", width=10,
                                  command=self.quit)
        self.quit_button.grid(pady=10, row=4, column=0)
        
        self.restart_button = Button(parent.question_frame,
                                  text="Restart",
                                  font="calibri 12",
                                  bg="pale green", width=10,
                                  command=lambda : self.restart(parent))
        self.restart_button.grid(pady=10, row=4, column=1)

        if len(import_once) == 1:
            import_once.clear()
            self.importing()

    def score(self, parent):

        background_color = "gold"
        button_color = "SteelBlue2"
        foreground_color = "white"

        parent.destroy_children(parent.question_frame)

        self.score_label = Label(parent.question_frame,
                                 text="Total Score", borderwidth=1, relief="solid",
                                 font="calibri 20 bold underline",
                                 bg=background_color, width=35, pady=10)
        self.score_label.grid(row=0)

        self.your_score_label = Label(parent.question_frame,
                                      text="Your Score Is: " +
                                      str(len(scores)) + "/10",
                                      font="calibri 20 bold",
                                      bg=background_color, width=35, pady=10)
        self.your_score_label.grid(row=1, pady=10)
        
        self.all_score_label = Label(parent.question_frame,
                                      text="Placeholder", font="calibri 20 bold",
                                      bg=background_color, width=35, pady=10)
        self.all_score_label.grid(row=2, pady=10)
        
        self.your_highscore_label = Label(parent.question_frame,
                                      text="Placeholder", font="calibri 20 bold",
                                      bg=background_color, width=35, pady=10)
        self.your_highscore_label.grid(row=3, pady=10)        

        self.back_button = Button(parent.question_frame,
                                  text="Back",
                                  font="calibri 12",
                                  bg=foreground_color, width=10,
                                  command=parent.game_summary)
        self.back_button.grid(pady=10, row=4)
        
        
        leaderboard_names2 = leaderboard_names.copy()
        leaderboard_scores2 = leaderboard_scores.copy()
        n = 0
        words = ""
        
        for i in leaderboard_names:
            if i==leaderboard_names[-1]: #This looks for names that are the same, which would mean that it is the user's past score.
                n=n+1
                index=leaderboard_names.index(i)
                highscore_list.append(str(leaderboard_scores[index]))
                del leaderboard_names[index]
                del leaderboard_scores[index]
        highscore_list.sort(reverse=True)
        
        n = 0
        for i in range(0, len(highscore_list)):
            if n < 10:
                global name
                n = n+1
                words = words + str(n)+") "+str(name)+"     "+str(highscore_list[i])+"/10     \n"
        self.all_score_label.configure(text="Top 10 Scores:\n"+words)
        self.your_highscore_label.configure(text="Your highscore is "+(highscore_list[-1]).split(",")[0]+"/10")

    def question_summary(self, parent):

        background_color = "gold"
        button_color = "SteelBlue2"
        foreground_color = "white"

        parent.destroy_children(parent.question_frame)

        self.score_label = Label(parent.question_frame,
                                 text="Question Summary", borderwidth=1, relief="solid",
                                 font="calibri 20 bold underline",
                                 bg=background_color, width=35, pady=10)
        self.score_label.grid(row=0, columnspan=2)

        self.question_number_label = Label(parent.question_frame,
                                           text="Question " + str(question_summary_index + 1), wrap=290,
                                           font="calibri 14 bold", borderwidth=1, relief="solid",
                                           bg=background_color, width=35, pady=10)
        self.question_number_label.grid(row=1, pady=20, columnspan=2)

        self.question_label = Label(parent.question_frame,
                                    text="Q: " + question_summary_store[question_summary_index], wrap=290,
                                    font="calibri 12", borderwidth=1, relief="solid",
                                    bg=background_color, width=43, pady=10)
        self.question_label.grid(row=2, pady=20, columnspan=2)

        self.answer_label = Label(parent.question_frame,
                                  text="A: " + answer_summary_store[question_summary_index], wrap=290,
                                  font="calibri 12", borderwidth=1, relief="solid",
                                  bg=background_color, width=43, pady=10)
        self.answer_label.grid(row=3, pady=20, columnspan=2)

        self.previous_question_button = Button(parent.question_frame,
                                               text="Previous Question",
                                               font="calibri 12", wrap=290,
                                               bg=button_color,
                                               padx=30, pady=10, command=lambda: self.previous_question(parent))
        self.previous_question_button.grid(row=4, column=0, pady=5, padx=3)

        self.next_question_button = Button(parent.question_frame,
                                           text="Next Question",
                                           font="calibri 12", wrap=290,
                                           bg=button_color,
                                           padx=30, pady=10, command=lambda: self.next_question(parent))
        self.next_question_button.grid(row=4, column=1, pady=5, padx=3)

        self.back_button = Button(parent.question_frame,
                                  text="Back",
                                  font="calibri 12", borderwidth=1, relief="solid",
                                  bg="white", width=10,
                                  command=parent.game_summary)
        self.back_button.grid(pady=15, row=5, columnspan=2)

        if question_summary_index == 0:
            self.previous_question_button.configure(state=DISABLED)
        else:
            self.previous_question_button.configure(state=NORMAL)

        if question_summary_index + 1 == len(question_summary_store):
            self.next_question_button.configure(state=DISABLED)
        else:
            self.next_question_button.configure(state=NORMAL)

    def next_question(self, parent):
        global question_summary_index
        question_summary_index = question_summary_index + 1

        def x(): return self.question_summary(parent)
        x()

    def previous_question(self, parent):
        global question_summary_index
        question_summary_index = question_summary_index - 1
        self.question_summary

        def x(): return self.question_summary(parent)
        x()

    def leaderboard(self, parent):

        background_color = "gold"
        button_color = "SteelBlue2"
        foreground_color = "white"

        parent.destroy_children(parent.question_frame)

        self.score_label = Label(parent.question_frame,
                                 text="Leaderboard", borderwidth=1, relief="solid",
                                 font="calibri 20 bold underline",
                                 bg=background_color, width=35, pady=10)
        self.score_label.grid(row=0,)

        self.top_score_label = Label(parent.question_frame,
                                     text="Top 10 Scores",
                                     font="calibri 20 bold underline", borderwidth=1,
                                     bg=background_color, width=35, pady=10)
        self.top_score_label.grid(row=1, pady=10)

        self.leaderboard_score_label = Label(parent.question_frame,
                                             text="Placeholder", justify=LEFT,
                                             font="calibri 20 bold", borderwidth=1,
                                             bg=background_color, width=35, pady=10)
        self.leaderboard_score_label.grid(row=2)

        self.back_button = Button(parent.question_frame,
                                  text="Back",
                                  font="calibri 12", borderwidth=1,
                                  bg="white", width=10,
                                  command=parent.game_summary)
        self.back_button.grid(pady=10, row=3)

        # Temporary list to help with later sorting.
        temp_scores = sorted(leaderboard_scores, reverse=True)
        # Turns the temp scores into integers so that it can be sorted.
        for i in range(0, len(temp_scores)):
            temp_scores[i] = int(temp_scores[i])
        temp_scores = sorted(temp_scores, reverse=True)
        # Turns the temp scores into a string.
        for i in range(0, len(temp_scores)):
            temp_scores[i] = str(temp_scores[i])
        leaderboard_names2 = leaderboard_names.copy()
        leaderboard_scores2 = leaderboard_scores.copy()

        n = 0
        words = ""

        for i in temp_scores:
            n = n + 1
            if n < 11:
                leaderboard_sort = leaderboard_scores2.index(int(i))
                leaderboard_sort = leaderboard_scores2.index(int(i))
                words = (words + str(temp_scores.index(i) + 1) + ")    " +
                         leaderboard_names2[leaderboard_sort] + " " + str(
                    leaderboard_scores2[leaderboard_sort]) + "/10\n")
                self.leaderboard_score_label.configure(text=words)
                del leaderboard_names2[leaderboard_sort]
                del leaderboard_scores2[leaderboard_sort]

    def quit(self):
        sys.exit()
    
    def restart(self,parent):
        global leaderboard_names
        leaderboard_names = []
        global leaderboard_scores
        leaderboard_scores = []
        global questions
        questions = []
        global answers
        answers = []
        global scores
        scores = []
        global question_number
        question_number = ["1"]
        global corect_answers
        correct_answers = []
        global highscore_list
        highscore_list = []
        # One element in the list that will be deleted so that the import function happens only once
        global import_once
        import_once = ['1']
        global question_summary_store
        question_summary_store = []
        global answer_summary_store
        answer_summary_store = []
        global question_summary_index
        question_summary_index = 0
        self.quiz(parent)
    
    def quiz(self,parent):
        parent.question_box.destroy()
        Quiz()
    
    def importing(self):
        Importing()

    def destroy_children(self, parent_frame):
        # Destroy all children from a frame
        # :param parent_frame: The frame to destory all children from

        for child in parent_frame.winfo_children():
            child.destroy()


class Importing:

    def __init__(self):

        reading = []
        f = open("Scores.txt", "r")
        # Reads the scores.txt file and separates each line by splittng '\n'.
        # Each line is then appended to reading to be used
        # to append to leaderboard lists.
        for i in f.read().split("\n"):
            reading.append(i)
        reading.pop()
        for i in reading:
            # Splits each item in reading at ',' and takes the first item.
            leaderboard_names.append(i.split(",")[0])
            # Splits each item in reading at ',' and takes the second item.
            leaderboard_scores.append(int(i.split(",")[1]))
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

        f = open("Scores.txt", "w")
        for i in range(len(leaderboard_names) - 1):
            # Writes back old scores into 'Scores.txt' file
            # to keep previous data.
            f.write(leaderboard_names[i] + "," +
                    str(leaderboard_scores[i]) + "," + "\n")
        # Writes in the current users scores into 'Scores.txt'
        # to record new data.
        f.write(leaderboard_names[-1] + "," +
                str(leaderboard_scores[-1]) + "," + "\n")
        f.close()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Geography Quiz")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    something = Quiz()
    root.mainloop()
