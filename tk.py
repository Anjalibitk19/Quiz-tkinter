#importing tkinter
from tkinter import *
root=Tk()

#function for correct answer
def core():
    global count
    count=0
    count+=1
    corel=Label(f1, text="WOOW IT'S A CORRECT ANSWER \n YOU GAIN 1 POINT").pack()
    
#function for wrong answer
def wr():
    wrl=Label(f1, text="OOPS IT'S A WRONG ANSWER").pack()


#if user press 1 
def op1():
    #1st question
    q1=Label(f1, text="WHAT WAS TWITTERS ORIGINAL NAME?").pack()
    op11=Button(f1, text="TWTTR", command=core).pack()
    op12=Button(f1, text="BLUE BIRD",command=wr).pack()
    op13=Button(f1, text="TWRR",command=wr).pack()
    op14=Button(f1, text="FLYING BIRD",command=wr).pack()
    

    #2nd question
    q2=Label(f1, text="WHICH ANIMAL IS CONSIDERED AS GOOD LUCK IN EUROPE?").pack()
    op21=Button(f1, text="DOG", command=wr).pack()
    op22=Button(f1, text="LADYBUG",command=core).pack()
    op23=Button(f1, text="LION",command=wr).pack()
    op24=Button(f1, text="SHEEP",command=wr).pack()
    
#instruction function
def op2():
    i1=Label(f1, text="for each question there is 1 point").pack()


#setting up window
root.geometry("666x666")



#setting title of the window
root.title("Anjali's quiz")

#creating frame
f1=Frame(root).pack()

#welcome labels inside the frame
we=Label(f1, text="**********************************************").pack()
wel=Label(f1, text="                 WELCOME                       ").pack()
welc=Label(f1, text="*********************************************").pack()

#setting options button
o1=Button(f1, text="PLAY GAME", command=op1).pack()
o2=Button(f1, text="SHOW INSTRUCTIONS", command=op2).pack()

#running mainloop
root.mainloop()
