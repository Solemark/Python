from tkinter import Tk, StringVar, Label, Entry, Button

Student = {
    'student_name': str,
    'student_mark': int
}

def marks_gui() -> None:
    name: str
    mark: str
    output: str
    students = []
    
    def get_grade(student_mark: int) -> str:
        if student_mark < 50:
            return 'F'
        elif student_mark < 65:
            return 'P'
        elif student_mark < 75:
            return 'C'
        elif student_mark < 85:
            return 'D'
        else:
            return 'HD'

    def submit() -> None:
        student: Student
        print(int(mark.get()))
        student = {'student_name': name.get(), 'student_mark': int(mark.get())}
        students.append(student)
        output.set('Added student: ' + ' ' + student['student_name'] + ' ' + get_grade(student['student_mark']))
        name.set('')
        mark.set('')

    def display() -> None:
        text = ''
        for student in students:
            text += (student['student_name'] + ' ' + get_grade(student['student_mark']) + '\n')
        output.set(text)

    def search() -> None:
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

marks_gui()