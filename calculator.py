import tkinter
from tkinter import *
win=tkinter.Tk()

win.title("Calculator")
win.geometry('300x300')
win.resizable(0,0)

data=StringVar()
val=""
operator=''
a=0


def btn_click(num):
    global val
    val=val+str(num)
    data.set(val)

def operator_pressed(op):
    global a
    global val
    global operator
    operator=str(op)
    a=int(val)
    val=val+str(op)
    data.set(val)

def c_pressed():
    global val
    val=""
    data.set(val)

def result():
    global a
    global val
    global operator
    val2=val
    if operator=='+':
        x=int(val2.split('+')[1])
        c=a+x
        data.set(c)
        val=str(c)

    elif operator=='-':
        x=int(val2.split('-')[1])
        c=a-x
        data.set(c)
        val=str(c)

    elif operator=='x':
        x=int(val2.split('x')[1])
        c=a*x
        data.set(c)
        val=str(c)

    elif operator=='/':
        x=int(val2.split('/')[1])
        if x==0:
            z="Can't divide by zero"
            data.set(z)
            a=''
            val=''
        else:
            c=int(a/x)
            data.set(c)
            val=str(c)
        

lbl=Label(win,text='Input',bg='grey',anchor='se',textvariable=data,font=('verdana',22))
lbl.pack(expand=True,fill='both')

f1=Frame(win)
f1.pack(expand=True,fill='both')

f2=Frame(win)
f2.pack(expand=True,fill='both')

f3=Frame(win)
f3.pack(expand=True,fill='both')

f4=Frame(win)
f4.pack(expand=True,fill='both')


button1=Button(f1,text='7',fg='white',bg='black',command = lambda: btn_click(7))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f1,text='8',fg='white',bg='black',command = lambda: btn_click(8))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f1,text='9',fg='white',bg='black',command = lambda: btn_click(9))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f1,text='C',fg='white',bg='red',command=c_pressed)
button1.pack(side='left',expand=True,fill='both')

button1=Button(f2,text='4',fg='white',bg='black',command = lambda: btn_click(4))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f2,text='5',fg='white',bg='black',command = lambda: btn_click(5))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f2,text='6',fg='white',bg='black',command = lambda: btn_click(6))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f2,text='+',fg='white',bg='blue',command = lambda: operator_pressed('+'))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f3,text='1',fg='white',bg='black',command = lambda: btn_click(1))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f3,text='2',fg='white',bg='black',command = lambda: btn_click(2))
button1.pack(side='left',expand=True,fill='both')


button1=Button(f3,text='3',fg='white',bg='black',command = lambda: btn_click(3))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f3,text='-',fg='white',bg='blue',command = lambda: operator_pressed('-'))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f4,text='0',fg='white',bg='black',command = lambda: btn_click(0))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f4,text='=',fg='white',bg='black',command=result)
button1.pack(side='left',expand=True,fill='both')

button1=Button(f4,text='/',fg='white',bg='blue',command = lambda: operator_pressed('/'))
button1.pack(side='left',expand=True,fill='both')

button1=Button(f4,text='x',fg='white',bg='blue',command = lambda: operator_pressed('x'))
button1.pack(side='left',expand=True,fill='both')





