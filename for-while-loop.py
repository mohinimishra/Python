list =[1,2,3,4]
#For loop
for iterator in list:
    print(iterator)

# internal beghaviour of for loop
for x in range(1,6):
    print(f"x is {x}")
     
sum = 0
for x in list:
    sum += x
    
print(sum)


days =["monday", "tuesday", "wednesday", "Thursday"]
for x in days:
    print(f"Happy {x}")


# While Loop
i=0
while i<5:
    i+=1
    if i==3:
        continue #dont execute the rest of the code and go loop
    print(i)
else:
    print(i)

# Loops Assignment
"""
Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

- Create a while loop that prints all elements of the my_list variable 3 times.

- When printing the elements, use a for loop to print the elements

- However, if the element of the for loop is equal to Monday, continue without printing"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i=0
while i <3:
    for x in my_list:
        if x == "Monday" :
            print("==================")
            continue
        else:
            print(x)
    i+=1