# To Input a list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
Total_height=0
Total_students=0

for x in student_heights:
  Total_height+=x
  Total_students+=1

avg_height=Total_height/Total_students

print(f'''total height = {Total_height}
number of students = {Total_students}
average height = {round(avg_height)}  ''')