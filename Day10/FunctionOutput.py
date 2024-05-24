# Function with output

def format(f_name,l_name):
  """Takes first and last name and format it to return the title case version of the name"""
  formatted_f_name=f_name.title() 
  formatted_l_name=l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"

output=format (f_name="ViVEk",l_name="sInGh")
print(output)


# Function with Multiple Returns is possible
def format2(f_name,l_name):
  if f_name=="" or l_name=="":
    return "Invalid input!"
  formatted_f_name=f_name.title() 
  formatted_l_name=l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"

output=format2(input("Write your first name. "), input("Write your last name. "))
print(output)