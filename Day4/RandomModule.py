import random
# for random integers
random_integer= random.randint(1,99)
print(random_integer)

# for random float

random_float=random.random()
print(random_float)
# default range is (0.0 , 1.0)
# To get desired range for float we can multiply by number 

random_float=random.random()*6
print(random_float)