# Creating a set using {}
my_set = {1,2,3,4, 4, 5} # retun only one value once n duplication
print(my_set) # {1, 2, 3, 4, 5}
print(type(my_set)) # output: <class 'set'>

# Creating a set from a list using the set() constructor
my_set_using_constructor = set(["python", "java"])
print(my_set_using_constructor) #{'java', 'python'}
print(type(my_set_using_constructor)) #<class 'set'>


# Creating an empty set (note: {} creates an empty dictionary)
empty_set = set()
print(empty_set) #set()
print(type(empty_set)) #<class 'set'>

# set operations

setA = {"java", "C++"}
setB = {"pyhton", "node"}
setA.add("python") # adding an element 
union = setA | setB 
print(f"Union: {union}") # Union: {'node', 'pyhton', 'java', 'C++'}
union = setB|setA
print(f"Union: {union}")  # {'python', 'C++', 'node', 'java'}

intersection = setA & setB
print(intersection) # {'python'}

difference = setA - setB # set1.difference(set2)
# Difference (elements in set1 but not in set2)
print(difference) # {'java', 'C++'}

setA.remove("python") #{'java', 'python', 'C++'}
print(my_set)

my_set.discard(3)
print(my_set)#{1, 2, 4, 5}

my_set.clear()  # will clear whole set
print(my_set)

my_set.add(9)
print(my_set)# {9}

my_set.update([10,11,12])
print(my_set) #{9, 10, 11, 12} will update value in bulk or more than one 


# Tuple
my_tuple =( 'java', "javascript")
print(my_tuple) #('java', 'javascript')

print(type(my_tuple)) #<class 'tuple'>
print(len(my_tuple)) # 2
print(my_tuple[0]) # java

my_tuple[0]="python"
print(my_tuple) #TypeError: 'tuple' object does not support item assignment



