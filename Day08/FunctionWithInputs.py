# Simple function
def greet():
  print("Hello how are you?")
  print("What do you want")
  print("The weather is good today isn't it\n")
greet()



# Function With Input
def greet_with_name(name):
  print(f"Hello how are you {name}")
  print (f"What do you want{name}")
greet_with_name("Vivek\n")



# Function With Multiple Parameters

def greeting(name, location):
    print(f"My name is {name} and i'm from {location}")

greeting("Ptown", "Nala Sopara")

# Positional argument
greeting("Soho", "Delhi")
greeting("Delhi", "Soho")


# Keyword Argument
greeting(location="Delhi", name="Soho")
