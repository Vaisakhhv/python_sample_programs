"""
#1.Write a Python program to print "Hello Python".
print("Hello python")
#2.Write a Python program to do arithmetical operations addition and division.
num1= int(input("enter a number: "))
num2= int(input("enter a number: "))
sum = num1 + num2
print(f"{num1}+{num2}={sum}")

num3= float(input("enter a number for division: "))
num4 = float(input("enter a number for division: "))
if num4 == 0:
    print("ERRO CANNOT DIVIDED BY O ")
else:
    division= num1/num2
    print(f"{num3}/{num4}={division}")"""

#python workout.py
#3.Write a Python program to find the area of a triangle.
"""
base = float(input("Enter the length of the base of the triangle: ")) 
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("the area of  the triangle is: ",area)"""
#4.Write a Python program to swap two variables.
"""
a = input("Enter the value of the first variable (a): ") 
b = input("Enter the value of the second variable (b): ") 
print(f"original values:a={a}, b ={b} ")
temp = a
a = b
b = temp
print(f"swapped values a={a}, b ={b}")"""
"""
#5.Write a Python program to generate a random number.
import random
print(f"random number: {random.randint(1,100)}")

#6.Write a Python program to convert kilometers to miles

kilometers = float(input("Enter distance in kilometers: ")) 
conversion_factor = 0.621371 
miles = kilometers * conversion_factor 
print(f"{kilometers} kilometers is equal to {miles} miles")"""

#7.Write a Python program to convert Celsius to Fahrenheit.
"""
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32 
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit")

#8.Write a Python program to display calendar
import calendar 
year = int(input("Enter year: ")) 
month = int(input("Enter month: ")) 
cal = calendar.month(year, month) 
print(cal)"""

#liner search
"""
numbers=list(map(int,input("Enter the numbers: ").split()))
search=int(input("Enter the number to search: "))
for i in range(len(numbers)):
    if search == numbers[i]:
        print("element found at index{i}")
        break
else:
    print("element not found")"""

#Fibonaci
"""
a=0
b=1
number_of_iteration=int(input("Enter the number of iteration: "))
for element in range(number_of_iteration):
    print(a)
    c=a+b
    a=b
    b=c

#prime number

num=int(input("enter a number: "))
for i in range(2,num):
    if num % i == 0:
        print("not a prime number")
        break
else:
    print("prime number")"""

#pattern

num = int(input("enter the number of elements: "))
for row in range(1,num+1):
    for column in range(1,num+1):
        print("*",end="")
    print()


num = int(input("enter the number of elements: "))
for row in range(1,num+1):
    for column in range(1,row+1):
        print("*",end="")
    print()

            