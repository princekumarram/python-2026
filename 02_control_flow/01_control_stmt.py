
##? Make decisions → if, elif, else
# age=20
 
# if age>=18:
#     print("you are an adult")



# if age >= 18:
#     print("Adult")       # inside if
# print("Program ended")   # outside if 


# age = 16

# if age >= 18:
#     print("You can vote")
# else:
#     print("You cannot vote")



marks = 75

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
    
    
print("===============================")   


##? Repeat code → for, while
# fruits = ["Apple", "Mango", "Banana"]

# for fruit in fruits:
#     print(fruit)
    
# name = "Prince"

# for char in name:
#     print(char)
    
## range() with for

for i in range(5):
    print(i)
 
 ##! range(start, stop)
for i in range(1, 6):
    print(i)   
    
##! range(start, stop, step)
for i in range(2, 11, 2):
    print(i) 
    
    
 ##! while
 
count = 1

while count <= 5:
    print(count)
    count += 1   
 
print("===============================")   
        
##? Stop or skip loop execution → break, continue
##! break
for i in range(1, 10):
    if i == 5:
        break
    print(i)
    
##! continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)   
##? Keep an empty block temporarily → pass

age = 20

if age >= 18:
    pass
else:
    print("Not an adult")