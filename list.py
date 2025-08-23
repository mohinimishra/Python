# my_list= ['apple', 'js', 'rubby', 'python']
# print(my_list)
# print(my_list[0])

# my_list[0]= "mohini"
# print(my_list)
# print(len(my_list))
# print(my_list[2:4])

# my_list.append('new')
# print(my_list)
# my_list.insert(0,'coding')
# print(my_list)
# print(my_list.remove('new'))
# print(my_list.pop(0))
# my_list.sort()
# print(my_list)


list = ['mm', 1, False, True , {"python"}]
# print("list",list)
# print("lenght",len(list))
# print("value",list[4])
list.append('list in python')
list.append([{"language", "hindi"}])
list_obj = list[len(list)-1][0]
print(list[len(list)-1][0])
for x in list_obj: 
    print(f"x:{[x]}")
    
print(list[0:3]) # output: ['mm', 1, False]

list.append("new") 
print(list) #output: ['mm', 1, False, True, {'python'}, 'list in python', [{'language', 'hindi'}], 'new']
list.insert(0, "first value") # output: ['first value', 'mm', 1, False, True, {'python'}, 'list in python', [{'hindi', 'language'}], 'new']
print(list)



## Assignement
"""
- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""

zoo = ['monkey', 'cat', 'owl', 'lion', 'rat']
zoo.pop(3) # deleteing inedex 3rd
print(zoo)
zoo.append('tiger')
zoo.pop(0) # deleteing inedex 3rd
print(zoo)
print(zoo[0:3])

