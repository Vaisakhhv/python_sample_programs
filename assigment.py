"""
Customer_name=(input("Enter your name: "))

Food_iteam_name=(input("Enter food iteam name"))
Quantity=(int(input("Enter the quatity")))
Price_per_item=(float(input("Enter price per iteam")))
Delivery_Distance=(float(input("Enter the distance in Km")))

print("Customer name:", Customer_name)
print("Food iteam name:", Food_iteam_name)
print("Quatity of the food:" ,Quantity)
print("Price per iteam:", Price_per_item)
print("Delivery distance in km:", Delivery_Distance)

#data type using type()

print("Customer Name type:", type(Customer_name))
print("Food Item type:", type(Food_iteam_name))
print("Quantity type:", type(Quantity))
print("Price Per Item type:", type(Price_per_item))
print("Delivery Distance type:", type(Delivery_Distance))

#memory locations id()

print("Customer Name type:", id(Customer_name))
print("Food Item type:", id(Food_iteam_name))
print("Quantity type:", id(Quantity))
print("Price Per Item type:", id(Price_per_item))
print("Delivery Distance type:", id(Delivery_Distance))

#calculate finall bill amount

Total_food_Cost = Quantity*Price_per_item
Delivery_charge = 10 + (Delivery_Distance * 5)
final_bill_amount = Total_food_Cost + Delivery_charge
implicit_conversion_example = Quantity + Delivery_charge

print("Quantity:", Quantity)
print("Delivery Charge:", Delivery_charge)
print("Quantity + Delivery Charge:", implicit_conversion_example)

print("Result type:", type(implicit_conversion_example))

quatity_int = int(Quantity)
price_float = float(Price_per_item) 
distance_float = float(Delivery_Distance)

print("Quantity:", Quantity)
print("Delivery Charge:", Delivery_charge)
print("Quantity + Delivery Charge:", implicit_conversion_example)

print("Is quantity an integer?",
      isinstance(Quantity, int))

print("Is price a float?",
      isinstance(Price_per_item, float))

print("Is final bill a float?",
      isinstance(final_bill_amount, float))
print("          ONLINE FOOD BILL")


print("customer name:" ,Customer_name)
print("Food Item          : ", Food_iteam_name)
print("Quantity            : ", Quantity)
print("Price Per Item      : ₹", Price_per_item)
print("Delivery Distance   : ", Delivery_Distance, "KM")
print("----------------------------------------")
print("Total Food Cost     : ", Total_food_Cost)
print("Delivery Charge     : ₹", Delivery_charge)
print("----------------------------------------")
print("FINAL BILL          : ₹", final_bill_amount)
"""
# Online Banking System

balance = 10000

print("----- ONLINE BANKING SYSTEM -----")

print()
print("1. Create Account")
print("2. Deposit")
print("3. Withdraw")
print("4. Check Balance")
print("5. Exit")

print()

choice = int(input("Enter your choice: "))

# Deposit
if choice == 2:

    deposit_amount = int(input("Enter Deposit Amount: "))

    balance = balance + deposit_amount

    print()
    print("Amount Deposited Successfully")
    print("Updated Balance:", balance)

    # Lambda Function
    interest = lambda amount: amount * 0.05

    print()
    print("Interest Calculation using Lambda:")
    print(interest(balance))

    # Map / Filter
    accounts = [15000, 20000, 25000, 8000, 5000]

    eligible_accounts = list(
        filter(lambda amount: amount > 10000, accounts)
    )

    print()
    print("Accounts with Balance > 10000:")
    print(eligible_accounts)

    # Sorted + Lambda
    customer_names = ["Rahul", "Anu", "Sheha"]

    sorted_names = sorted(
        customer_names,
        key=lambda name: name
    )

    print()
    print("Sorted Customer Names:")
    print(sorted_names)

    # PIN Verification using Recursion
    def pin_verification(attempt):

        if attempt > 3:
            print()
            print("Maximum Attempts Reached")
            return

        print("PIN Verification Attempt:", attempt)

        pin = input("Enter PIN: ")

        if pin == "1234":
            print("PIN Verified Successfully")
            return

        pin_verification(attempt + 1)


    pin_verification(1)


elif choice == 1:

    print()
    print("Create Account")


elif choice == 3:

    withdraw_amount = int(input("Enter Withdraw Amount: "))

    if withdraw_amount <= balance:

        balance = balance - withdraw_amount

        print()
        print("Amount Withdrawn Successfully")
        print("Updated Balance:", balance)

    else:

        print()
        print("Insufficient Balance")


elif choice == 4:

    print()
    print("Current Balance:", balance)


elif choice == 5:

    print()
    print("Thank You for using Online Banking System")


else:

    print()
    print("Invalid Choice")


