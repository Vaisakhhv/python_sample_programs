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