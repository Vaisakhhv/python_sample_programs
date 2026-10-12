list=["vysakh","rahul","anu","sooraj","vishnu"]
print(list)
tuple=(101,"single",2500)
print("room rent:", tuple)
room_types = {"single","double","suite"}
room_types.add("single")
print(room_types)
rules= frozenset(["no smoking","checkout on time","maintain silence"])
print(rules)
def calculate_room_bill(rent,days):
    return rent * days
bill = calculate_room_bill(2500,3)
print("total room bill:",bill)
name = input("enter guest name:")
print(name.title())
days = int(input("enter number of days stayed: "))
if days > 5:
    print("long stay")