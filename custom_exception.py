'''
class CustomException(Exception):
    pass
def check_number(num):
    if num<0:
        raise CustomException("not allowed negative numbers")
    return num

try:
    result=check_number(-7)
except CustomException as e:
    print(e)
else:
    print(result)'''


'''
class NameTooShortError(Exception):
    pass
name = input("enter your username: ")
try:
    if len(name)<8:
        raise NameTooShortError("want 8 letters")
except NameTooShortError as e:
    print(e)
else:
    print(name)'''
'''
class InsufficeientBalanceError(Exception):
    pass
amount=int(input("enter the amount to withdraw: "))
total_amount=5000
try:
    if amount>5000:
        raise InsufficeientBalanceError("insufficeintbalance")
except InsufficeientBalanceError as e:
    print(e)
else:
    balance=total_amount-amount
    print(f"{amount} is created  the remaining balance is {balance}")'''
