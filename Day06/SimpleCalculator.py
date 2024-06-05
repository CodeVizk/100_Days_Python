# The Calculator

def add(num1,num2):
  return num1+num2

def subtract(num1,num2):
  return num1-num2

def multiply(num1,num2):
  return num1*num2

def divide(num1,num2):
  return num1/num2


def calculator():
  s_continue="n"
  first_num=0
  should_continue=False
  while not should_continue:
    if s_continue=="n":
      first_num=float(input("What's the first number? "))
    operation=input("+ \n- \n* \n/ \nSelect operation- ") 
    second_num=float(input("What's the next number? "))
    result=0
  
  
    if operation=="+":
      result=add(num1=first_num,num2=second_num)
    elif operation=="-":
      result=subtract(num1=first_num,num2=second_num)
    elif operation=="*":
      result=multiply(num1=first_num,num2=second_num)
    elif operation=="/":
      result=divide(num1=first_num,num2=second_num)
    print(f"{first_num} {operation} {second_num}= {result}")
    s_continue=input(f"Type 'y' to continue calculating with {result},"
    "or type 'n' to start a new calculation:")
    if s_continue=="y":
      first_num=result


calculator()