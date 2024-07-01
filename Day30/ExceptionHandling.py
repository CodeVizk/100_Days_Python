# File not found

try:
    file = open("text.txt")
    a_dictonary = {"key": "value"}
    print(a_dictonary["gerwe"])

except FileNotFoundError:
    file = open("text.txt", "w")
    file.write("xyz")

except KeyError as error_message:
    print(F"The Key {error_message} does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")
    raise TypeError("This is an example")