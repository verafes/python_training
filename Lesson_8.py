# Lesson 8. Function

# A function is a block of code which can be called to perform a specific task.
# The function takes inputs (arguments), do some specific computation and returns argument(s) value or produces output.

# Defining function for sum of two (itegrer) argumnets 
def add(a, b):
  return a + b

print(add(4, 8))
print(add(200, 1))

# we can pass value of arguments to a variable  
c = add(12,13)
print(c)

# Returns string 
def greet(name): 
  return f"Hello {name}"
  
print(greet("Vera"))

# How to skip 
def say_hello(name):
  pass # skips -> none, else -> error
print(say_hello("Vera"))

# reryrns alternative strings
def say_hello2(name):
  return "Hello boss" if name == "John" else "Hello guest"
print(say_hello2("Vera"))

def greeting(time):
  if 0 <= time < 6:
    return "Good night"
  elif 6 <= time < 12:
    return "Good morning"
  elif 12 <= time < 18:
    return "Good night"
  elif 18 <= time < 24:
    return "Good everning"
  else:
    return "Wrong time"
    print(time)

# Greeting depens on input time by user
time = int(input("Enter time (0-24): "))
print(greeting(time))

# Function to calculate average two numbers provided by user input 
# storing input numbers into variables

def average(a, b):
  return round(a+b/2, 2)

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(f"average for {a} and {b} is:", average(a, b)) # Calling a Function

# Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

def geom_arith_mean(a,b):
  arith = round((a +b) /2, 2)
  geom = round((a*b)**0.5, 2)
  return arith, geom # returns a tuple
  return [arith, geom] # returns a list

print(geom_arith_mean(3, 8)) # Calling a Function
print(geom_arith_mean(5, 5)) 

print("\n---- convert F to Celsius")
def temperature(tf):
  tc = round((tf - 32)*5/9, 2)
  return tc

tf = int(input("Enter t: "))
print(f"TC = {temperature(tf)}") 

print("\n---- function to calculate 1+2+3 ... +n")
# 1+2+3 ... +n
n = int(input("enter num: "))
def summation(n=0): # 0 is value by default
  #pass
  if n <0:
    return "Error"
  s = 0
  for i in range(1, n+1):
    s += i
  return s

print(summation(-5))
print(summation())
#print(summation(n))

print("\n---- function to calculate percent vowels")
def percent_vowels(s):
  vowels = "aeuio"
  s = s.lower().replace(" ", "")
  count_vowels = 0
  for letter in s:
    if letter in vowels:
      count_vowels += 1
  print(count_vowels)
  percent = count_vowels / len(s) * 100
  print(round(percent, 1), " %")

s = input("Enter string: ")
print(percent_vowels(s)) # Calling a Function
