# week 2

# Exercise 1
"""number1 = int(input("give num "))
number2 = int(input("give another num"))
add = number1+number2
mult = number1*number2
print(f"addition of {number1} and {number2} is {add}")
print(f"multiplication of {number1} and {number2} is {mult}")
"""
# Exercise 2
'''
Create a list consisting of tuples given below:
    (1,'A')
    (2,'B')
    (3,'C')
    (4,'D')
    (1,'A')
Find a way to remove duplicates from the list
Print contents of the list before removing the duplicates and after removal

Result list should be sorted.
Create a dictionary using this list. First elements of the tuples are the keys and the second elements are values for the dictionary.
Print the dictionary
'''

my_list = [(1,'A'), (2,'B'), (3,'C'), (4,'D'), (1,'A')]
my_set = set(tuple(my_list)) # Eliminates duplicates
print(f"My list objects before removal {my_list}")
my_list=list(my_set) # Make this set a list
my_list.sort() # Sort ASC
print(f"my list objects after the removal of duplicates and sorted as ascending order. {my_list}")

# creating the dictionary


my_dict = {}
for obj in range(len(my_list)):
    key = my_list[obj][0]
    val = my_list[obj][1]
    my_dict[key] = val

print(my_dict)