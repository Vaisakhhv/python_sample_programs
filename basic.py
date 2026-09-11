"""
print("Welcome to python programming")
#getting user inputs
student_name=input("enter your name: ")
student_age=int(input("enter your age: "))
student_mark=float(input("enter your mark: "))
is_present=bool(input("Is present or not(T/F): "))
languages_known=input("enter the languages known:").split(",")
#printing the data
print("The student name is: ",student_name)
print("The student age is: ",student_age)
print("The student mark is: ",student_mark)
print("Present or not: ",is_present)
print("languages known: ",languages_known)

#type functions

print(type(student_name))
print(type(student_mark))
print(type(student_age))
print(type(is_present))
print(type(languages_known))

#id()-built in fun that returns unique identity of an object during its life time

num1=10
num2=20
num3=30
print(id(num1))
print(id(num2))
print(id(num3))

list1=[1,2,3]
list2=[1,2,3]
print(id(list1))
print(id(list2))
"""
value1=25.6
value2=30
print(isinstance(value2,float))
print(isinstance(value2,(int,float)))
'''
#implicit type coversion
data1=10
data2=20.5
data3=data1+data2
print(data3)

data4="30"
data5="45"
data6=data4+data5
print(data6)'''
#explict
age=20
age=float(age)
print(type(age))
