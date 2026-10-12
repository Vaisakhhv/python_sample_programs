#unexpected events are called exception,that we can resolve or handle
#eg:forgot password etc...(exception handling-resolving problem)
#keywords:1.try-what are the types of problem that gonna to form
#2.except-problem solver(try+expect =problem resolve)
#3.finally-normal used for the cloding the connection with the database
'''
print("statement 1")
print("statement 2")
print("statement 3")
try:
    value1=10
    value2=0
    value3=value1/value2 #zero division error
except ZeroDivisionError:
    print("denominator cant be zero")
print("statement 4")
print("statement 5")'''

#try except else
'''
numerator=int(input("enter the numerator"))
denominator=int(input("enter the denominator"))
try:
    quotient=numerator/denominator
except ZeroDivisionError:
    print("denominator cant be zero")
else:
    print("quotient")'''

#TYPE ERROR-
'''
try:
    num1="15"
    num2=25
    add=num1+num2
    print(add)
except TypeError:
    print("string cant be added with integer value")'''

#INDEX ERROR-index out of range

'''
numbers=[1,2,3,4,5]
try:
    print(numbers[10])
except IndexError:
    print("index out of range")

#KEY ERROR-DICTIONARY
book_details={
    "book_id":2,
    "book_name":"atomic habits"
}
try:
    print(book_details["book author"])
except KeyError:
    print("key not found")'''
#FILENOTFOUNDERROR- searching for a non available file
'''
try:
    with open("test_file.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")'''

#IMPORT ERROR
'''
try:
    from math import square
except ImportError as e:
    print(e)#show what is the error by using as e like'''

#ATTRIBUTE ERROR-giving non functionality to any datastructure

'''
try:
    user_value="welcome"
    print(user_value.add())
except AttributeError as f:
    print(f)'''

#Value error-when no proper value is given
'''
try:
    data=int("vysakhh")
except ValueError as d:
    print(d)'''

#NAME ERROR-when printing an illatha oru variable
'''
try:
    print(student)
#except NameError as h:
    #print(h)
finally: 
    print("executed normally")'''

#MULTIPLE EXCEPTION-more than one error(handle one excepetion at a time)
'''
try:
    user_value="welcome"
    print(user_value.add())
    data=int("vysakhh")
except ValueError as d:
    print(d)
except AttributeError as f:
    print(f)'''
    #resolve the frist problem in multi exception as we can a seen on the terminal box,

#MULTIPLE EXCEPTION USING ANOTHER METHOD


try:
    user_value="welcome"
    print(user_value.add())
    data=int("vysakhh")
except (ValueError,AttributeError) as d:
    print(d)
    #same output but different method