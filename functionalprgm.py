#pure function
#-->for same input they give same outputs
"""
def addition(num1,num2):
    return num1+num2
print(addition(2,6))
print(addition(2,6))"""
#eg2
"""
def pure_function(numbers):
    new_list=[]
    for item in numbers:
        new_list.append(item*2)
    return new_list"""
#print(pure_function([1,2,3,4,5]))
'''
original_list=[1,2,3,4,5]
modified_list=pure_function(original_list)
print(original_list)
print(modified_list)'''

#FIRST CLASS FUNCTION:-assign a function to variable
""""
def greet(name):
    return f"hello {name}"
#print(greet("vysakh"))
message=greet("vysakh")
print(message)
#passing fn as an argument


def greet():
    print("hello")
def display(func):
    func()
display(greet)"""

#return a fn from another fn
"""
def outer():
    def inner():
        print("hello form inner function")
    return inner
result=outer()
result()"""

#store fn in a list
"""
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
function=[add,sub]
print(function[0](2,3))"""

#HIGHER ORDER FUNCTION
""""
def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def calculate(operation,x,y):
    return operation(x,y)
print(calculate(add,2,3))"""

#ITERATOR:- to retrieve data one by one we us iterators by next
"""
iter_list=iter([1,2,3,4])
print(next(iter_list))
print(next(iter_list))"""


#GENERATOR:-to generate one by one
"""
def count_down(n):
    while n>0:
        yield n
        n-=1
count=count_down(4)
print(next(count))
print(next(count))"""

def square_num():
    for i in range(1,11):
        yield i*i #return one by one
square=square_num()
print(next(square))#next-->one by one fetching
print(next(square))

#decorator:- fn return another fn by adding a decator
"""def calculator(func):
    def inner(*args):
        print("calculating two numbers:")
        result=func(*args)
        print("final output obtained: ")
        return result
    return inner
@calculator
def add(num1,num2):
    return num1+num2

@calculator
def sub(num1,num2):
    return num1-num2
print(add(2,3))
print(sub(4,3))"""