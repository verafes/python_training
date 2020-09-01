# Lesson #2. Homework

# Task #1 - Use the input command to enter a three-digit number, and then get the sum of its digit.
num = int(input("Enter a three-digit number: "))
first_dig = num // 100
print(first_dig)
second_dig = (num // 10) % 10
print(second_dig)
third_dig = num % 10
print(third_dig)
sum = first_dig + second_dig + third_dig
print("Given  number is: ", num)
print(f"The sum of its digit is: {sum} \n")

# Task #2 - Use the input command to enter the number of sides of a regular polygon and get the sum of its interior angles
n = int(input("Enter any number of sides for a regular polygon (> 2): "))
print("n =", n, "sides")
interior_angle = int((n - 2) * 180 / n) 
print("Interior angle = ", interior_angle)
angles_sum = int((n - 2) * 180)
angles_sum = (n - 2) * 180
print("Sum of Interior Angles = ", angles_sum)
print("\n")

# Task #3 - Use the input command to prompt the user for the number of miles. Convert this distance to kilometers and feet.
miles = int(input("Enter any number of miles: "))
print("Given number of miles: ", miles)
km = miles * 1.60934
print("Distance in kilometers =", round(km, 3))
feet = miles * 5280  
print("Distance in feet =", feet)
print("\n")

# Task #4 - Fahrenheit to Celsius conversion. 
# Use the input command to prompt the user for the number of degrees Fahrenheit and convert this temperature to Celsius. 
#To do this, subtract 32 from the number of degrees Fahrenheit, multiply the result by 5 and then divide by 9.
fahrenheit = int(input("Enter temperature in Fahrenheit: "))
print("Given temperature:", fahrenheit, "F")
celsius = (fahrenheit - 32) * 5 / 9
print("Temperature in Celsius:", round (celsius, 1))
print("\n")

# Task #5 - Celsius to Fahrenheit conversion 
celsius = int(input("Enter temperature in Celsius: "))
print("Given temperature:", celsius, "C")
fahrenheit = celsius * 9 / 5 + 32
print("Temperature in Fahrenheit:", round (fahrenheit, 1))
print("\n")

# Task #6 - Use the input command to prompt the user for the order cost (price), tip percent, and sales tax percent. 
#Calculate the total order costs (total_price). 
price = int(input("Enter the cost of a purchase order: "))
tip_percent = int(input("Enter tip percent: "))
tax_percent = float(input("Enter tax percent: "))
tip_amount = price * tip_percent / 100
tax_amount = price * tax_percent / 100
print(f"{tip_percent} % Tip: {tip_amount}")
print(f"{tax_percent} % Sales Tax: {tax_amount}")
total_price = round((price + tip_amount + tax_amount), 2)
print("Oder total:", total_price) 
print("\n")

# Task #7 - With the input command, prompt to enter the price of a discounted item and the percentage of the discount. 
#Calculate the original price of the discounted item (full price of the product), round the result to 2 decimals. 
#For example, a discounted item costs $ 40 with a 50% discount. Then the price of the product without discount is $ 80. If an item is priced at $ 40 with a 10 percent discount, its full price is $ 44.44. 
# Formula - original price = sales price / (1 - discount percentage / 100)
item_dis_price = float(input("Enter the sales price (price with discount): "))
discount_percentage = float(input("Enter discount percent: "))
original_price = item_dis_price / (1 - discount_percentage / 100)
round_orig_price = round(original_price, 2)
print(f"The original price of the {discount_percentage} % discounted item =", round_orig_price)

https://repl.it/@verafes/Home-work-2
