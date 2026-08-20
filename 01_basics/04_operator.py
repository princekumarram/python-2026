
##!  Arithmetic Operators

a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

print('==========================')
##! Comparison Operators
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a < b)   # True
print(a > b)   # False

print('==========================')

##!  Assignment Operators
x = 10
x += 5

print(x)

print('==========================')
##! Logical Operators
age = 23

print(age > 18 and age < 30)

is_student = True

print(not is_student)

print('==========================')

##! Membership Operators

name = "Prince"

print("P" in name)
print("z" not in name)

print('==========================')

##! Identity Operators
a = [1, 2]
b = a

print(a is b)