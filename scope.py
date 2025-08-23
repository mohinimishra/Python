x = "10" # x define as global variable

def function():
    x = "enclosing"  # enclosing scope
    def inner():
        x="local" # local scope
        print(x)
    inner()
    
function()
        

global_value = 10
def change_global_value():
    # global_value = 21 # as a local variable
    global global_value  # declare you're modifying the global variable
    global_value = 21
    print(f"global_value {global_value}")
    return global_value
    
print(f"global_value", global_value)


def local_scope():
    scope= 45 # local scope
    print(scope)
    return scope

print(f"local_scope",local_scope()) # local_scope 10


# print(scope) #NameError: name 'scope' is not defined

def enclosing():
    x= 10
    def inner():
        #x=12    # will create new variable x inside function scope
        nonlocal x
        x=12 # modified outer x
        print(f"inner{x}")
    inner()
    print(f"outer{x}")
    
enclosing()