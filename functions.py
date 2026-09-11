"""
def function_name(parmeters):
    code to be executed
"""
"""
def welcome():
    print("welcome vysakh")

welcome()
"""
"""
def greeting(username,userage):
    print(f"welcome {username},you are {userage} year old")
greeting("vysakh",21)
"""
"""
def addition(num1,num2):
    return num1+num2
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print(addition(num1,num2)) 

"""
"""
#positional argument
def book_ticket(moviename,customername,seats,ticketprice):
    totalprice=seats*ticketprice
    return f"{customername} booked {seats} tickets for {moviename}. Total amount: {totalprice}"
print(book_ticket("breakingbad","vysakh",2,250))
"""
#keyword argument
"""
def customer_details(customername,customerage,city):
    print(f" {customername} is {customerage} years old lives in {city}")
customer_details(customername="vysakh",customerage=12,city="kayamakulam")

"""
#default arguments
'''

def booking_status(customername="Brian",status="confirmed",screen="screen1")
    print(f"{customername} booking status is {status}. The screen allocated is {screen}")
booking_status()
booking_status("vysakh")'''
#multiple arguments
'''
def calculate_bill(*ticketprices):
    print(f"ticketprices : {ticketprices}")
calculate_bill(150,130,120,110)'''
#try out kwargs
#
# ===========================================
#built in function
#============================================
"""
print(len("vysakh"))
print(sum([1,2,3,4]))
print(min([2,3,1,4]))
print(max([6,8,3,2]))
print(sorted([4,2,5,6,7,9]))
print(sorted([2,3,34,1],reverse=True))"""#for decending order

#legb rule
"""
def student_details():
    name = "vysakh"
    print(f"student name{name}")
student_details()
print("student name : ",name)"""

#golbal variable
'''
college_name="mar ivanios college"
def display():
    print("collage name: ",college_name)
display()
print("college name: ",college_name)
'''
#enclosing variable
'''

def department():
    department_name="bca"
    def student():
        print("department name :",department_name)
        student()
department()'''
"""
tax=50#global varieable
def shopping():
    discount=100#enclosing
    def bill():
        amount=2000
        total_amount=amount-discount+tax
        print(f"total amount is : {total_amount}")
    bill()
shopping()
"""
#recursive functions
"""
def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
num=int(input("enter a number: "))
print(factorial(num))

#working
num=6
6*factorial(5)
6*5*factorial(4)
6*5*4*factorial(3)

6*5*4*3*2*factorial(1)
"""
#lambda funtion
#LAMBDA ARGUMENTS:EXPRESSION SYNATAX
"""
def add(num1,num2):
    return num1+num2
print("total: ",add(3,2))
"""
"""
add= lambda a,b:a+b
print(add(3,2))
"""
'''
square=lambda num:num*num
print(square(2))
'''
''''
even=lambda num: num %2 == 0
print(even(2))

is_odd=lambda x:x%2!=0
print(is_odd(7))

smallest=lambda a,b,c:min(a,b,c)
print(smallest(2,3,4))

are =lambda l,b:l*b
print(are(1,2))

people = [("Vysakh", 21), ("Rahul", 25), ("Arun", 19), ("Akhil", 23)]

people.sort(key=lambda x: x[1])

print(people)'''
def student_info(**data):
     for key, value in data.items():
         print(key,":",value)
student_info(name="Ravi", age=18, marks=85) 