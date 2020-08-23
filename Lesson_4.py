# Lesson #4. If - else conditional expressions. Ternary Operators

b = True
a = False
print(type(a)) # class 'bool'
print(type(b)) # class 'bool'

# This works simply because True == 1 and False == 0

# >, <, >=, <=, ==, !=, in 
print(5 > 2)
print("a" == "A")
print("a" != "b") # not equal

print("a" in "aueio") # will be True
print("s" in "aueio") # will be False

print("---- logical operators or, and, not")
# logical operators or, and, not
num = 32
print(num > 9 and num < 100 ) #  all shhold be true
day = 7
print(day == 6 or day == 7) # one of should be true
n = 8 

print("---- Even / Odd")
# A number is even if it is perfectly divisible by 2. 
print (n % 2 == 0) # even 
print (n % 2 != 0) # odd
print (not n % 2 == 0) # odd number

print("----")
print( not "b" in "aueio") # will be true
num = 13
print(num >= 10 and num <=20) # will be true
print (10 <= num <= 20) # tha same - will be true
print("---- if else")
a = 4
if a > 0:
  print("positive")

b = -4
if b > 0:
  print("positive")
elif b < 0:
  print("negative")
else:
  print("zero") 

print("----")
answer = input("Are you OK? ")
if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
  print("Cool!")
else:
  print("Get better!")

print("----")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operation (+, -,*,/): ")
if op == "+":
  result = a + b
elif op == "-":
  result = a - b
elif op == "*":
  result == a * b
elif op == "/" or op == ":":
  result = a / b
else:
  result = "Error"
print(f"{a} {op} {b} = {result}")

print("----")
s = input("Enter a letter: ")
vowels = "auioeAEUIO"
if s in vowels:
  print(f"{s} is vowel")
else:
  print(f"{s} is not vowel")

print("----")
# age < 14 drink milk
# age < 18 drink coke
# age < 21 drink beer
# age >= 21 drink whisky

age = int(input("Enter your age: "))
if age <0:
  print("Wrong age")
elif age < 14:
   print("drink milk")
elif age < 18:
  print("drink coke")
elif age < 21:
  print("drink beer")
else:
  print("drink whisky")

print("---- If a triangle is exist")
# a,b,c, --> triangle
#The sum of the length of two sides of a triangle is always greater than the length of the third side.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a < b + c and b < a + c and c < a+ b:
  print("Triangle exist")
else: 
  print("Triangle does not exist")
  
# 4.2. Ternary operator vs if else

# 1. If else
num = 12
if num % 2 == 0:
  description = "Even"
else:
  description = "Odd"
print(description)

# 2 Ternary operator
descr = "Even" if num % 2 == 0 else "Odd"
print(descr)

# name = input("Enter name: ")
# greet = "Hello boss!" if name =="John" else "Hello user!"
# print(greet)

t = 38
health = "Healthy" if t < 37 else "Ill"
print(health)


