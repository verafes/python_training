# Lesson 6. Loops
print("\n--- Print out numbers from 0, 1, ... 10")
x = 1
while x <= 10:
  print(x) 
  x +=1

# while x > 0: # always true -> endless loop
#   print(x) # endless loop
#   x +=1

print("\n--- Print out num in order reverce 8,7 .... 1")
x = 8
while x >= 1:
  print(x)
  x -= 1

print()
#  2, 4, 6 ... 20
x =2
while x<=20:
  print(x)
  x +=2 

print()
print("\n--- 1+2+3+ .... 10")
# 1+2+3+ .... 10
s = 0
x  = 1
while x <= 10:
  s = s + x
  x += 1
print(s)

print("\n--- Factorial - n!")
# n! = 1*2*3*4*5...*n - factorial
n = int(input("Enter number: "))
factorial = 1 
x = 1
while  x <= n:
  # f = factorial * x
  factorial *= x 
  x += 1
# print(f"{n}! = {f}")  
print(f"{n}! = {factorial}")  


print("\n--- ")
# range(n) -> 0 ... n-1 / в интервале 0...n
print("--- output 0,1, ... 10")
# 0,1, ... 10
for x in range(11): # = 0-10 
  print(x)

print("\n 5 6 7 8 9 10")
# 5.6
for x in range(5,11):
  print(x)

print("\n--- ")
# 1,2, ... 10
for x in range(1, 11): # интервал от 1 - 10
  print(x)

print("\n--- Print all odd numbers from 3, 5, 7, ... 15")
#
for number in range(3, 16, 2):
  print(number)

print("\n--- Countdown 10,9,8, ... 1")
# 10,9,8, ... 1
for x in range(10,0,-1):
  print(x)

print("\n---  Output 10,7,4,1")
for x in range(10,0,-3):
  print(x)

print("\n---  Output 1 2 3 4 5 6 7 8 9 10")
# s = "1 2 3 4 5 6 7 8 9 10")
s = m = ''
x = 1
while x <= 10:
  s = s + str(x) + " "
  m = m + str(x) + "_" # extra symbol at the end
  x += 1
print(m)
print(s[:-1]) # to rid of extra space
print(s.strip())

print("\n--- Ptint out 1 sheep... 2 sheep... 30 sheep...")
sh = ''
for x in range(1,31):
  sh = sh + f"{x} sheep... " 
print(sh) 

for x in range(1,31):
  if x < 30:
    sh = sh + f"{x} sheep... "
  else:
    sh = sh + f"{x} sheep..." # no space at the end
print(sh) 

print("\nAdd all odd numbers 1+3+5+7...99")
s = 0
for x in range(1, 100, 2):
  s += x
print(s)

print("\n--- Break/continue in loop")
# breake - to break Loop
# continue - skips one iteration  
print("--- Print sum of two entered nunbers until they entred 0")
s = 0
while True:
  n = int(input("Enter number: "))
  if n == 0:
    break
  s = s + n  # = s += n
print(s)

print("\n--- Print odd numbers 1 3 5 7 9 11")
s = ''
x = 1
while x < 12:
  if x % 2 == 0: # x is  even
    x += 1
    continue
  s = s + str(x) +  " "
  x += 1
print(s)

print("\n--- Sum 1+2+3+5+6+7+8+9+10")

a= 0
x =1
while x <=10:
  if x == 4:
    x += 1 # if skip this command --> endles loop
    continue
  a += x 
  x += 1
print(a)

print("\n--- Print od numbers 1 3 5 7 9 11")
s = ''
x = 1
while x < 12:
  if x % 2 != 0: # x is odd
    s = s + str(x) +  " "
  x += 1
print(s)

print("\n--- Print stars in Pyramid shape")
# *
# **
# ***
# ***

s = ''
n = 4
x = 1 # number of *
while (x <= n):
  print("*" * x)
  x = x +1
print(s)

n = 5
for x in range(1, n+1):
  print("*" * x)
print(s)


n = 4
x = 1 
while (x <= n):
  if x < n:
    s = s + "*" * x + "\n"
  else:
    s = s + "*" * x # without a space at the end
  x = x + 1
print(s)


print("\n--- Print numbers 10 in Pyramid shape")
#10
#1010
#...
n = 10
s = ""
x = 1
while x <= n:
  s =  s  + str(n) * x + "\n"
  x += 1
print(s) 

print("\n--- Pyramid lined up numbers")
# 1
# 22
# 333
# 4444
# 55555

s = ""
n = 5 
for x in range(1, n+1): # n-1
  if x < n:
    s = s + str(x) * x + "\n"
  else:
    s = s + str(x) * x 
print(s)