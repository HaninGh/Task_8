import subject_module
import student_module

# Create 3 objects of Subject class
subject1 = subject_module.Subject("Math", 90)
subject2 = subject_module.Subject("Science", 80)
subject3 = subject_module.Subject("English", 70)

# Create 3 objects of Student class
student1 = student_module.Student("Soha yousef", 46, "Egypt")
student2 = student_module.Student("Hamza ", 19, "Palestine")
student3 = student_module.Student("Emy", 20, "Moracoo")

# Add marks to students
student1.add_mark(subject1.mark)
student1.add_mark(subject2.mark)
student1.add_mark(subject3.mark)

student2.add_mark(subject1.mark)
student2.add_mark(subject2.mark)
student2.add_mark(subject3.mark)

student3.add_mark(subject1.mark)
student3.add_mark(subject2.mark)
student3.add_mark(subject3.mark)

# Print the marks of all students
print("Marks of Soha yousef:", student1.get_all_marks())
print("Marks of Hamza:", student2.get_all_marks())
print("Marks of Emy:", student3.get_all_marks())

# Print the average marks of all students
print("Average marks of Soha yousef:", student1.Calc_average())
print("Average marks of Hamza:", student2.Calc_average())
print("Average marks of Emy:", student3.Calc_average())