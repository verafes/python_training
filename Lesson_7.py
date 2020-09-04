#Lesson #7. Strings and loops

print("--- Output by index")
s = "world"
for i in range(len(s)):
  print(s[i]) # with index

print("--- Output by symbols")
s = "hello, 10"
for letter in s:
  print(letter) # with symbos/element of the string 

print("== In reverse order with index ")
for i in range(len(s)-1,-1,-1):
  #print(i) # index
  print(s[i])

print("--- Calculate digits in a string")

poem = "1 potatoes, 2 potatoes, 2 potatoes, 4!"
count = 0
for el in poem:
  if el.isdigit():
    count += 1
print(count) # calculate 

print("--- Calculate digits in a string by index")
count = 0
for i in range(len(poem)):
  if poem[i].isdigit(): # i - index
    count += 1
print(count)  

print("---- Output in reverce order with whitesspaces")
s = "hello" # ---> "o l l e h"
s = s[::-1] 
print(s)

print("--- Output with whitesspaces between symbols")
t = ""
for i in range(len(s)-1, -1, -1):
  print(i) # print indexses
  t = t + s[i] + "_"
print(t.strip("_")) # remove last symbol
print(t[:-1]) # remove last symbol

print("--- Output in reverce order")
s = "hello"
for i, letter in enumerate(s):
  print(i, letter) # from 0 to end

print("--- Output in Camel Case ")
# Дана строка. Все символы строки с четными индексами сделать заглавными (uppercase), символы строки с нечетными индексами сделать строчными (lowercase).
s = "alternate"
t = ""
#s[0] = s[0].upper -> error
for i, el in enumerate(s):
  if i % 2 == 0:
    t += el.upper()
  else:
    t += el.lower()
print(t)

print("--- Is it the digit in the string ")

s = "May 18 is a holiday"
for elem in s:
  if elem.isdigit():
    print("Yes")
    break
else:
  print("No")
  
print("--- Double each symbols exept whitesspaces and digits")
st = "summer 1 or winter " 
print(st)
t = ""
for el in st:
  if el == " " or el.isdigit(): 
    t = t + el
    # continue
  else:
    t = t + el + el
    # t += t * 2
print(t)
