# Lesson 5. String function and methods
# All string methods returns new values. They do not change the original string.

print("--- Searchig position of a specified symbol")
# index() - Searches the string for a specified value and returns the position of where it was found
s = "programming language"
print(s[1:-1]) 
# # - print(ln(s))
index = s.index("g")
print(index)
last_index = s.rindex("g")
print(last_index)

print("\n--- Searchig a specified symbol")
# find() - Searches the string for a specified value and returns the position of where it was found
i = s.find("P") # -1
print(i)
last_i = s.rfind("a")
print(last_i)

print("\n--- Alphabetic symbol or digit")
# isalpha() - Returns True if all characters in the string are in the alphabet
s = "sky" # alfabetic 
print(s.isalpha()) # return True if all symbols are alfabetic 
s = "7up"
print(s.isalpha()) #False
s = "s!"
print(s.isalpha()) #False

# isdigit() - Returns True if all characters in the string are digits
s = "2020" 
print(s.isdigit()) # True
s = "20 20 " 
print(s.isdigit()) # False for space
s = "20.20" 
print(s.isdigit(), 1) # false for dot

print("---")
# isalnum() - Returns True if all characters in the string are alphanumeric
s = "August19"
print(s.isalnum()) # True
s = "August 19"
print(s.isalnum()) # False because of space

print("\n--- lower/upper case, titles")
# islower() - Returns True if all characters in the string are lower case	
s = "Aasd"
print (s.islower()) # False
print ("o".islower()) # True
print (s.isupper())# False
print ("HELLO".isupper()) # ttrue

# istitle()	Returns True if the string follows the rules of a title
print(s.istitle()) # true

print("Sky is blue".istitle()) # False
print("Sky Is Blue".istitle()) # True

print("\n--- .count() - number of times a specified value")
# count() - Returns the number of times a specified value occurs in a string
s = "programming language"
g = s.count("g") 
print(g) # "g" is 4 times in the string
q = s.count("ng")
print(q)

print("\n--- justified string")
# ljust() / rjust() - Return a left/right justified version of the string 
s = "Hello"
print(s.rjust(20)) # justified to 20 position
print(s.ljust(20), "a")
print(s.center(20)) # Returns a centered string

word = "summer"
print("*" * 20)
print("*" + word.center(18) + "*")
print("*" * 20)

print("\n--- Change case")
# capitalize() - Converts the first character to upper case
s = "my flOwErs aRe beaUtiful"
print(s.capitalize()) # Converts the first character to upper case
print(s.title()) # Converts the first character of each word to upper case
print(s.lower()) # Converts a string into lower case
print(s.upper()) # Converts a string into upper case
print(s.swapcase()) # Swaps cases, lower case becomes upper case and vice versa

print("\n--- what is start/end symbol")
# endswith() - Returns true if the string ends with the specified value
s = "my flOwErs aRe beaUtiful"
end = "beaUtiful"
print(s.endswith("ful")) # True
print(s.endswith(end)) # True

# startswith() - Returns true if the string starts with the specified value
start = "my"
print(s.startswith(start)) # True

print("\n--- in - search specified symbol(s)")
s = "my flOwErs are beaUtiful"
print("a" in s) # True
print("are" in s) # True

print("\n--- strip() - Returns a trimmed version of the string")
#rstrip()	Returns a right trim version of the string
#lstrip()	Returns a left trim version of the string
s = " My flowers are beautiful  "
print(s.strip()) # strip() function will remove leading and trailing whitespaces

# strip() - remove specified symbols
s = "**My flowers are beautiful**"
print(s.strip("*")) # removes all "*"
print(s.rstrip("*")) # removes * at the right

s = "  My flowers are beautiful  "
print(s.lstrip()) # will remove leading spaces (at the left)
print(s.rstrip()) # will remove trailing spaces (at the rhight)

print("\n--- replace() - replace specified symbols")
# replace()	Returns a string where a specified value is replaced with a specified value
s = " My flowers are beautiful  "
s1 = s.replace(" ", "*")
print(s1)
print(s)
s2 = s.replace("flowers", "friends")
print(s2)