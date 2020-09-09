# Home work #5. Ternary Operators. String function 

print("---- Task 1. Work day/Weekend")
# Task #1. Input a day of the week number (1-7) to the variable num_of_day. 
# Using ternary operators, assign the value “Weekend” to the variable day if week number is 6 or 7, otherwise “Work day”. 
num_of_day = int(input("Please enter week number (1-7): "))
day = "Weekend" if num_of_day == 6 or num_of_day == 7 else "Work day" 
print(day)

print("\n---- Task 2. Lucky number")
# Task #2. Input a number to variable n. 
# Using ternary operators, assign the value "Lucky number" to the variable is_lucky 
# if the number is divisible by 9, otherwise "Not a lucky number". 
# Print the result saying whether this number is lucky or not.
n = int(float(input("Please enter any number: ")))  
n1 = (n % 9)
print (n1)
is_lucky = "Lucky number" if n1 == 0 else "Not a lucky number"
print(is_lucky)

print("\n---- Task 3. Favorite color")
# 3. Create a variable "phrase" and assign the value "My eyes are green too!" to it. 
# Using input command, ask the user, “What is your favorite color?” 
# Replace the word “green” in phrase with the user's favorite color and print the result.
phrase = "My eyes are green too!"
color = input("What is your favorite color? ")
print(phrase.replace("green", color))

print ("Version #1")
first_name = input("Please enter your first name: ") 
middle_name = input("Please enter your middle name: ")
last_name = input("Please enter your last name: ")
maximum = max(len(first_name), len(middle_name), len(last_name))
print(maximum)
print(first_name.title().rjust(maximum))
print(middle_name.title().rjust(maximum))
print(last_name.title().rjust(maximum))

print ("\nVersion #2")
# name = input("Please enter your first, middle and last name (with spaces). 
# (If no middle name, put NO. Three words required): ")
first, middle, last = name.title().split(" ")
print(first, middle, last)
m = max(len(first), len(middle), len(last))
print(m)
print(first.rjust(m))
print(middle.rjust(m))
print(last.rjust(m))

print("\n---- Task 5. Remove all vowels")
# 5. Create the variable s and assign any string value to it. Remove all vowels from the text. 
# For example, s = “We like Python” --> “W lk Pythn”.
s = "It is Easy to Learn and Use Python."
print(s)
vless = s.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","").replace("y","")
print(vless)
uvless = vless.replace("A","").replace("E","").replace("I","").replace("O","").replace("U","").replace("Y","")
print(uvless)

print("\n---- Task 6. Replase a word")
# 6. Using the input command, enter a string. Then enter the word to be replaced. 
# Then enter the replacement word. Output the result. 
# For example, a user entered the statement "Have a good day", the word "good", the word "nice". 
# The result should be: "Have a nice day"

phrase = input("Please enter a phrase of 2 or more words: ")
word_repl = input("What word would you like to be replace in the phrase: ")
word_add = input("Now please enter a word to replace with: ")
#print(f"I hope you have a" good {time_of_day}") 
if word_repl.find(" "): # if a user entered the word with space(s)
  word_repl = word_repl.replace(" ","") # remove space(s)
  new_phrase = phrase.replace(word_repl, word_add)
  print(new_phrase)
else: 
  new_phrase = phrase.replace(word_repl, word_add)
  print(new_phrase)

print("\n---- Task 7. Remove/Add specified symbols")
# 7. Given a String. There are some spaces at the beginning and end of the statement. 
# Get a string where each word is capitalized, spaces at the beginning of the statement are removed, 
# and spaces at the end of the statement are replaced with the same number of exclamation marks. 
# For example, s = "    I like summer   ". Get "s = "I Like Summer!!!"
s = "     I like to learn Python   "
print("*" + s + "*") # * just to see borders
st = s.title().strip(" ")
cnt = len(s) - len(s.rstrip())

print("\"" + st + "!" * cnt + "\"")
