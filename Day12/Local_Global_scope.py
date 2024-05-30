# Predict the output

enemies = 1

def increase_enemies():
  enemies =3
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")



# Local Scope

def potion_buff():
  potion_strength=2
  print(potion_strength)

potion_buff() 
# print(potion_strength) 
# this will give a not defined error as potion_strength is declared inside the function potion_buff so it is a local scope variable


# Global Scope
Player_health=100

def potion_buff():
  potion_strength=2
  print(Player_health)

potion_buff() 

# This will print player_health as a global scope variable can accesed by anyone 


# There is no Block Scope
game_level =3
enemies=["Skeleton","Zombies","Alien"]
if game_level< 5:
  new_enemy=enemies[0]

print(new_enemy)  
# This will work as Python have no block scope

# But as we confine it into a function it will not work

def Gaming_level():
  game_level =3
  enemies=["Skeleton","Zombies","Alien"]
  if game_level< 5:
    new_enemy=enemies[1]
    
print(new_enemy)
# Here new enemy have become a local variable of function so it cannot be accessed outside the function