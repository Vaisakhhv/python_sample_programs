""""
store_data=open("newfile.txt","w") #w-automatical file will create
store_data.write("Welcome to python programs")
print(store_data)
store_data.close()

read_data=open("newfile.txt","r")
print(read_data.read())
read_data.close()

append_data=open("newfile.txt","a")
append_data.write("\npython is an interpreted lanaguage")
print(append_data)
append_data.close()


read_data=open("newfile.txt","r")
print(read_data.read())
read_data.close()

#using context manager

with open("newfile.txt","r") as f:
    print("current position: ",f.tell())
    f.read(6)
    print("after read position is: ",f.tell())
    f.seek(4) #used to move position
    print("after seek :",f.tell()) 
    print(f.read())"""

"""
with open("nature.jpg","rb") as data: #rb:-read binary
    print(data.read())"""
"""
data=open("delete_file.txt","x") #x:-for  create new file
print(data)
data.close()

file_path="delete_file.txt" #delete the file
import os
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted succesfully")
else:
    print("file doesnot exits")"""

#serialization


import pickle
data={
    "students":["vysakh","raja","rani"]

}


#Serialization - saving data to file

with open("user_details.pkl","wb") as f:
    pickle.dump(data,f)
    print("data is serialized to user details")
#Deserialization retrieving data
with open("user_details.pkl","rb") as f:
    pickle.load(f)
    print("data is deserialized from user details") 

#serialization saving data into memory
"""
dump_data=pickle.dumps(data) #save to pkl 
print("data is serialized to bites: ",dump_data)

load_data=pickle.loads(dump_data) #read from pkl
print("deserialization data to bytes: ",load_data)"""

#JSON Serialization 
import json 
with open("data.json", "w") as f: 
    json.dump(data, f) 
with open("data.json", "r") as f: 
    data = json.load
