balance=1000
print("-----ONLINE BANKING SYSTEM-----")
print("1. creating account")

print("2. deposit amount")
print("3. withdraw amount")
print("4. check balance")
print("5. transaction histroy")
print("6. exit")

choice=int(input("enter your choice: "))
if choice ==2:
    deposit_amount=int(input("enter your amount"))
    balance = balance+deposit_amount

    print("amount deposited successfully")
    print("updated balace",balance)
    interest=lambda amount:amount * 0.05
    print("Interest Calculation using Lambda:")
    print(interest(balance))
    print("Account with balance")