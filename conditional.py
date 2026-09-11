'''
if condition:
  code to be executed
elif condition:
   code to executed
else:
   code to be executed


num=int(input("Enter a number: "))
if num>=0:
    print("positive number")
else:
    print("negative number")

vowel_checker = str(input("enter a character: "))
if vowel_checker in "aeiouAEIOU":
    print("entered char is vowel")
else:
    print("not a vowel")

#even or odd
num = int(input("enter a number: "))
if num%2==0:
    print("even")
else:
    print("odd")


age = int(input("enter a age: "))
if age<18:
    print("adult")
else:
    print("not adult")

num=int(input("enter a number: "))
if num>=0:
    if num%2==0:
        print("number is positive and even")
    else:
        print("number is postive and odd")
else:
    print("negative number")
'''
#check whether given no is 3 digit or not

#for and while are entry controller loops
"""
for variable in sequence:
    code to be executed

#using range function
for variable in range(start,stop,step):
    code to be executed

start=default value is 0
stop= number - 1
step=default value is 1 for positive numbers and for negative number we need to assign

#syntax for while loop:
initialization
while condition:
    code to be executed
    updation
"""
'''
word=input("enter a word: ")
for letter in word:
    print (letter)
    

for item in [1,2,3,4,5]:
    print(item)

for element in range(11):
    print(element)
    
for element in range(5,15):
    print(element)

for element in range(10,26,5):
    print(element)

for item in range(20,10,-1):
    print(item)
'''
'''
multiple=int(input("enter a number: "))
for item in range(1,11):
    print(item*multiple)

multiple=int(input("enter a number: "))
for item in range(1,11):
   # print(multiple,"*",item,"=",item*multiple)
    print(f"{multiple}*{item}={item*multiple}")
'''
'''
value=1
iterations=int(input("Enter the number od iterations"))
while value<=iterations:
    print(value)
    value+=1

num=int(input("enter a number: "))
fact=1
while num>0:
    fact*=num
    num-=1
print("factorial=",fact)

#else with loop
for i in range(3):
      print(i) 
else: 
    print("Loop finished without break") 
#JUMPING STATEMENTS
#1.BREAK,2.CONTINUE,3.PASS
#BREAK
for i in range(1, 10):
         if i == 5:        
          break  
         print(i) '''
#continue
for i in range(1, 6):  
      if i == 3:
       continue    
      print(i) 
for i in range(1,6):
    if i == 3:
        pass
    print(i)