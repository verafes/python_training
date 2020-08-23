# Home work #4. if else Conditional Expressions 

print("---- Task 1. Vowel")
# Task #1. Assign your name to a variable. Determine if the name starts with a vowel.
name = input("Please enter your name: ")
vowels = "auioeAEUIO"
first = name[0]
if first in vowels:
  print(f"{first} is vowel.")
else:
  print(f"{first} is not a vowel.\n")

print("\n---- Task 2. Long/short name")
# Task #2. Using the input command, assign a user name to a variable. 
# If the name contains more than 5 letters, type "Your name is long!" Otherwise, type "Your name is short!" 
user_name = input("What is your name? ")
ln = len(user_name)
if ln > 5:
  print("Your name is long!")
else:
  print("Your name is short!")  

print("\n---- Task 3. Hours")
# 3. Using the input command, assign a user name and time in hours from 0 to 24 to variables.
# · If the time is between 0 and 6 (inclusive), type "Good night, name";
# · If the time is from 7 to 11 (inclusive), type "Good morning, name";
# · If the time is from 12 to 18 (inclusive), type "Good day, name";
# · If the time is from 19 to 24 (inclusive), type "Good night, name";
# · Otherwise type "Wrong time". 
name = input("What is your name? ")
hour = int(input("What is the current time? (Please enter hours only 0 - 24): "))
if hour < 0:
  print("Wrong time")
elif hour >= 0 and hour <= 6: # just for pracrice operators 
  print(f"Good night, {name}!")
elif 11 >= hour >= 7:
  print(f"Good morning, {name}!")
elif 18 >+ hour >= 12 :
  print(f"Good day, {name}!")
else:
  print(f"Good night, {name}") 

print("\n---- Task 4. Price")
# 4. With the input command, prompt a user for price and assign to a variable.   
# · If price >= 300, you get 30% discount; 
# · If price >= 200, you get a 20% discount;
# · If price >= 100, you get a 10% discount;
# · But If the price is less than 100, there is no discount. Find the total cost of the item. 
price = float(input("What is the price? "))
if price >= 300:
  total = round(price - price * 30 / 100, 2) 
  print(f"Y5ou get a 30% discount. Total cost is {total}.")
elif price >= 200:
  total = round(price - price * 20 / 100, 2) 
  print(f"You get a 20% discount. Total cost is {total}.")
elif price >= 100:
  total = round(price - price * 10 / 100, 2) 
  print(f"You get a 10% discount. Total cost is {total}.")
elif price >= 0:
  print(f"There is no discount. Total cost is {price}.")
else:
  print("Error. Price can't be less 0.")

print("\n---- Task 5. Age")
# 5. Prompt a user for age and assign to a variable. 
#· If age <16 type "child";
#· But if age <50 type "young man";
#· Otherwise type "senior".
age = int(input("How old are you? "))
if age < 16:
  print("child")
elif age < 50:
  print("young man")
else: 
  print("senior")

print("\n--- Task 6. Traffic light")
# 6. Assign the traffic light to the variable "current_color". Print the next traffic light comes after 'red','yellow','green'.
current_color = input("Enter any color of traffic light: ")
if current_color == "red":
  print("Next traffic light is green.")
elif current_color == "green":
  print("Next traffic light is yellow.")
elif current_color == "yellow":
  print("Next traffic light is red.")
else: 
  print("Wrong color. This is not a traffic light.")
