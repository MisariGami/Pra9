# 20CE029 Misari Gami
# GitHub repository link : 

# Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship.

class Student:
    def __init__(self, rollNumber, Name):
        self.rollNumber = rollNumber
        self.Name = Name
    
class Exam(Student):
    marks = {
        "Maths" : 0,
        "Science" : 0,
        "English" : 0,
        "Physics" : 0,
        "Sanskrit" : 0,
        "Gujarati" : 0
    }
    def __init__(self, rollNumber, Name, marks):
        Student.__init__(self, rollNumber, Name)
        self.marks = marks

class Result(Exam):
    def __init__(self, rollNumber, Name, marks):
        Exam.__init__(self, rollNumber, Name, marks)
        self.total_marks = sum(self.marks.values())
    def display(self):
        print("Roll no: ", self.rollNumber)
        print("Name : ", self.Name)
        print("Marks : ", self.marks)
        print("Total marks : ", self.total_marks)

n = int(input("Enter no. of students : "))
rollNumber = input("Enter roll no : ")
Name = input("Enter name : ")
marks = {
    "Maths" : int(input("Enter Maths marks : ")),
    "Science" : int(input("Enter Science marks : ")),
    "English" : int(input("Enter English marks : ")),
    "Physics" : int(input("Enter Physics marks : ")),
    "Sanskrit" : int(input("Enter Sanskrit marks : ")),
    "Gujarati" : int(input("Enter Gujarati marks : "))
}
result = Result(rollNumber, Name, marks)
result.display()