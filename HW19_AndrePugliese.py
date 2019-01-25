print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 18, Dec 10, 2017")

class Student:
    
    letterGradeCode = {'A':4, 'B+':3.5, 'B':3,'C+':2.5, 'C':2,'D':1,'F':0}
    
    def __init__(self, name, ucid, transcript = {}):
        self.studentName = name
        self.studentUCID = ucid
        self.studentTranscript = transcript
        
    def grade_obtained(self, courseName, letterGrade):
        self.studentTranscript[courseName] = letterGrade
        print(self.studentName + ", your grade " + letterGrade + " for " + courseName + " has been successfully recorded!")
    
    def viewGrade(self, courseName):
        if courseName not in self.studentTranscript:
            print(self.studentName + ", you did not take " + courseName + "!!")
        else:
            print(self.studentName + ", your grade for " + courseName + " is a(n) " + self.studentTranscript[courseName])
          
    def calculateGPA(self):
        GPA = 0
        for course in self.studentTranscript:
            if self.studentTranscript[course] in self.letterGradeCode:
                GPA += self.letterGradeCode[self.studentTranscript[course]]
        print(GPA / len(self.studentTranscript))
        

class Course_Section:

    university = 'NJIT'
    
    def __init__(self, number, name, enrolledStudents = []):
        self.classNumber = number
        self.courseName = name
        self.enrolledStudents = enrolledStudents

    def enroll(self, student):
        if student.studentName not in self.enrolledStudents:
            self.enrolledStudents.append(student.studentName)
            print(student.studentName + ' (ucid ' + student.studentUCID +') has​ ​successfully​ ​enrolled​ ​in​ ​section​ ​1​ ​of​ ​CS100.')
        else:
            print('already enrolled!')

    def drop(self, student):
        if student.studentName in self.enrolledStudents:
            self.enrolledStudents.remove(student.studentName)
            print(student.studentName + ' with ucid ' + student.studentUCID +'  ​been​ ​successfully​ ​dropped​ ​from​ ​section​ ​1​ ​of​ ​CS100!')
        else:
            print(student.studentName + ' with ucid ' + student.studentUCID +' does​ ​not​ ​exist​ ​in​ ​section​ ​1​ ​of​ ​CS100.')
            
s = Student('John', 'j24')
sec = Course_Section('1', 'CS100')
sec.enroll(s)
sec.enroll(s)
sec.drop(s)
sec.drop(s)