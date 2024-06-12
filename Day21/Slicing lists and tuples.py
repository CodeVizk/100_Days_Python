# Slicing is the way to get multiple items from between a database

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])

# Some other ways to use slicing
# This will give us every item of the list from index 2
print(piano_keys[2:])

# This will give us items from the start till index 4
print(piano_keys[:5])

# This will give us itme from index 2 to 4 with increment of 2 i.e is ["c","e"]
print(piano_keys[2:5:2])

# This will give us every 2nd item
print(piano_keys[::2])

# This is to get every item from the end of in reverse
print(piano_keys[::-1])


# Slicing tuples
piano_tuples = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuples[3:6])
