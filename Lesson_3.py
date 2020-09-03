# Lesson #3. Strings. String indexing.  
# Getting part of a string. Multiplying a string by a number. Getting the index of a substring in a string.

s = "Library"
print(type(s))
n = len(s) # calculate length of the s string 
# Function len() returns the length of the a string
print(n)

# String Slicing. Getting part of a string.
# The individual characters can be accessed by index.
# String indexing in Python is zero-based: the first character in the string has index 0 , the next has index 1 , and so on.

print(s[0])
print(s[1])
print(s[len(s)-1]) # get the last symbol > y
print(s[-1]) # returns the same > y 

print(s[0:3]) # slice a part of the string, symbol #3 does not included -> 'Lib'
print(s[:5]) # returns 'Libra'
print(s[2:5]) # returns 'bra'
print(s[3:]) # from #4 to the last > 'rary'
print(s[1:-1]) # ibrar
print(s[::1]) # Library with the step 1 symbol
print(s[::-1]) # from back to the fist symbol

# Concatenating and Joining Strings
a = "my" 
b = "home"
c = a + b # merge (without space) 
d = b + a # merge 
print(c, d)
f = a + "\n" + b # dividing into 2 line
print(f)

# The * Operator. Multiplying a string by a number.
s = "hi" # new value for s
print(s*10) # multiply times

# Getting the index of a substring in a string.
monkey --> m----y
word = input("Enter a word: ")
count = len(word) - 2
print(word[0] + "-" * count + word[-1]) 

time = "12:20:05"
time = "12:00:00"
hours = int(time[:2]) # string to interger
print (hours)
minutes = int(time [3:5])
print(minutes)
seconds = int(time[6:])
print(seconds)
total_seconds = hours * 3600 * 60 + seconds
print(f"total seconds = {total_seconds}")

# functions
x = -12
print(abs(x)) # modul of digit
a = 25
b = 34
dif = abs(a-b)
print(dif)

x = 12.94372
print(round(x, 3))
print(round(x))

# maximum or minimum
a = 34
b = 9
c = 89
maximum = max(a, b, c)
minimum = min(a, b, c)
print(maximum, minimum,"\n-----")

# running competition
r1 = int(input("Enter rusult of 1 sportman: "))
r2 = int(input("Enter rusult of 2 sportman: "))
r3 = int(input("Enter rusult of 1 sportman: "))
winner_res = min(r1, r2, r3)
print(winner_res)

s = 'summer m'
i = s.index('m') # first m
print(i)
# print(s.index('a')) Error
i = s.rindex('m')
print(i, "\n-----")

i = s.find("m")
print(i)
print(s.find("a")) # -1
i1 = s.rfind("m")
print(i1, "\n-----")

s = "hellllooo word"
space = s.index(" ") # length before space
print(space)
first = s[:space]
print(first)
second = s[space+1:]
print(second)
result = second + " " + first
print(result)
