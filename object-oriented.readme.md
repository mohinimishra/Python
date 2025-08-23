# Object Oriet Programming (OOP)

 Object oriented programming, which is also known as OOP, is a programming paradigm based on the concepts of objects which can contain data and code.

 OP has benefits that include scalability, efficiency, and reusability.

### There's really two ways to define them.

You can define an object by behavior, or you can define an object by state.

Behavior is what the object does while the state is what the object is, and then combined, it just kind of what the object is overall.

```py
# creating a obj

class Book:
    name:str="Andy Macnab"
    price:int="250"
    
book = Book()
print(book.name, book.price)


from datetime import datetime
class TimeTeller:
    def __init__(self, time:str, day:str, year:str ):
        self.time= time
        self.day= day
        self.year=year
    

time = TimeTeller(datetime.now().day, datetime.now().year, False)
print(time.time, time.day, time.year)

    
```

Python is Dynamically Typed
Python uses type hints like year: str as hints only — not rules.

It does not enforce types at runtime (unless you add extra checks yourself).

So even if you write year:: str, Python won’t stop you from passing a boolean or anyother type , list, etc.

### How to Enforce Type Checking Yourself
If we want to make sure the input is really a str, we can Use isinstance() or convert manually
#### [View oop.py](./oop.py)

```py
from datetime import datetime
class TimeTeller:
    def __init__(self, time:str, day:str, year:str ):
        if not isinstance(time,str):
            raise TypeError(f"time must be in str")
        if not isinstance(day,str):
            raise TypeError(f"day must be in str")
        if not isinstance(year,str):
            raise TypeError(f"year must be in str")
        self.time= time
        self.day= day
        self.year=year
    

time = TimeTeller(datetime.now().day, datetime.now().year, False)
print(time.time, time.day, time.year) #  raise TypeError(f"time must be in str")

```
## Abstraction
To hide the implementation and only show nesessary info to user.

```py
from Enemy import *
    
zombie = Enemy()

print(zombie.talk()) 
# will throw err AttributeError: 'Enemy' object has no attribute 'type_of_enemy'

# first assign value to atribute type_of_enemy

zombie.type_of_enemy="Zombie"
print(zombie.talk()) # I am a Zombie. Be prepared!
print(zombie.walk_forward()) # Zombie attacking you. Your health point is 10

```
## Constructors
Are used to create and initialize an object of a class with or without  starting value.



### Example
```py
# calling constructorr 
zombie= Enemy()
```

### Type of Constructor
* Empty Constructor

    A constructor in Python is a special method called __init__() that automatically runs when you create (instantiate) an object from a class.
```py
def __init__(self):
        pass
```
* No Argument Constructor
    A no-argument constructor (also called a default constructor) is a constructor that:

    * Takes no arguments (except the required self).
    * It can be empty or contain logic that doesn’t require any external input.

```py
    def __init__(self):
        print("Enemy object created")
```

* Parameter Constructor
    
    A parameterized constructor is a constructor that accepts arguments (parameters) in addition to self so that you can pass values while creating an object.


