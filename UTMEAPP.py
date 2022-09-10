from lib2to3.pytree import LeafPattern
from tkinter import *
from tkinter import mainloop
from xml.etree.ElementTree import C14NWriterTarget
from tkinter.messagebox import *
from tkinter.messagebox import askquestion
from PIL import Image, ImageTk, ImageDraw
from random import randint



def grade_checker(num):
    score1 = 0
    """
    score2 = 0
    score3 =0
    score4 = 0
    score5 = 0 
    """

    if num == "A1":
        score1 += 6

    elif num == "B2":
        score1 += 5

    elif num == 'B3':
         score1 += 4

    elif num == 'C4':
        score1 += 3

    elif num == 'C5':
        score1 += 2

    elif num == 'C6':
        score1 += 1


    return score1





def sitting1(num1, num2, num3, num4, num5):
    total = num1 + num2 + num3 + num4 + num5
    final_total = total + 10
    UTMER = eval(entry01.get())/400
    UTME = UTMER * 60
    finale = final_total + UTME

    return finale


def sitting2(num1, num2, num3, num4, num5):
    total = num1 + num2 + num3 + num4 + num5
    final_total = total + 6
    UTMER = eval(entry01.get())/400
    UTME = UTMER * 60
    finale = final_total + UTME

    return finale



def sub_main():

    sub1 = eval(entry1.get())
    sub2 = eval(entry2.get())
    sub3 = eval(entry3.get())
    sub4 = eval(entry4.get())
    sub5 = eval(entry5.get())


def grade_entry1():
    grade1 = str(entry001.get())
    grade2 = str(entry002.get())
    grade3 = str(entry003.get())
    grade4 = str(entry004.get())
    grade5 = str(entry005.get())


    check1 = grade_checker(grade1)
    check2 = grade_checker(grade2)
    check3 = grade_checker(grade3)
    check4 = grade_checker(grade4)
    check5 = grade_checker(grade5)

    sit = sitting1(check1,check2,check3, check4, check5 )
    output_label.configure(text=" Your Screening Point : {:.1f}".format(sit))



def grade_entry2():
    grade1 = str(entry001.get())
    grade2 = str(entry002.get())
    grade3 = str(entry003.get())
    grade4 = str(entry004.get())
    grade5 = str(entry005.get())


    check1 = grade_checker(grade1)
    check2 = grade_checker(grade2)
    check3 = grade_checker(grade3)
    check4 = grade_checker(grade4)
    check5 = grade_checker(grade5)

    sit = sitting2(check1,check2,check3, check4, check5 )

    output_label.configure(text=" Your Screening Point : {:.1f}".format(sit))
    


def stop_operation():
    answer = askquestion(title="Quit", message="Really Quit?")
    if answer == "yes":
        root.destroy()




root = Tk()
root.title('Screening Point Application')




message_label1 = Label(text='Subject', font=("Roman", 11))
message_label2 = Label(text='Grade', font=("Roman", 11))

message_label1.grid(row=0, column=0)
message_label2.grid(row=0, column=2)

output_label = Label(font=('Roman', 11))
output_label.grid(row=8, column=0, columnspan=3)


entry1 = Entry(font=('Italic', 11), width=14)
entry2 = Entry(font=('Italic', 11), width=14)
entry3 = Entry(font=('Italic', 11), width=14)
entry4 = Entry(font=('Italic', 11), width=14)
entry5 = Entry(font=('Italic', 11), width=14)

entry1.grid(row=1, column=0)
entry2.grid(row=2, column=0)
entry3.grid(row=3, column=0)
entry4.grid(row=4, column=0)
entry5.grid(row=5, column=0)


entry001 = Entry(font=('Italic', 11), width=10)
entry002 = Entry(font=('Italic', 11), width=10)
entry003 = Entry(font=('Italic', 11), width=10)
entry004 = Entry(font=('Italic', 11), width=10)
entry005 = Entry(font=('Italic', 11), width=10)

entry001.grid(row=1, column=2)
entry002.grid(row=2, column=2)
entry003.grid(row=3, column=2)
entry004.grid(row=4, column=2)
entry005.grid(row=5, column=2)


entry01_label = Label(text='UTME Score',font=('Italic', 11), width=10)
entry01_label.grid(row=9, column=0)

entry01 = Entry(font=('Italic', 14), width=5)
entry01.grid(row=9, column=1)

calc_button1 = Button(text='One Sitting', font=('Roman', 14), command=grade_entry1)
calc_button2 = Button(text='Two Sitting', font=('Roman', 14), command=grade_entry2)
calc_button5 = Button(text='Quit', font=('Roman', 14), command=stop_operation)

calc_button1.grid(row=10, column=0)
calc_button2.grid(row=10, column=2)
calc_button5.grid(row=11, column=1)

mainloop()
