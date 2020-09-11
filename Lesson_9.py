# Lesson #9. Lists (Arrays)
# List is equivalent to arrays

arr = [6, 1, -9,  4, 3]
print(type(arr)) # -> returns class 'lists'
print(arr) # outputs the list
print(len(arr)) # returns the list's len (0...n)
print(arr[0]) # returns first item -> 6
print(arr[-1]) # returns last item -> 3
print(arr[0 : -1]) # returns the list with last item excluded
print(arr[::-1]) # -> reverses the list

print("\n----Lists. Using For loops")

arr = [6, 1, -9,  4, 3]
print(arr)

print("\n---- Using For loop")
# напечатаем items 
for i in range(len(arr)): # 0-4
  print (i, arr[i]) # returns index and item
  print (f"arr[{i}] = {arr[i]}")

print("\n--- output items")
for el in arr:
  print(el) # outputs items

print("\n--- output index and items")
for i, el in enumerate(arr):
  print(i, el) # index and item

print("\n---- Print each odd item")
# iterating through each odd item by index
s = arr[::2] 
print(s)

print("\n----Get sum and multiplication of elements using For loops")
arr = [1, 3, 5, 10]
summ = 0

for el in arr:
  summ += el
print("sum = ", summ)

p = 0 
for i in range(len(arr)):
  p *= arr[i]
print("multiplication = ", p)

print("\n---- Get sum of even elements using iterating the index ") 
# iterating through each item by index
arr = [1, 3, 5, 10, 4, 1]
s = 0
for i, el in enumerate(arr):
  if i % 2 == 0:
    s += el
print(s)

print("\n--- Function Sum")
arr = [1, 3, 5, 10, 4, 1]
print(sum(arr)) # sum function calculates sum
print(min(arr))
print(max(arr))
print(sum(arr)/len(arr)) # average 

print("\n--- Creating lists")
lst = [1, 2, 3, 4, 5] # assign

lst2 = list(range(10)) # function list
print(lst2)

lst = list(range(2,21,2)) # creating, using range
print(lst)

lst = list(range(10, 0, -3)) # returns in reverse order
print(lst)

print("\n--- String to list")
lst = list("hello") # hello -> list by element
print(lst)

print("\n---- Splitting lists")
text = "It is nice weather today"
letters = list(text) # by symbols
print(letters)
words = text.split() # by words
words = text.split(" ") 
print(words)

print("\n--- Split by a specified symbol")
time = "10:01:40"
arr = time.split(":") # by ":"
print(arr)
seconds = int(arr[0]) * 3600 + int(arr[1]) * 60 + int(arr[2]) 
print(seconds) 

print("\n--- Script - Who is winner in competition")
# Task: who won a Running Race? 
n = int(input("Enter number of runners: "))
results = []
for i in range(1, n+1):
  res = int(input(f"Enter result of {i}runners: ")) 
  results.append(res) # add new items to Arrays 
print(results)

print(f"Result of winner: {min(results)} seconds")

