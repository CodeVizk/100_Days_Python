# Recommended to write the code in console
import random
student_names = ["Alex", "Beth", "Monica", "Rahul", "Avon"]
print(student_names)

# using students names creating a dictionary with each student gets a random marks
student_dictionary = {student: random.randint(10, 100) for student in student_names}
print(student_dictionary)

# Creating a dictionary containing students who have scored more than 60
passed_student = {student: score for (student, score) in student_dictionary.items() if score >= 60}
print(passed_student)