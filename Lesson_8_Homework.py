# Homework # 8. Function

print("--- Task #1.") 
# 1. Define the function which takes input number and returns the sign of the integer to its opposite.

num = int(input("Enter any number: "))
def opposite(num):
  return num * -1

print(opposite(num))

print("\n --- Task #2.") 
# Task 2.  Define the function 'angles_of_polygon', which tales the argument n (number of angles) and returns и the sum of the interior angles of the n-gon. The interior angle sum of a polygon is given 180 * (n − 2).

n = int(input("Enter any number of sides for a regular polygon (> 2): "))
def angles_of_polygon(n):
  #pass
  angles_sum = 180 * (n - 2)
  if n > 2:
    return angles_sum
  else:
    print("Error. Number of sides can not be less 3.")

print("Sum of Interior Angles = ", angles_of_polygon(n))

print("\n --- Task #3.") 
# Task 3. Define the function 'miles_to_feet', which takes a distance in miles as argument and returns the distance in feet. 1 mile equals 5,280 feet.

miles = int(input("Enter distance in miles: "))

def miles_to_feet(miles):
  pass
  feet = miles * 5280
  return feet

print("Distance in feet =", miles_to_feet(miles))

print("\n --- Task #4.") 
# 4. Define the function that takes two arguments - weight и height. The function calculates Body Mass Index (BMI) and returns the category based on BMI scores. The BMI formula: bmi = weight / height ** 2.
# · For bmi <= 18.5, returns "Underweight";
# · For bmi <= 25.0, returns "Normal";
# · For bmi <= 30.0, returns "Overweight";
# · For bmi > 30 , returns "Obese".

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

def mass(weight, height): 
  if weight <= 0 or height <= 0:
    return "Wrong data"
  else:
    mheight = height / 100
    bmi = weight / mheight ** 2
    print("Your bmi: ", round(bmi, 2))
    if 10 < bmi <= 18.5:
      return "Underweight"
    elif 18.5 < bmi <= 25.0:
      return "Normal"
    elif 25.0 < bmi <= 30:
      return "Overweight"
    elif 30 < bmi < 56:
      return "Obese"
  
print(mass(weight, height))

print("\n --- Task #5.") 
# 5. Define the function which takes n number of planet in order of their distance from the Sun and returns the planet name:
# ·n = 1: name = "Mercury"
# · n = 2: name = "Venus"
# · n = 3: name = "Earth"
# · n = 4: name = "Mars"
# · n = 5: name = "Jupiter"
# · n = 6: name = "Saturn"
# · n = 7: name = "Uranus"
# · n = 8: name = "Neptune"

planet_num = int(input("Enter an order number of solar planet (1-8): "))

def planet_name(planet_num): 
  if planet_num == 1:
    return "Mercury"
  elif planet_num == 2:
    return "Venus"
  elif planet_num == 3:
    return "Earth"
  elif planet_num == 4:
    return "Mars"
  elif planet_num == 5:
    return "Jupiter"
  elif planet_num == 6:
    return "Saturn"
  elif planet_num == 7:
    return "Uranus"
  elif planet_num == 8:
    return "Neptune"
  else:
    return "Wrong data"

print(planet_name(planet_num))

print("\n --- Task # 6.")
# 6. Define the function that takes three arguments a, b, c (sides of a triangle) and calculates Area if the triangle is valid or returns the message, "The triangle does not exist" owerwise. Use Heron's formula: area = (p * (p - a) * (p - b) * (p - c)) ** 0.5, где p = (a + b + c) / 2

print("Enter three sides of triangle (number only)")
a = float(input(' 1st side: '))
b = float(input(' 2nd side: '))
c = float(input(' 3rd side: '))
#The triangle is valid if the sum of two sides is greater than the largest of the three sides.

def square_of_triangle(a,b,c): 
  if a <= 0 or b <= 0 or c <= 0: 
    print("Wrong data.")   
  elif (c < a + b ) and (b < a + c ) and (a < b + c):
    print("Triangle is valid.")
    p = (a + b + c) / 2 # calculate the semi-perimeter
    area = round((p*(p-a)*(p-b)*(p-c)) ** 0.5, 2) # calculate the triangle area
    print("Semi-perimeter:", p)
    return area
  else:
    print("The triangle does not exist.") 
  
print('The area of the triangle:', square_of_triangle(a,b,c))

print("\n --- Task #7.") 
# 7. Define the function that takes input number n and returns the number of divisors of n. E.g. the divisors of 10 are: 1, 2, 5, 10. The divisors of 12 are: 1, 2, 3, 4, 6, 12.

num = int(input("Enter any integer: "))
def getDivisorsCount(num):
    count = 0
    divisor = num
    while (divisor > 0):
      if num % divisor == 0:
        count += 1
        print(f"Divisor {count} ->", divisor)
      divisor -= 1
      return count

print("Number of divisors: ", getDivisorsCount(num))
