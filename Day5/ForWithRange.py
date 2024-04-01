# Range fucntion 
# syntax: range(start,stop,step):



# To get sum of even number 
target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
if target <=1000:
  sum=0
  for even in range (0,target+1,2):
    sum+=even
  print(sum)  