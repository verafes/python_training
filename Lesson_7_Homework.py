# Home work #7. String and Loops

print("--- Task #1.") 
# 1. Given a string. Calculate the total number of capital letters in the string. 
statement = "There Are Case Styles: Camel, Pascal, Snake, and Kebab Case"
count = 0 
print(statement)

for i in range(len(statement)):
  if statement[i].isupper(): # i - index
    count += 1
print(count, "symbols are uppercase in the statement.") # calculate 

print("\n--- Task #2.") 
# 2. Calculate the total number of vowels in the string (upper and lower case)
s = "It is Easy to Learn and Use Python."
print(s) 
vowels = "aoieu"
v_count = 0

for el in s:
  for v in vowels:
    if el == v:
      # print(el)
      v_count += 1
    else:
      el == v.isupper()
print("In total, there are", v_count, "vowels in the string.")

print("\n--- Task #3.") 
# 3. Assign the given string to a variable. Output the string with symbols separated by a single wthitespace. e.g. "Python" -> "P y t h o n". 
st = "Separate the string by 1 single space character." 
print(st)
space = ""
for el in st:
  if el == " ":
    space = space + el   
  else:
    space = space + el + " "
print(space, "*") # checking -> if duplicated spases between words and extra spases at the end.
print(space.strip().replace("  ", " ")) # Removing extra spases

print("\n--- Task #4. ") 
# 4. In the given string, add whitespaces after non-alphaberic symbols.

s = "Bananas,2apples,sweets and 10plums"
sp = ""
x = 1
for item in s: 
  if item.isalpha() == False: 
    sp += item + "_"
  else:
    sp += item
print(sp + "*") # checking 
print(sp.replace("_", " ").replace("  ", " ")) # removing extra whitespaces 

# while sentence.isalpha() == True:
  
print("\n--- Task #5.") 
# 5. Given a string. Print out the string with vowels in upper case, e.g. "summer"--> "sUmmEr".
stri = "by alternative"
vowels = "aoieu"
new_stri = ""
for letter in stri:
  if letter in vowels:
    new_stri += letter.upper()
    #print(letter)
  else:
    new_stri += letter.lower()
print(new_stri)

print("\n--- Task #6.") 
# 6. Given a string. Get two new strings: the first one is composed from the even-indexed characters, the other - from the odd-indexed characters. E.g., s = "separate". --> "sprt", "eaae".

sentence = "I_really*like-California."
print(sentence)
even = ""
odd = ""
for i, symbol in enumerate(sentence):
    if i % 2 == 0: # Check if i(index) is even
      even += symbol
    else:
      odd += symbol
print("Even indexes:", even) # including symbols in role of spaces
print("Odd indexes:", odd) 

print("\n--- Task #7.") 
# 7. Given a string that has both upper and lower-case letters. Output the same string but in the all upper or lower-case depending on which set of letters is larger. Convert to lowercase if the sets are equal. For example, for the string "HeLLo World", it should be "hello world" because of the lowercase set in the initial string is larger. 

phrase = "HOW TO MAKE a millioN dOllars THrough writING"
#phrase = "THERE ARE CASE STYLES: Camel, Pascal, Snake, AND Kebab Case"
print(phrase)
up_count = 0
low_count = 0

for i in range(len(phrase)):
  if phrase[i].isupper(): # i - index
    up_count += 1
  elif phrase[i].islower():
    low_count += 1
  
if up_count < low_count:
  result = phrase.lower()
else:
  result = phrase.upper()

print("Number of upper-case letters:", up_count, "\nNumber of lower-case letters:", low_count)
print(f"Result statement: \n" + result)
