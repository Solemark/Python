from tkinter import Tk, StringVar, Label, Entry, Button
import Mark

class MarksGUI:
    global name
    global mark
    global output
    global students
    students = []

    def submit():
        m = Mark.Mark()
        m.Mark(name.get(), mark.get())
        students.append(m)
        output.set('Added student: ' + ' ' + m.get_student_name() + ' ' + m.get_student_mark() + ' ' + m.get_grade(m.get_student_mark()))
        name.set('')
        mark.set('')

    def display():
        text = ''
        for x in students:
            text += (x.get_student_name() + ' ' + x.get_student_mark() + ' ' + x.get_grade(x.get_student_mark()) + '\n')
        print(text)
        output.set(text)

    def search():
        print('search')

    root = Tk()
    root.title('Mark Entry System 3.0')
    name = StringVar()
    mark = StringVar()
    output = StringVar()

    Label(root, text='Enter the students details').grid(row=0, columnspan=2)
    Label(root, text='Name:').grid(row=1, column=0)
    nameBox = Entry(root, textvariable=name).grid(row=1, column=1)
    Label(root, text='Mark:').grid(row=2, column=0)
    markBox = Entry(root, textvariable=mark).grid(row=2, column=1)
    button = Button(root, text='submit', command=submit).grid(row=3, column=0)
    button = Button(root, text='display', command=display).grid(row=3, column=1)
    button = Button(root, text='search', command=search).grid(row=4, column=0)
    button = Button(root, text='exit', command=exit).grid(row=4, column=1)
    Label(root, textvariable=output).grid(row=5, columnspan=2)

    root.mainloop()