#comprehensions:it provide a concise and readable way to create collections
#list comprehension generate list,
#set comprehension generate set,
#dictionary comprehension generate dictionary.
#syntax:-
#[expression for item in iterable if condition]

#list comprehension
"""
numbers=[1,3,5,2,7]
odd_numbers = [item for item in numbers if item%2 != 0]
print(odd_numbers)"""
"""
number=[1,4,5,6,2]
result=tuple(x**2 for x in number)
print(result)

cubes={item:item**3 for item in range (1,11)}
print(cubes)"""
"""
#set
elements=[2,3,4,2,6,7,6]
even_numbers={item for item in elements if item%2==0}
print(elements)"""
"""
names=["Vysakh","sasi","sabu","babu"]
uppercase=[item.upper() for item in names]
print(uppercase)

check_letter=[item for item in names if "V" in item]
print(check_letter)"""
"""
texts="breakingbad"
vowel_checker=[item for item in texts if item in "AEIOUaeiou"]
print(vowel_checker)

unique_char={item for item in texts}
print(unique_char)

asci_code={item:ord(item) for item in texts}  #ord-to generate ascii code
print(asci_code)"""
"""
languages=["python","java","sql"]
length=[len(item)for item in languages]
print(length)

first_char=[item[0] for item in languages]
print(first_char)

first_char_with_pair={item:len(item) for item in languages}
print(first_char_with_pair)"""

#LAMBDA FUNCTION
"""
new_list=[2,3,1,7,8]
squared_list=list(map(lambda iteam:iteam*iteam,new_list))
print(squared_list)

odd_list=list(filter(lambda item:item % 2!=0,new_list))
print(odd_list)

list_tuples=[
    ("sabu",32,"malpuram"),
    ("jan",21,"daravi"),
    ("gunda",78,"bombay"),
    ("manikam",15,"mumbai")
]

ascending=sorted(list_tuples,key=lambda iteam:iteam[1])
print(ascending)"""
"""
employes={
    "sabu":23,
    "hambu":56,
    "manu":20,
}
sorted_dictionary=dict(sorted(employes.items(),key=lambda item:item[1]))
print(sorted_dictionary)"""

from functools import reduce
list=[2,3,1,7,8]
sum_of_elements=reduce(lambda x,y:x+y,list)
print(sum_of_elements)