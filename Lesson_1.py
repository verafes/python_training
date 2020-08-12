# Lesson #1. Variables

# String Variables 

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

# Numeric Variables and Clases 

print(5)
print(3 + 8)
a = 10
print(a)
print(type(a)) # returns class 
b = 5.2
print(b)
print(type(b)) # returns class 

name = "Alice"
print(name)
print(type(name)) # returns class 

# Mathematical equations

a = 11
b = 3
add = a + b
dif = a - b
mult = a * b
div = a / b
int_div = a // b
reminder = a % b
power = a ** b
print(add)
print(a, "+", b, "+", add)

# String formatting

print(f"{a} + {b} = {add}")
print(f"{a} - {b} = {dif}")
print(f"{a} * {b} = {mult}")
print(f"{a} / {b} = {div}")
print(f"{a} // {b} = {int_div}")
print(f"{a} % {b} = {reminder}")
print(f"{a} ** {b} = {power}")

div = round(a / b, 2)
print(f"{a} / {b} = {div}")

price_of_toy = 27
count = 17
total_price = price_of_toy * count
print(f"Price of {count} toys equal {total_price}")
print(f"Price of {count} toys equal {price_of_toy * count}")

https://repl.it/@verafes/Variables

