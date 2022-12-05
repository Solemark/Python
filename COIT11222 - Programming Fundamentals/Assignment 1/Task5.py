import tkinter
from tkinter import messagebox, StringVar

totalGrade: int = 0
sNumber: int = 0

def getGrade():
    global sNumber
    global totalGrade
    if int(grade.get()) <= 49:
        messagebox.showinfo("Student Grade", "Student has failed (F)")
    elif int(grade.get()) <= 64:
        messagebox.showinfo("Student Grade", "Student has passed (P)")
    elif int(grade.get()) <= 74:
        messagebox.showinfo("Student Grade", "Student has recieved a Credit (C)")
    elif int(grade.get()) <= 84:
        messagebox.showinfo("Student Grade", "Student has recieved a Distinction (D)")
    else:
        messagebox.showinfo("Student Grade", "Student has recieved a High Distinction (HD)")
    sNumber += 1
    totalGrade += int(grade.get())
    avgText.set("The average grade for students is: " + str(round(totalGrade/sNumber, 2)))

window = tkinter.Tk()
window.title("Mark Entry System 2.0")
tkinter.Label(window, text = "Welcome to the mark entry system 2.0!").pack()
tkinter.Label(window, text = "Please enter the student's grade between 0-100").pack()
grade = tkinter.Entry(window)
grade.pack()
avgText = StringVar()
avgText.set("The average grade for students is: 0")
tkinter.Label(window, textvariable = avgText).pack()
tkinter.Button(window, text = "Enter", command = getGrade).pack()
window.mainloop()