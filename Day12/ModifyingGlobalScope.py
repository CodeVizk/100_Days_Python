# Modifying a Global Variable 
enemies = 1

def increase_enemies():
  # enemies +=1 [This gives error as it tries to find a local variable enemies to modify it, so to modify a global variable we simply define ]

  
  # global enemies
  # enemies+=1
  
  
  # However this can lead to bugs and error so modifying a global varibale is avoided in Python instead we can 

  
  print(f"enemies inside function: {enemies}")
  return enemies+1
  # This will not modify the original value of global variable
  

increase_enemies()
print(f"enemies outside function: {enemies}")