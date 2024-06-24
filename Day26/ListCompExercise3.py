# Instructions
#  Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers that are common in both files.
# e.g. if file1.txt contained:
# 1
# 2
# 3
# and file2.txt contained:
# 2
# 3
# 4
# result = [2, 3]

with open("file1.txt") as f1:
  list1 = f1.readlines()

with open("file2.txt") as f2:
  list2 = f2.readlines()

result = [int(num) for num in list1 if (num in list2)]

# Write your code above 👆
print(result)
