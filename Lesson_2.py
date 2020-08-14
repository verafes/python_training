# Lesson #2. Input function
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

https://repl.it/@verafes/Imput#main.py
