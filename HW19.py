class Course_Section:
    
    def __init__(self, number, courseName, enrolled_students = []):
        self.num = number
        self.course_name = courseName
        self.enrolled_students = enrolled_students
        
    def enroll(self, student):
        for enrolled in self.enrolled_students:
            if student[1] == enrolled[1]:
                print("already enrolled!")
            if student[1] != enrolled[1]:
                self.enrolled_students.append(student)
                print(student[0] + " (ucid " + student[1] + ") has successfully been enrolled in section " + str(self.num) + " of " + self.course_name + ".")
            
s1 = Course_Section(1, 'CS100')
s1.enrolled_students
s1.enroll(('John', 'j24'))
s1.enroll(('John', 'j24'))