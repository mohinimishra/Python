
# defining function
def my_function(name):
    print(f"My name is {name}")
    
my_function('mohini')

# returning function
def add (a,b):
    return a+b

print(add(3,5))

# default 
def introduce(name="Guest", age=18):
    return f"My name is {name} and I am {age} years old."

print(introduce())                     # Outputs: My name is Guest and I am 18 years old.
print(introduce("Bob"))                # Outputs: My name is Bob and I am 18 years old.
print(introduce(age=25, name="Charlie"))  # Outputs: My name is Charlie and I am 25 years old.

# Assignement 
"""
 Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values"""

def disctionaryData(firstname, lastname, age):
    return{
        'firstname':firstname,
        'lastname':lastname,
        'age':age
        }
val = disctionaryData('mohini', 'mishra', '20')
print(val)

val2 = disctionaryData(age='21', firstname='jack', lastname="rock")
print(val2)
    