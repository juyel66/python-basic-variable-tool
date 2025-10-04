from math import *

# a = 2
# b=3
# c = a+b
# print("The sum of a  and b is:",c)

# print(15+5)
# print(15-5)
# print(15*5)
# print(15/5)
# print(14854%5)



# num1= int (input("Enter your first number:"))
# num2 = int (input("Enter your second number:"))
# sum =  num1 + num2
# sub =  num1 - num2
# mul =  num1 * num2
# dev =  num1 / num2
# mod =  num1 % num2
# print("The sum of two numbers is:", sum)
# print("The sum of two numbers is:", sub)
# print("The sum of two numbers is:", mul)
# print("The sum of two numbers is:", dev)
# print("The sum of two numbers is:", mod)


# # triangle area
# base = int (input("Enter the base of triangle:"))
# height = int (input("Enter the height of triangle:"))

# area = 1/2 * base * height
# print("The area of triangle is:", area)


# circle area 

# r = int (input("Enter the radius of circle:"))
# pi = 3.1416
# area = pi * r * r
# print("The area of circle is:", area)



# print(max(5,10))
# print(min(5,10))
# print(abs(-5))
# print(pow(5,10))
# print(sqrt(5))
# print(floor(5.7))
# print(ceil(5.7))
# print(sin(0.5))
# print(gamma(0.5))
# print(erf(0.5))

# # string manipulation 
# print("hello", end=" ")
# print("world")



# calculate grade 

mark = int(input("Enter your mark:"))

if 100 >=  mark >= 80:
    print("Your Result is A+")
elif 80 > mark >=70:
    print("Your Result is A")
elif 70 > mark >=60:
    print("Your Result is A-")
elif 60 > mark >=50:
    print("Your Result is B")
elif 50 > mark >=40:
    print("Your Result is C")
elif 40 > mark >=33:
    print("Your Result is D")
elif  mark >=100:
    print("Invalid Mark")
else:
    print("You are fail")


# calculate grade in advance 

# Input marks for 5 subjects
mark1 = int(input("Enter mark for subject 1: "))
mark2 = int(input("Enter mark for subject 2: "))
mark3 = int(input("Enter mark for subject 3: "))
mark4 = int(input("Enter mark for subject 4: "))
mark5 = int(input("Enter mark for subject 5: "))

# Check pass/fail for each subject
if mark1 >= 33:
    result1 = "Pass"
else:
    result1 = "Fail"

if mark2 >= 33:
    result2 = "Pass"
else:
    result2 = "Fail"

if mark3 >= 33:
    result3 = "Pass"
else:
    result3 = "Fail"

if mark4 >= 33:
    result4 = "Pass"
else:
    result4 = "Fail"

if mark5 >= 33:
    result5 = "Pass"
else:
    result5 = "Fail"

# Print subject results
print("\nSubject Results:", result1, result2, result3, result4, result5)

# Calculate total and average
total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5
print("Total:", total)
print("Average:", average)

# Determine overall result
if result1 == "Fail" or result2 == "Fail" or result3 == "Fail" or result4 == "Fail" or result5 == "Fail":
    overall_result = "Fail"
    grade = "N/A"
else:
    overall_result = "Pass"
    if 80 <= average <= 100:
        grade = "A+"
    elif 70 <= average < 80:
        grade = "A"
    elif 60 <= average < 70:
        grade = "A-"
    elif 50 <= average < 60:
        grade = "B"
    elif 40 <= average < 50:
        grade = "C"
    elif 33 <= average < 40:
        grade = "D"

print("Overall Result:", overall_result)
print("Grade:", grade)
