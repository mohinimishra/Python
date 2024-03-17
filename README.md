

# Learning Python Basics!

**Learn Python Basics** is an excellent introduction to Python programming, and that too in the most interactive way possible.

## Creating a Virtual Environment and The Project Folder
A Virtual Environment in Python is a self-contained directory that contains a Python installation for a particular version of Python.

```bash
python3 -m venv env
```
This command will create a directory named env.

It’s a very useful way to make sure that we’re using the right Python version when we’re working on a particular project.

Activating Virtual Environment

# Activating Virtual Environment 
```python
source env/bin/activate
```

# First Python Program
We will write a simple program that displays "Hello, World!" on the screen/terminal.

python

```python
    print("Hello, World!")
```
## Python Comments
In Python, parts of code beginning with # are called comments. For example,
```python
    # print a number
    print(25)
```

## Numbers
* Mainly we have  two type of numbers.
* Integer - 1,-1,2,90
* Float - 1.0, -20.9, 888.00

## Strings
string reperesents in python looks like -
```python
    # print a number
    print("hello")
    print('hello')
```
## Python Variables

### create variables :  

```python

greeting = "Merry Christmas"
print(greeting)

# greeting is a variable.
# It is storing a string value Merry Christmas.
# The = sign is used to assign values to variables.

```
### errors : 
```python
print(age)

#Traceback (most recent call last):
 # File "/Users/mm/github/Python/index.py", line 2, in <module>
  #  print(age)
#NameError: name 'age' is not defined
``` 




### print variables
### change values assigned to variables
We can change the value stored in variables as per our needs. For example,
```python
age = 25
print(age)
 
age = 26
print(age)

```
### Assign Value of One Variable to Another
```python
color1 = "blue"
print(color1)   # Output: blue
 
color2 = "pink"
 
# assign the value stored in color2 to color1
color1 = color2
 
print(color1)  # Output: pink
print(color2)  # Output: pink
```

### Error
```python
# create a variable
city1 = "Paris"
 
# assign city2 to city1
city1 = city2 #NameError: name 'city2' is not defined.
 
print(city1)  

```
### Legal Variables Name
Naturally, there are certain restrictions when it comes to naming variables in Python. A variable name can only consist of three things:

* alphabets
* numbers
* underscores

We can't use spaces or any other symbols when naming a variable.

### Variables Are Case-Sensitive
```python
age = 19
print(Age)   # Traceback (most recent call last):
  # File "<string>", line 2, in <module>
#ERROR!NameError: name 'Age' is not defined. Did you mean: 'age'?
```

## Print Newline (Enter Key)
we use the newline character \n in the position where we want to break the line:
```python
print("Welcome to Programiz\nThe Amazing Spider-Man")
```
## Long strings we can use using triple (single/double quotes)
```python
 string ="""
Welcome to Programiz
it must be a dictionary mapping Unicode

Character keys will be then converted to ordinals.


in the resulting dictionary, each character in x will be mapped to the
character at the same position in y. If there is a third argument, it"""

print(stirng)
```
## String Concatination
```python
first_name = 'mohini'
last_name ='mishra'
print(first_name + last_name) #output - mohinimishra
```
we can use 'f' keyword before the string or concating them this will return formatted string.
```python
name = f'hello'
print(name) # output hello
first_name = 'mohini'
last_name ='mishra'
print( name  + ' ' + first_name + ' ' +last_name) #output - hello mohini mishra
```
## Strings are muttable/or not changed
```python
name = "mohini'
name = "hello"
print(name) # will return hello 

name.replace('h', 'H')
print(name) # will return hello not Hello, to do so 

new_name = name.replace('h', 'H')
print(new_name) # will retrun now Hello

```


## REPL Helpfull command 
`type()` - help to get type of variable or value like 
```python
type(5)   # return <class 'int'> 
let name = 'Python'
type(name)   # return <class 'str'> 

```

`dir()` to get what method present in that value or variable. I will also return __method but are internal method which is not for use.

```python
let name = 'Python'
dir(name)
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

```
 `help()` - help related to class variable nd help with what there method do and other.
 Make sure to only plass class.


