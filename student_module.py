class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.subjects = []

    def add_mark(self, mark):
        self.subjects.append(mark)

    def get_all_marks(self):
        return self.subjects

    def Calc_average(self):
        return sum(self.subjects) / len(self.subjects)

student = Student("Soha yousef", 46, "Egypt")



student.add_mark(100) #add a mark to the student's list of marks

#to get all of the marks for a student
marks = student.get_all_marks()
print(marks)

#the average of a student's marks
average = student.Calc_average()
print(average)