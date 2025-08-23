
disctionary = {
    'username':'mohini',
    'age':10}

print(disctionary) #{'username': 'mohini', 'age': 10}
print(type(disctionary))#<class 'dict'>

# to get value of particulatr attribute
print(disctionary.get("username")) #mohini

#add to dictionary
disctionary['married'] = True
print(disctionary) #{'username': 'mohini', 'age': 10, 'married': True}

#len
print(len(disctionary)) # 3

#pop
disctionary.pop("age")
print(disctionary) # {'username': 'mohini', 'married': True}

#loop
for x in disctionary:
    print(f"x is {x}") #only geeting keys username, married

for x, y in disctionary.items():
    print(f"x is {x} : {y}") #gets both key and value   
    
# Assignement
disctionary2 = disctionary
print(f"disctionarys:{disctionary2}") #No new dictionary is created, disctionary2 and disctionary both point to the same object in memory
disctionary2["gender"] = "female"
print(f"disctionarys2:{disctionary2}") # Changes to dict2 also affect dict2 because they reference the same dictionary.
print(f"disctionarys:{disctionary}") #{'username': 'mohini', 'married': True, 'gender': 'female'}

# Copy
disctionary2 = disctionary.copy() #shaollow copy
disctionary2['hobbies']=['traveling', 'Coding']
print(f"disctionarys:{disctionary}") #{'username': 'mohini', 'married': True, 'gender': 'female'}
print(f"disctionarys2:{disctionary2}") # {'username': 'mohini', 'married': True, 'gender': 'female', 'hobbies': ['traveling', 'Coding']}

# Copy() is shallow — nested objects are shared!

disc1= {'a':[1,2,3], 'b':{'name':'mohini'}}
disc2 = disc1.copy()

disc2['a'].append(4)
disc2['c'] = {'language':'python'}

print(f"disc1 is {disc1}")# {'a': [1, 2, 3, 4], 'b': {'name': 'mohini'}} 
print(f"disc2 is {disc2}") # {'a': [1, 2, 3, 4], 'b': {'name': 'mohini'}, 'c': {'language': 'python'}}

# copy.deepCopy() for full copy

import copy 
disc3 = copy.deepcopy(disc1)
disc3['a'].append(5)
print(type(disc3['b']))
disc3['b']['age'] = "20"



print(disc3) # {'a': [1, 2, 3, 4, 5], 'b': {'name': 'mohini', 'age': '20'}}
print(disc1) #{'a': [1, 2, 3, 4], 'b': {'name': 'mohini'}}


# Clear
disctionary.clear()
print(disctionary) #{}

# to delete disctionary
del disctionary

#<------------------------------------ Assignement ------------------------------------------------------->
"""
Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values

- Create a new variable vehicle2, which is a copy of my_vehicle

- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4

- Delete the mileage key and value from vehicle2

- Print just the keys from vehicle2"""

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
# Creating a for loop to print all keys and values
for x, y in my_vehicle.items():
    print(f"key-value {x}:{y}")
    
#Create a new variable vehicle2, which is a copy of my_vehicle
vehicle2 = my_vehicle.copy()
vehicle2['number_of_tires'] = 4

vehicle2.pop("mileage")

for x in vehicle2:
    print(f"key of vehicle2 {x}")
