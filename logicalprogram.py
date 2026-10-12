"""
numberlist=[]
number_of_elements=int(input("enter the number of elements"))
for element in range(number_of_elements):
    num=int(input(f"Enter the element {element+1}: "))
    numberlist.append(num)

largest_num=numberlist[0]
smallest_num=numberlist[0]
for num in numberlist:
    if num > largest_num:
        largest_num=num
    if num < smallest_num:
        smallest_num=num
print("largest number in the list is",largest_num)
print("largest number in the list is",smallest_num)"""

#13 5678
#largest=13
#smallest=13
#num=13
#1. first iteration num›largest - false, num<smallest - false
#2. second iteration num=5, largest=13, smallest=13 - true small=5
#3. third iteration num=6, largest=13, smallest=5 - f
#4. fourth iteraton num =7,largest=13,smallest= 5 - false

"""
#try out -seperate list of element as positive and negaative number list
positive = []
negative = []
number_of_elements=[10,-2,7,-3,4,5,-98]
for num in number_of_elements:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print("positive numbers",positive)
print("negative numbers",negative)"""

#Number of occurence of given number in a tuple

#1 2 3 4 5 2 3 4 5 1 6 7
"""
count=0
numbers=tuple(map(int,input("enter the numbers to be inserted: ").split()))
number_to_check=int(input("enter the number to count"))
for element in numbers:
    if element==number_to_check:
        count+=1
print(f"occurance of {number_to_check} in tuple is {count} ")"""

#split "1 2 3 4 5"-"1""2""3""4""5"
#map-(1,2,3,4,5) 

#REVERSE THE DICTIONARY
"""
data={"a":1,"b":2,"c":3}
reversed_data={}
reversed_keys=list(data.keys())  #["a","b","c"]
for key in reversed_keys[::-1]:
    reversed_data[key]=data[key]
print(reversed_data)"""

#linear search
"""
user_marks=list(map(int,input("Enter the number to be insereted: ").split()))
search_element=int(input("Enter the element to search: "))
for i in range(len(user_marks)):
    if search_element == user_marks[i]:
        print(f"Element found at index {i} ")
        break
else:  
    print("Element not found")
"""
#Fibonacci series:-0 1 1 2 3 
#a=0,b=1,c=0+1=1
#a=b,b=a,c=1+1=2
#a=1,b=2,c=1+2=3
#
"""
a=0
b=1
number_of_iteration=int(input("enter the number of iteration: "))
for element in range(number_of_iteration):
    print(a)
    c=a+b
    a=b
    b=c"""
#Prime number
"""
num=int(input("enter a number: "))
for i in range(2,num):
    if num % i == 0:
        print(" not a Prime number ")
        break
else:
    print(" prime number")"""

#Sorting


#13,89,75,10,51
#first iteration = 
# 13>89 -false
#13>75 -false
#13>10 -true (swap)
#10 89 75 13 51
#10>51 -false
#second iteration =
#  89>75 -true(swap) 10 75 89 13 51
#89>13 -true (swap)
#10 75 13 89 51
#89>51 -true (swap)
#10 75 13 51 89
#third iteration - 75>13 -true (swap) 10: 13 75

#13,89,75,10,51
#temp=num[i] 13
#num[i]=num[j] 10
#num[j]=temp 10
"""
def bubblesort(num):
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i]>num[j]:
                temp=num[i]
                num[i]=num[j]
                num[j]=temp
    return num
print(bubblesort([13,89,75,10,51]))"""

#Pattern

"""
number = int (input("Enter the number of elements: "))
for row in range(1,number+1):
    for column in range(1,number+1):
        print("*",end=" ")
    print()"""
"""
#(row numbers)
number = int (input("Enter the number of elements: "))
for row in range(1,number+1):
    for column in range(1,number+1):
        print(row,end=" ")
    print()

#column numbers

number = int (input("Enter the number of elements: "))
for row in range(1,number+1):
    for column in range(1,number+1):
        print(column,end=" ")
    print()

#left side
"""
""""
number = int (input("Enter the number of elements: "))
for row in range(1,number+1):
    for column in range(1,row+1):
        print("*",end=" ")
    print()

#left side row

number = int (input("Enter the number of elements: "))
for row in range(1,number+1):
    for column in range(1,row+1):
        print(row,end=" ")
    print()
#left side col

number = int (input("Enter the number of elements: "))
for row in range(1,number+1):
    for column in range(1,row+1):
        print(column,end=" ")
    print()"""


number = int (input("Enter the number of elements: "))
for row in range(1,number+1):
    for column in range(1,number+1):
        if row >= column:
            print("*",end=" ")
    print()