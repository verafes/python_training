# Homework #3. Strings. 

# Task #1. Using the input command, assign your name to a variable, and then use that string to print its length, the first and the last characters.  
print("--- Task #1. Length of a name")
name = (input("What is your name? "))
ln = len(name) # calculate length of the name string
first = name[0]
#last = name[ln-1]
last = name[-1]
print(f"{name}, your name has {ln} letters")
print(f"{name}, your name starts with the letter \"{first}\".")
print(f"{name}, your name ends with the letter \"{last}\". \n")

# Task 2. Using the input command, assign your name to a variable. Print hello greeting with the name in reverse order. For example, "Alice" --> "Hello, ecilA!"
print("\n--- Task #2. Revese name")
name2 = (input("What is your name? "))
print(f"Hello, {name2[::-1]}!" )

# Task #3. We are given a string with 10 digits, e.g. s = "1234567890". Using concatenation and joining strings, print a string in the phone number format: "(+123) 456-7890."
# print("Print the string 1234567890 in the phone number format.")
print("\n--- Task # 3. Phone number")
s = "1234567890"
one = s[:3]
print(one)
two = s[3:6]
print(two)
three = s[6:] 
print(three)
print(f"Phone number: (+{one}) {two} - {three} \n") 

# 4. Using the input command, assign to a variable your first and last name separated by a space. Convert the string to email format. E.g. "Alice Moon" --> "Alice.Moon@company.com".
print("\n--- Task # 4. Email")
full_name = (input("Please enter your first and last name: "))
company = (input("and your company nickname (one word): "))
space = full_name.index(" ")
print(space)
first_name = full_name[:space]
print(first_name)
last_name = full_name[space+1:]
print(last_name)
print(company)
email = (first_name + last_name + "@" + company + ".com")
print("Your email:", email, "\n")

# Task 5. Enter a word. Wrap the word in star pattern frame.  
print("\n--- Task # 5. Word in a star frame")
word = (input("Enter any word(s): "))
ln_word = len(word)
star = "*" * (ln_word + 4)
print(star)
print("*", word, "*" )
print(star)

