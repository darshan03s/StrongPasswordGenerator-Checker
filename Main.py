from tkinter import *
import string
import random
import subprocess

gui=Tk()
gui.title("Strong Password Generator")

#[----------------------------------------------Password Generator------------------------------------------------------------------]
len=IntVar()
lowlen=IntVar()
uplen=IntVar()
diglen=IntVar()
symlen=IntVar()
pstr1=StringVar()
pstr2=StringVar()
sum=IntVar()

lower=string.ascii_lowercase
upper=string.ascii_uppercase
digit=string.digits
symbol=string.punctuation
str=lower+upper+digit+symbol


def clear1():
    passentry.delete(0, END)
    lene.delete(0, END)

def btnc():
    pwd = random.sample(str, len.get())
    password = "".join(pwd)
    passentry.insert(0, password)

def clear2():
    passentry2.delete(0, END)
    lowl.delete(0, END)
    upl.delete(0, END)
    digl.delete(0, END)
    syml.delete(0, END)

def btnc2():
   str2 = random.choices(lower, k=lowlen.get()) + random.choices(upper, k=uplen.get()) + random.choices(digit, k=diglen.get()) + random.choices(symbol, k=symlen.get())
   random.shuffle(str2)
   password2 = "".join(str2)
   passentry2.insert(0, password2)

def cleara1():
    passentry.delete(0, END)

def cleara2():
    passentry2.delete(0, END)

#Password Strength
def newwindow():
 cmd='python checkPassword.py'
 p=subprocess.Popen(cmd, shell=True)

length=Label(gui, text="Enter Length:", font="calibri 12 bold")
length.place(x=100,y=450)
lene=Entry(gui, textvariable=len, width=45)
lene.place(x=205, y=450)

passlabel=Label(gui,text="Password:", font="calibri 12 bold")
passlabel.place(x=100, y=480)
passentry=Entry(gui, width=45)
passentry.place(x=205, y=480)

btn1=Button(gui,text="Generate Password",borderwidth=0,font="Calibri 0 bold", command=btnc)
btn1.place(x=170, y=510)
clearbutton1=Button(gui, text="Clear All",borderwidth=0,font="Calibri 0 bold", command=clear1)
clearbutton1.place(x=280, y=550)
cleara1=Button(gui, text="Clear Password",borderwidth=0,font="Calibri 0 bold", command=cleara1)
cleara1.place(x=330, y=510)

#Choose Characters
lowlength=Label(gui, text="Lowercase characters :", font="calibri 12 bold")
lowlength.place(x=530,y=450)
lowl=Entry(gui, textvariable=lowlen, width=5)
lowl.place(x=700, y=452)

uplength=Label(gui, text="Uppercase characters :", font="calibri 12 bold")
uplength.place(x=760,y=450)
upl=Entry(gui, textvariable=uplen, width=5)
upl.place(x=930, y=450)

diglength=Label(gui, text="Digits :", font="calibri 12 bold")
diglength.place(x=990,y=450)
digl=Entry(gui, textvariable=diglen, width=5)
digl.place(x=1050, y=450)

symlength=Label(gui, text="Symbols :", font="calibri 12 bold")
symlength.place(x=1120,y=450)
syml=Entry(gui, textvariable=symlen, width=5)
syml.place(x=1200, y=450)

passlabel2=Label(gui,text="Password:", font="calibri 12 bold")
passlabel2.place(x=560, y=480)
passentry2=Entry(gui, width=100)
passentry2.place(x=640, y=480)

btn2=Button(gui,text="Generate Password", command=btnc2,borderwidth=0, font="Calibri 0 bold")
btn2.place(x=740, y=510)
clearbutton2=Button(gui, text="Clear All", command=clear2,borderwidth=0, font="Calibri 0 bold")
clearbutton2.place(x=660, y=510)
cleara2=Button(gui, text="Clear Password", command=cleara2,borderwidth=0, font="Calibri 0 bold")
cleara2.place(x=900, y=510)

#[-----------------------------------------------------Password Generator-------------------------------------------------------------]

pcbtn=Button(gui, text="Check Password strength here", font="Calibri 15 bold", command=newwindow)
pcbtn.place(x=550,y=600)

gui.state('zoomed')
gui.mainloop()
