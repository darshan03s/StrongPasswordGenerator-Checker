from tkinter import *
import re

myGui = Tk()
myGui.geometry('700x500')
myGui.title('Password Strength Checker')
guiFont = font = dict(family='Courier New, monospaced', size=18, color='#7f7f7f')

def checkPassword():
 #Common Password
    with open('common.txt', 'r') as f:
     common = f.read().splitlines()

    strength = ['Password can not be Blank', 'Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong','Weak! This is a commonly used Password']
    score = 1
    password = ePassword.get()

    if len(password) == 0:
        passwordStrength.set(strength[0])
        return

    if len(password) <= 4:
        passwordStrength.set(strength[1])
        return

    if password in common :
        passwordStrength.set(strength[6])
        return

    if len(password) >= 8:
        score += 2

    if re.search("[0-9]", password):
        score += 1

    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 1

    if re.search("(?=.*[@#$%^&+=!]).*$ ", password):
        score += 1


    passwordStrength.set(strength[score])

passwordStrength = StringVar()
eLabel = Label(myGui, text="Please Enter you Password:   ", font="Calibri 15 bold")
eLabel.pack(pady=10)
ePassword = Entry(myGui, width=50)
ePassword.pack()

stris = Label(myGui, text="Strength is :", font="Calibri 15 bold")
stris.place(x=150 ,y=80)
checkStrLab = Label(myGui,textvariable=passwordStrength, font="calibri 15 bold", justify=CENTER)
checkStrLab.place(x=270, y=82)

checkStrBtn = Button(myGui, text="Check Strength", command=checkPassword, font="Calibri 0 bold")
checkStrBtn.place(x=300, y=120)

Passclbl=Label(myGui, text=" A Strong Password has :\n \n"
                           "* Atleast 8 chacarcters\n"
                           "* A mix of Uppercase and Lowercase characters\n"
                           "* A mix of numbers and signs\n"
                           "* Must not be a commonly used Password\n",
               font="Calibri 18 bold", justify=LEFT).place(x=150, y=200)

myGui.mainloop()
