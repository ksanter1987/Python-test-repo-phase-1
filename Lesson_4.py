# Task 1
# The greatest number
# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

import random
i =0
random_list = []
while i < 10:
    random_number = random.random()  
    random_list.append(random_number)
    i += 1
print(random_list)
print()
print(max(random_list))
print(n)

# Task 2
# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing
# the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

import random
i =0
index = 0
random_list1 = []
random_list2 = []
while i < 10:
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)   
    random_list1.append(random_number1)
    random_list2.append(random_number2)
    i += 1
print(random_list1)
print(random_list2)
common_list = list(set(random_list1) & set(random_list2))
print(common_list)


# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible 
# by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

i = 0
our_list = []
special_list = []
while i < 100:
	our_list.append(i + 1)
	if (i + 1) % 7 == 0 and (i + 1) % 5 != 0:
		special_list.append(i + 1)
	i += 1
print(our_list)
print()
print(special_list)