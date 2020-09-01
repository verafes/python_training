# Homework #6. Loops 

print("--- Task #1. 10 monkeys") 
# Task #1. Write a program that output the following string: "1 monkey 2 monkeys ... 10 monkeys".

for x in range(1, 11):
  if x == 1:
    monkey = f"{x} monkey "
  else:
    monkey = monkey + f"{x} monkeys "
print(monkey.strip()) 

print("\n--- Task #2. Countdown timer")
# Task #2. Write a program that output the string that tracks the number of seconds that remain for the roket launching: "10 seconds...9 seconds...8 seconds...7 seconds...6 seconds...5 seconds...4 seconds...3 seconds...2 seconds...1 second"
for x in range(10, 0, -1):
  print(str(x) + " seconds...")
print()

print("\n--- Task #3")
# Task #3. Input two numbers k and n. Calculate you own power (k**n) without using power (**) operator but by using repeated  multiplication (number is being multiplied by itself). 
# Example: 3**4 = 81 is equivalent to 3*3*3*3 = 81.  

n = int(input("Please enter any number: "))
k = int(input("Please enter any number for a power: "))
x = 1
s = n
for x in range(1, k):
  n = s * n
  x += 1
print("k ** n =", n)
m = (str(s) + " * ") * (k-1) 
print(f"{m}{s} = {n}") 

print("\n--- Task #4")
# Task #4. The first day of training, the athlete ran 5 km. Each next day, he ran 5% more than the day before. How many kilometers will the athlete run on the 10th day?
day = 1
distance = 5
print("The first day distance = ", distance, "km")
distance2 = distance * (1.05**9) # for checking
print(f"The 10th day distance should be {distance} * (1.05 ** 9) =", round(distance2,2), "km")

print()
while day < 10:
  distance +=  distance * 5/100
  print(distance)
  day += 1
print("On the 10th day, the athlete run ", round(distance,2), "km")

print("\n--- Task #5. ")
# Task #5. The student did not know a single English word at the beginning of the training. On the first day of class, he learned 5 English words. On each next day, he learned 2 more words than the day before. In how many days will the student know at least n English words?
n = int(input("Please enter number of words: "))
day = 0 # d2
words = 5
print(f"The student knew {day} words before training session.")
print(f"The student learned {words} on the first day.")
total = 5
while words <= n:
  words = words + 2 
  day = day + 1
  # total = total + words #?
print(f"The student will learn {n} words at the the {day} day, but he may learn {words} words by the end of the {day} day of the traning.")
print("Verify with addition: 5" + " + 2" * day + " = " + str(words) + " words")
print(total) #?

print("\n--- Task #6. ")
# Task #6. Prompt to a user to input the nunber of steps. Get the string that contains stairs made of sharp sign (#). 
# #
#  #
#   #
#    #
#     #
num = int(input("How many steps in the stairs: "))
stairs = ''
x = 1

while x <= num:
  print(" " * x + "#")
  x += 1
print(stairs)

print("--- Task #7. ")
# 7. Output stars having the form of a pyramid. With the command input, get the number of levels. Use function for center align the string.  
#    *
#   ***
#  *****
# *******
levels = int(input("Please enter any number of levels for pyramid: "))
star = '*'
x = 1 
# ver 1
c_point = levels * 2 # -> extra space before pyramid if levels*2+1 
for x in range(levels):  
  star = "*" + x * 2 * "*"
  x += 1
  print(star.center(c_point))

# ver 2 - in class
# levels = int(input("Please enter any number of levels for pyramid: "))
 
c_point = levels * 2 - 1 
for x in range(1,levels + 1):
  stars = x * 2 - 1
  print(("*" * stars).center(c_point))
  
