# Intro Lessons #2

print("Hello world!") 
print("My name is Vera")

# Variables and mathematical equations

a = 5 # A variable is created when it is assigned a value

print(a) # should return 5 
a = 7
print(a) # returns the new value = 7
a = a + 1
print(a) # 7 + 1 = 8
a +=1
print(a) # 8 + 1 = 9
a -=2 
print(a) # 9 - 2 = 7
a *= 3 
print(a) # 7 * 3 = 21
a /= 2 
print(a) # 21 / 2 = 10.5
a = a // 2 
print(a) # returns 5

a = 3
remainder = a % 2 #remainder of division 
print(remainder) # should return 1 

print(remainder == 0) #check if remainder is zero => should return False/True 

# False because reminder = 1 and does not equal zero

# Formatting strings
first_name = "Vera"
print(first_name)
last_name = "Fesianava"
print(first_name, last_name)
print(first_name)
print(last_name)
print(first_name + last_name) #consignation
full_name = first_name + " " + last_name 
print(full_name)
age = 10
print(full_name, age)
print(full_name + ", " +str(age))

print(f"{full_name}, {age} years old")
print(f"{first_name} {last_name}, --> {age}")

price_of_toy = 27
count = 17
total_price = price_of_toy * count
print(f"Price of {count} toys equal {total_price}")

print(f"Price of {count} toys equal {price_of_toy * count}")

# Classes
number = 10 
num = 3.2 
name = "Bob" 
is_student = True 
print(type(number)) # class 'int'
print(type(name)) # class 'str'
print(type(is_student)) # class 'bool' (boolean)
print(type(num)) # class 'float'


