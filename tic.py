import tkinter 
from tkinter import *
from tkinter import messagebox

mw=tkinter.Tk()
mw.geometry('250x250')
mw.title('Tic-Tac-Toe')
mw.resizable(0,0)

btn1=StringVar()
btn2=StringVar()
btn3=StringVar()
btn4=StringVar()
btn5=StringVar()
btn6=StringVar()
btn7=StringVar()
btn8=StringVar()
btn9=StringVar()

    #frame1
f1=Frame(mw,bg='pink')
f1.pack(expand=True,fill=BOTH)

button1=Button(f1,textvariable=btn1,command=lambda:press(1),bg='black',fg='white')
button1.pack(side=LEFT,expand=True,fill=BOTH)

button2=Button(f1,textvariable=btn2,command=lambda:press(2),bg='black',fg='white')
button2.pack(side=LEFT,expand=True,fill=BOTH)

button3=Button(f1,textvariable=btn3,command=lambda:press(3),bg='black',fg='white')
button3.pack(side=LEFT,expand=True,fill=BOTH)

    #frame2
f2=Frame(mw)
f2.pack(expand=True,fill=BOTH)

button4=Button(f2,textvariable=btn4,command=lambda:press(4),bg='black',fg='white')
button4.pack(side=LEFT,expand=True,fill=BOTH)

button5=Button(f2,textvariable=btn5,command=lambda:press(5),bg='black',fg='white')
button5.pack(side=LEFT,expand=True,fill=BOTH)

button6=Button(f2,textvariable=btn6,command=lambda:press(6),bg='black',fg='white')
button6.pack(side=LEFT,expand=True,fill=BOTH)

    #frame3
f3=Frame(mw)
f3.pack(expand=True,fill=BOTH)

button7=Button(f3,textvariable=btn7,command=lambda:press(7),bg='black',fg='white')
button7.pack(side=LEFT,expand=True,fill=BOTH)

button8=Button(f3,textvariable=btn8,command=lambda:press(8),bg='black',fg='white')
button8.pack(side=LEFT,expand=True,fill=BOTH)

button9=Button(f3,textvariable=btn9,command=lambda:press(9),bg='black',fg='white')
button9.pack(side=LEFT,expand=True,fill=BOTH)

def clear():
    btn1.set('')
    btn2.set('')
    btn3.set('')
    btn4.set('')
    btn5.set('')
    btn6.set('')
    btn7.set('')
    btn8.set('')
    btn9.set('')

def again():
    global count
    global click
    count=0
    click=True
    box=messagebox.askquestion('Tic-Tac-Toe','Play Again?')
    if box=='yes':
        clear()
    elif box=='no':
         mw.destroy()

def check():
        if  (btn1.get()=='O' and btn2.get()=='O' and btn3.get()=='O'):
            messagebox.showinfo('Game Over','O wins')
            again()
            
        elif (btn1.get()=='X' and btn2.get()=='X' and btn3.get()=='X'):
            messagebox.showinfo('Game Over','X wins')
            again()
            
        elif (btn4.get()=='O' and btn5.get()=='O' and btn6.get()=='O'):
            messagebox.showinfo('Game Over','O wins')
            again()
            
        elif (btn4.get()=='X' and btn5.get()=='X' and btn6.get()=='X'):
             messagebox.showinfo('Game Over','X wins')
             again()
             
        elif (btn7.get()=='O' and btn8.get()=='O' and btn9.get()=='O'):
             messagebox.showinfo('Game Over','O wins')
             again()
             
        elif (btn7.get()=='X' and btn8.get()=='X' and btn9.get()=='X'):
             messagebox.showinfo('Game Over','X wins')
             again()
             
        elif (btn1.get()=='O' and btn5.get()=='O' and btn9.get()=='O'):
              messagebox.showinfo('Game Over','O wins')
              again()
              
        elif (btn1.get()=='X' and btn5.get()=='X' and btn9.get()=='X'):
             messagebox.showinfo('Game Over','X wins')
             again()
             
        elif (btn3.get()=='O' and btn5.get()=='O' and btn7.get()=='O'):
             messagebox.showinfo('Game Over','O wins')
        elif (btn3.get()=='X' and btn5.get()=='X' and btn7.get()=='X'):
             messagebox.showinfo('Game Over','X wins')
             again()
             
        elif (btn1.get()=='O' and btn4.get()=='O' and btn7.get()=='O'):
             messagebox.showinfo('Game Over','O wins')
             again()
             clear()
        elif (btn1.get()=='X' and btn4.get()=='X' and btn7.get()=='X'):
             messagebox.showinfo('Game Over','X wins')
             again()
             
        elif (btn2.get()=='O' and btn5.get()=='O' and btn8.get()=='O'):
             messagebox.showinfo('Game Over','O wins')
             again()
             
        elif (btn2.get()=='X' and btn5.get()=='X' and btn8.get()=='X'):
             messagebox.showinfo('Game Over','X wins')
             again()
             
        elif (btn3.get()=='O' and btn6.get()=='O' and btn9.get()=='O'):
             messagebox.showinfo('Game Over','O wins')
             again()
             
        elif (btn3.get()=='X' and btn6.get()=='X' and btn9.get()=='X'):
             messagebox.showinfo('Game Over','X wins')
             again()
        elif count==9:
            messagebox.showinfo('Game Over','DRAW')
            again()
            
             

def press(a):
    global click
    global count
    if click==True:
        if a==1:
            btn1.set('O')
        if a==2:
            btn2.set('O')
        if a==3:
            btn3.set('O')
        if a==4:
            btn4.set('O')
        if a==5:
            btn5.set('O')
        if a==6:
            btn6.set('O')
        if a==7:
            btn7.set('O')
        if a==8:
            btn8.set('O')
        if a==9:
            btn9.set('O')
        click=False
        count+=1
        check()
            
    elif click==False:
        if a==1:
            btn1.set('X')
        if a==2:
            btn2.set('X')
        if a==3:
            btn3.set('X')
        if a==4:
            btn4.set('X')
        if a==5:
            btn5.set('X')
        if a==6:
            btn6.set('X')
        if a==7:
            btn7.set('X')
        if a==8:
            btn8.set('X')
        if a==9:
            btn9.set('X')
        click=True
        count+=1
        check()

click=True
count=0
mw.mainloop()
