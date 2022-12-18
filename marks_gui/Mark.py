class Mark:
    global _student_name
    global _student_mark
    
    def __init__(self, student_name = '', student_mark = '', grade = ''):
        self._studentName = student_name
        self._studentMark = student_mark

    def Mark(self, student_name, student_mark):
        self._studentName = student_name
        self._studentMark = student_mark

    def set_student_name(self, student_name):
        self._studentName = student_name
    def get_student_name(self):
        return self._studentName

    def set_student_mark(self, student_mark):
        self._studentMark = student_mark
    def get_student_mark(self):
        return self._studentMark
    
    def get_grade(self, student_mark):
        if(int(student_mark) < 50):
            return 'F'
        elif(int(student_mark) < 65):
            return 'P'
        elif(int(student_mark) < 75):
            return 'C'
        elif(int(student_mark) < 85):
            return 'D'
        else:
            return 'HD'
