"""
1.Arthmetic operators
2.Assignment operators
3.Logical
4.Comparison
5.Bitwise
6.Membership
7.Identity

print("Arithemetic operators")
price_per_phone=20000
quatity=5
total_price=price_per_phone*quatity
average_price=total_price/quatity
gst_added=200
final_price=total_price+gst_added
discount_amount=1000
final_price=final_price-discount_amount
number_of_persons=3
remaining_price=final_price%number_of_persons
floor_division=final_price//7

print("price per phone is: ",price_per_phone)
print("quatity of the phone is :",quatity)
print("total price of the phone is : ",final_price)
print("average price of the phone is : ",average_price)
print("gst of the phone is : ",gst_added)
print("final price of the phone is : ",final_price)
print("discount amount is : ",discount_amount)
print("final price is : ",final_price)
print("number of persons is : ",number_of_persons)
print("remaining price is : ",remaining_price)
print("floor division is :",floor_division)
"""
#Assigment operators


score=100
score+=50
score/=2
print(score)
""""
#--------------------
#logical operator
#================

and -both condition must be true
or- any of the condition must be True
not-opposite of that condition
#and operators
username="vysakh"
password="123"
enter_username = (input("enter username"))
enter_password = (input("enter your password"))
if username == enter_username and password == enter_password:
    print("login succesfully")
else:
    print("incorrect")
#=================================
#or operators
#==============================

day=input("Enter a day")
if day == "Saturday" or day == "Sunday":
    print("Holiday")
else:
    print("working day")



#============================
#not operators
#======================

logged_in=True
if not logged_in:
    print("login successful,welcome user")
else:
    print("please login")
"""
#=======================================
#membership
#membership operartor : checks whwther an element is present or not keywors"in" and "notin"
'''
movies = ["lost","breaking bad","better call saul"]
movie = input("Enter a movie: ")
if movie in movies:
    print("Available")
else:
    print("Movie is not available")'''

#========================================
#not in
#========================================
'''
employes = ["vysakh","manu","sooraj"]
employe = input("Enter the employe name: ")
if employe not in employes:
    print("Access denied")
else:
    print("Access granted")
'''
#===========================
#identity operators->check whether memory locations is same or not
#===========================
'''
value1=35
value2=35
print(value1 is value2)
print(value1==value2)
'''
'''
list1=[1,2,3]
list2=[1,2,3]
print(list1 is list2)#check whether id is true
print(list1==list2)#check wheteher value is true
'''
#=============================
#bitwise operators
#=============================
"""
a=5
b=3
print(a & b)

# 0 1 0 1
# 0 0 1 1
# 0 0 0 1 -->when and gate is used only 1,1 the result will be 1

print(a | b)

print(a^b)

#0 1 0 1
#0 0 1 1
#0 1 1 0

print(~a)

print(5<<1)#5*2^1
print(5>>2)#5%2^2

"""