max_marks: int = 65
name: str = input("Enter the name of the student: ")
mark = int(input("Enter the mark of " + name + " out of " + str(max_marks) + ": "))
p: float=(mark*100)/max_marks
print(name + " recieved " + str(round(p, 2)) + "% of the total marks.")