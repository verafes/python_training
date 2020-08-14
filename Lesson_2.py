# Lesson #2. 
# 2.1. Data Types 

# Text Type: str
# Numeric Types: int, float, complex
# Boolean Type: bool

print("--- Reviewing. Getting integer and Reminder")
num = 19
print("Number is", num)
first = num // 10 # an integer number without decimals
print("integer", num, "//", 10, "=", first, )
second = num % 10 # reminder
print("Reminder", num, "% 10 =", second)

print("--- Clases of strings")
n1 = 10
n2 = 5.27
print(type(n1)) # int
print(type(n2)) # float

name = "Alise"
print(type(name)) # str
n = "12"
print(type(n)) # str

is_adult = True
print(type(is_adult)) # bool
is_adult2 = 18 > 10
print(type(is_adult2)) # bool

print("--- Float to Integer and back")
n = 2.8
n = int(n) #  an integer number without decimals
print(n)

n2 = 3
m = float(n2) # floating point number
print(m) 

print("--- Integer to String")
n3 = 12
s = str(n3)
print(n3)
print(s)
print(type(s))

print("--- Boolean to Integer")
q = False
q2 = int(q)
print(q2)

b = 15
b2 = bool(b)
print (b2)

print("--- String to Boolean")
s1 = "hi"
s2 = ""
ss1 = bool(s1)
ss2 = bool(s2)
print (ss1)
print (ss2)

https://repl.it/@verafes/Types-of-data

# 2.1. Input function
# input accept user input typed from the keyboard and convert it into a string abd retuts it to a variable 

name = input("What is your name? ")
print(f"Hello {name}!") 
age = input(f"{name}, how old are you? ") 
print(f"{name}, {age} is the best age!")
print(age, "is the best age!")

# class strings for both text and numbers 
print(type(name)) #class str
print(type(age)) #class str

print("--- Input two numbers to get sum of its digits")  
a =  int(input("Enter first number: "))
b =  int(input("Enter second number: "))
# s = int(a) + int(b) 
s = a + b
print(s)
 
print("--- Getting sum of floating-point numbers") #
a =  float(input("Enter first number: "))
b =  int(input("Enter second number: "))
# int() converts a string to integer
s2 = a + b
print(s2)

print("--- Converting an input distance in meters into kilometers")
# int convert string to integer
dist = int(input("Enter distance in meters: "))
km = dist / 1000
print("Distance in km = ", km)
print(f"Distance in km = {km}")
print(f"Distance in km = " + str(km))

https://repl.it/@verafes/Imput
 
