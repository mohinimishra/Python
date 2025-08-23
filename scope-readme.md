# Scope

In Python, scope refers to the visibility or accessibility of variables in different parts of your program. Understanding scope is crucial for managing variables and avoiding conflicts. Here's a detailed explanation of how scope works in Python.

## How Scope Works: LEGB Rule
Python checks for variable names in the following order:

| Scope Level   | Description                             | Example Context               |
| ------------- | --------------------------------------- | ----------------------------- |
| **L**ocal     | Inside the current function/block       | Variables inside a function   |
| **E**nclosing | In enclosing (outer) functions          | Nested functions              |
| **G**lobal    | At the module (file) level              | Top-level code in your script |
| **B**uilt-in  | Python's built-in names (e.g., `len()`) | Provided by Python itself     |

## Global Scope?
Variables declared outside of all functions.

Accessible everywhere in the same module/file.

Use global keyword to modify it from inside a function.
```py
x = 10  # global

def change_global():
    global x
    x = 20  # changes the global variable

change_global()
print(x)  # Output: 20
```
Without the global keyword, Python treats x inside the function as a local variable.

## Local Scope?
Variables declared inside a function.

Only accessible within that function.

Disappear once the function exits.
```py
def my_func():
    y = 5  # local variable
    print(y)

my_func()
# print(y)  # NameError: y is not defined
```
## Enclosing Scope (a.k.a. nonlocal)
Occurs in nested functions — variables defined in the outer function are accessible to the inner one.

Use nonlocal to modify the outer variable.

```py
def outer():
    x = 10

    def inner():
        nonlocal x
        x = 20

    inner()
    print(x)  # Output: 20

outer()

```

## Rules of nonlocal
You can only use nonlocal inside a nested function.

The variable must exist in the immediately enclosing scope (not global).

You can’t use nonlocal to refer to global variables (use global for that).