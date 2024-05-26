# Making a Calculator using Loops, Dictionary, Recursion, Function.
from ArtForCalculator import logo
print(logo)

def calculator():
  def add(n1,n2):
    return n1+n2

  def subtract(n1,n2):
    return n1-n2

  def multiply(n1,n2):
    return n1*n2

  def divide(n1,n2):
    return n1/n2
  operations = {
    "+":add ,
    "-":subtract ,
    "*":multiply ,
    "/":divide
  }
  num1=int(input("What's the first number? "))
  should_continue=True
  while should_continue:
    
    num2=int(input("What's the second number? "))
    for key in operations:
      print(key)
    User_Operation=str(input("Select operation "))
    
    calculation_function=operations[User_Operation]
    answer=calculation_function(n1=num1,n2=num2)
    
    print(f"{num1} {User_Operation} {num2} = {answer}")
    user_continue=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation- ")
    if user_continue=="y":
      num1=answer
      
    else:
      should_continue=False
      calculator()

calculator()