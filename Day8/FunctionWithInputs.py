# Simple fucntion
def greet():
  print("Hello how are you?")
  print("What do you want")
  print("The weather is good today isn't it\n")
greet()



# Function With Input

def greet_with_name(name):
  print(f"Hello how are you {name}")
  print (f"What do yo want{name}")
greet_with_name("Vivek\n")



# Function With Multiple Parameter

def greeting(name, location):
    print(f"My name is {name} and i'm from {location}")

greeting("Vivek","Nala Sopara")

# Positional argument
greeting("soho","Delhi")
greeting("Delhi","Soho")


# Keyword Argument
greeting(location="Delhi", name="Soho")