#Object - is an entity having state behaviour and identity
#eg - pen -->identity -its name state -- color,brand,model behaviour -- write,draw
#Class - is a group of similar object or its a user defined datatype
#There are 4 basic principles or pillars of  OOPS
#1.Inheritance
#2.Polymorphism
#3.Abstarction
#4.Encapsulation
'''
class Student:
    def display(self):
        print("i am a student")
student_object=Student()   #OBJECT CREATED
student_object.display()'''

#CONSTRUCTOR - is special type of method in python
#mainly used for initialising an object,it will be automatically called when an object is created
'''
class Employee:
    def __init__(self):
        print("default contructor is called")
employee_object=Employee()

#constructor with parameter

class Car:
    colour="red"
    def __init__(self,brand,model):  #instance variable:- inside function
        self.brand=brand
        self.model=model
car=Car("bmw","m5")
print(car.brand)
print(car.model)
car1=Car("mercedez","amg")
print(car1.brand,car1.model,car1.colour)'''

"""
class Library:
    def __init__(self,book,author):
        self.book=book
        self.author=author
    def book_count(self,count):
        self.count=count

library=Library("kurrup","vysakh")
print(library.book,library.author)
library.book_count(2)
print(library.count)"""

#1.INHERITANCE-passing the properties parent to class
#1.SINGLE LEVEL
"""
class User:         #base class or parent class or super class
    def login(self):
        print("user logged in")
class Influncer(User):     #child class/sub class/derived class
    def postreels(self):
        print("influncer post a new reel")
influncer=Influncer()
influncer.login()
influncer.postreels()"""

#2Multilevel inheritance
"""
class Vehicle:
    def category(self,mode):
        print("mode of transport :",mode)
class Car(Vehicle):
    def vechicle_category(self,vehicle_type,colour):
        print("Type of vechicle: ",vehicle_type)
        print("colur of vehicle: ",colour)
class ElectricCar(Car):
    def car_type(self,brand,category,variant,price):
        print(f" vehicle brand is {brand} and the category is {category}.Its variant is {variant} having price {price}")
ecar=ElectricCar()
ecar.category("road")
ecar.vechicle_category("car","blue")
ecar.car_type("audi","electric","r8","5 crore")"""

#MULTIPLE INHERITANCE
"""
class ImageUpload:
    def uploadimage(self,username,imagename):
        print(f"{username} posted {imagename} successfully")
class ReelUpload:
    def uploadreels(self,reel_title,reel_duration):
        print(f"uploaded reel is {reel_title} of {reel_duration} seconds")
class Instagram(ImageUpload,ReelUpload):
    def user_analytics(self,user_name,owner,reaction):
        print(f"{user_name} is having a {owner} account with {reaction} reaction on post uploaded") 
insta=Instagram()
insta.uploadimage("vysakh","vyom")
insta.uploadreels("flower_reel","15")
insta.user_analytics("bhaa","meta","1000000")"""


#try out hybrid,hyarchicel
"""
class Account:
    def details(self,):
        print("account details",)
        super().details()
class Loan:
    def details(self):
        print("loan details")
class Customer(Account,Loan):
    def details(self):
        print("customer details")
        super().details()  #MRO METHOD RESOLUTION ORDER(same name:details have to all 2 use this method)
blah=Customer()
blah.details()"""

#POLYMORPHISUM:- representing single object in may ways
#There are two types
#1.method overloading:- same class ,same method ,different arguments eg: facebook login like number or email or username password
#2.method overriding:- different class, same method ,same parameters eg: account login in different apps

#METHOD OVERLOADING
"""
class Calculator():
    def addition(self,num=0,num1=0,num2=0):
        return num+num1+num2
cal=Calculator()
print(cal.addition(2,3))
print(cal.addition(2,34,55))
print(cal.addition(23))

class Facebook():
    def login(self,email=None,password=None,phone_number=None):
        if email and password:
            print(f"login through email id : {email}")
        elif phone_number and password:
            print(f"login through mobile num: {phone_number}")
        else:
            print("Invalid login")
facebook=Facebook()
facebook.login(email="vys@gmail.com",password="123")"""
#facebook.login(phone_number="677675443",password="123")

#try out:payment cash,card,upi
"""class Payment():
    def pay_using(self,card=None,upi=None,)"""

#2.OVERRIDING METHOD
"""
class Employee:
    def work(self):
        print("working as employee")
class Manager(Employee):
    def work(self):
        print("working as manager")
        super().work()
manager=Manager()
manager.work()

#3.Abstraction - hiding implementation details from the user eg:atm withdrawal
#inherit then abstraction

from abc import ABC,abstractmethod

class Vechicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

class Car(Vechicle):#pass-act as a placeholder
    def start_engine(self):
        print("car started using key")
    def stop_engine(self):
        print("car stopped using key")
car_object=Car()
car_object.start_engine()
car_object.start_engine()
#Vechicle_object=Vechicle()#cannot instantiate abstract class we cannot create object when class is abstract.(ABC)
#if a class is abstarct,all the abstarct methods must be implemented in its child class
 
#encapsulation-Data hiding mechanism
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age #__private variable

    def show_age(self):
        print(self.__age) 

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age>0:
            self.__age=age
        else:
            print("age must be positive")

person_object=Person("Vysakh",22)
print(person_object.name)
#print(person_object.age)#cannot access outside the class as its is a private variable
person_object.show_age()
person_object.set_age(25)   
print(person_object.get_age())
#updation of a value-setter(),getter()-we can access it-->for reading and writting  
"""


#DUCK TYPING:if an object behave like the required object python doesnot care about its actual class
"""
class PDF:
    def print_document(self):
        print("Printing PDF")

class Word:
    def print_document(self):
        print("Printing word")

def print_file(file):
    file.print_document()

pdf=PDF()
word=Word()

print_file(word) """#print file function doesnot check whether object is pdf or word,it only check whether object has print

#Composition : one class contains object of another class(has a relationship)
"""
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine=Engine()

    def start_car(self):
        self.engine.start()
        print("car started")

car=Car()
car.start_car()"""

#name mangling

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def show_balance(self):
        print("balance",self.__balance)
bankaccount=BankAccount(4500)

bankaccount.show_balance()