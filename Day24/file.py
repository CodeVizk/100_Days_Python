# Access files, read, write files using with keyword on python
# file = open("my_file.txt")
# content = file.read()
# print(content)
#
# # We close the file after use to reduce resource usage
# file.close()


# But for ease we use the with method
# here is also an example of using relative path
with open("../../my_file.txt") as file:
    content = file.read()
    print(content)
# as soon as we are done with the code it automatically closes the file

# To write in a file using python first we need to set the mode of file there are three types of mode
# r = read only (Default mode)
# w = write
# a = append to add to the existing text

# with open("my_file.txt", mode="a") as file:
#     file.write("\nI'm 19 years old.")
#
#
# # we can create a new file through here but only in w mode
# with open("new_file.txt", mode="w") as ff:
#     ff.write("New text created.")

