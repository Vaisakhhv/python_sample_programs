#1.string-immutable data structure
# list-[]-ordered collection,mutable,allow dulpicates,can be accesed using indexing
#tuple-()ordered collection,inmutable,allow dulpicates,can be accesed using indexing
#set{}unodered collectiomn,mutable,doesnt allow duplicate,cannot be accesed using indexing
#dictionary_{key:value}ordered collection,value can be changed,allow duplicat value,can be accesed using key

username="vysakh"
#indexing
'''
0   1  2  3  4  #positiveindexing
-5 -4 -3 -2 -1  #negativeindexing
v   y  s  a  k
1   2  3  4  5 #length
'''
""""
print(username[2])
print(len(username))
print(username[-1])

#SLICING

#[start:stop:step]
#start:- default value will be zero
#stop:- value-1
#step:- number  of skips(defaultly 1 for positive numbers)

data="python is a programming language"
print(data[:8])
print(data[2:8])
print(data[2:12:3])
print(data[6:])
print(data[1:10:-2]) #it will not work
print(data[10:1:-2])
print(data[::-1])
print(data[::-2])
print(data[::-3])
print(data[1:8:2])
"""
""""
#STRING METHOD
text="python is simple"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.startswith("yt"))
print(text.endswith("simple"))
text[0]="r"
print(text)#not will work beacuse string imutable
print(id(text))
uppercase=text.upper()
print(id(uppercase))"""
""""
#LIST
userdata=["vysakh",21,"tvm"]
print(userdata)
userdata.insert(1,"kgi")
userdata.append(2026)
userdata.extend("python")
userdata.append(["eng","hindi","mal"])
print(userdata)
print(userdata[11])
print(userdata[11][0])
userdata.extend (["html","css"])
print(userdata)
userdata[0]="VYSAKH"
print(userdata)
userdata.remove("tvm")
print(userdata)
userdata.pop(3)
print(userdata)
userdata.reverse()
print(userdata)
"""
""""
#TUPLE-IMMUTABLE DATA STRUCTURE
tuple1=(1,2,3,4,5)
print(tuple1)

#NESTED TUPLE

tuple2=("vysakh","Sreesha","swami",(99,2,1))
print(tuple2)

#TUPLE UNPACKING
person=("vysakh",23,"alapuzha")
name,age,palce=person #SEPRATELY I CAN PRINT THE OUTPUT
print(name)

num=(10,20,30,40,50)
a,b,*c=num
print(c)

num1=(10,20,30,40,50)
f,*g,h=num1
print(f)
print(g)
print(h)

num2=(10,20,20,30,30,40,20,50)
print(num2.count(20))
print(num2.index(30))
print(num2[2]) 
"""
""""
name=input("enter a string:")
count=0
for char in name:
    count+=1
print("the count is:",count)
"""
""""
user_name = input("enter a string:")

for char in user_name:
    if user_name.count(char) == 1:
        print("first non-repeating character:", char)
        break
else:
    print("there is no non-repeating character")
#repeating character index,second non repeting charaacter,without using the count function
#find the index of frist repeating char
text = "hello"

for i in range(len(text)):
    for j in range(i + 1, len(text)):
        if text[i] == text[j]:
            print("Repeating character:", text[i])
            print("Index:", i)
            break
    else:
        continue
    break
#second non repeating character
text = "swiss"

first = None
second = None

for i in range(len(text)):
    found = False

    for j in range(len(text)):
        if i != j and text[i] == text[j]:
            found = True
            break

    if not found:
        if first is None:
            first = text[i]
        else:
            second = text[i]
            break

print("Second non-repeating character:", second)
#count element without using count
t = (1, 2, 2, 3, 2, 4)

element = 2
count = 0

for x in t:
    if x == element:
        count += 1

print("Count:", count)
"""
#========================
#SET-{},unordered collection of mutable ones,no duplicates
student1={"english","hindi","malayalam"}
student2={"english","hindi","python"}
student3={"python","urudu"}
student1.add("c")
'''student1.add{"kannada"marathyi}#error because only one argument just like append'''
student1.update(["c++","java"])#FOR MORE ELEMENTS TO ADD
print(student1)
student1.pop()
print(student1)
#student1.remove("arabi")
#print(student1)
# #rasises a key error when the key is not found
student1.discard("english")
print(student1)
#union,intersection ,difference 
#UNION-among all will print
print(student1)
print(student2)
print(student1.union(student2))
print(student1|student2)

#INTERSECTION-common

print(student1)
print(student2)
print(student1.intersection(student2))
print(student1&student2)

#DIFFERENECE-print not common no student1
print(student1)
print(student2)
print(student1-student2)
print(student1.difference(student2))

#SYMMETRIC DIFFERENCE-print all from student1 and student2 not common

print(student1)
print(student2)
print(student1.symmetric_difference(student2))
#issupset issuperset  isdisjoin note

#FROZEN SET -IMMUTABLE

fs1=frozenset("Anandu")
fs2=frozenset([1,2,3,4,2,3,4])
print(fs1)
print(fs2)
#DICTIONARY

student={
    "name":"Vysakh",
    "age":23,
    "place":"kayamakulam",
}
print(student)
print(student["name"])

info=dict(city="tvm",state="keralam")
print(info)
print(info.keys())
print(info.values())
print(info["city"])
student.pop("age")
print(student)

for key,value in student.items():
    if key=="name":
        print(key,value)

employee={
    "emp1":{
        "name":"Vysakh",
        "age":23
    },
    "emp2":{
        "name":"sree",
        "age":21
    },
    "emp3":{
        "name":"venu",
        "age":56
    }

}
print(employee["emp1"]["age"])