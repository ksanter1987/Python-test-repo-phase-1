# Lesson 2 Task 1 (The greeting program)
# Make a program that has your name and the current day of the week stored 
# as separate variables and then prints a message like this:
#      “Good day <name>! <day> is a perfect day to learn some python.”
# Note that <name> and <day> are predefined variables in source code.
# An additional bonus will be to use different string formatting methods 
# for constructing result string.

name = 'Alex'
day = 'monday'
print('Good day', name + '!', day, 'is a perfect day to learn some python.')
print('Good day'.upper(), name.center(12, '-'),'!'.upper(), day.center(12, '*'), 'is a perfect day to learn some python.'.upper())
print(('Good day ' + name) + '! ' + (day + ' is a perfect day to learn some python.'))
print(f'Good day {name}! {day} is a perfect day to learn some python.')
print(f'Good day {name}! {day} is a perfect day to learn some python.'.swapcase())
print(f'Good day {name}! {day} is a perfect day to learn some python.'.title())
print()
print()


# Lesson 2 Task 2 (Manipulate strings)
# Save your first and last name as separate variables, 
# then use string concatenation to add them together with 
# a white space in between and print a greeting.

first_name = 'Oleksiy'
last_name = 'Kuvychko'
print('Good evening ' + first_name + ' ' + last_name + '. Welcome to Python lesson')
print(f'Good evening {first_name} {last_name}. Welcome to Python lesson')
print()
print()


# Lesson 2 Task 3 (Using python as a calculator)
# Make a program with 2 numbers saved in separate variables a and b, 
# then print the result for each of the following: 
# Addition
# Subtraction
# Division
# Multiplication
# Exponent (Power)
# Modulus
# Floor division

a = 123
b = 31
print(f'Addition: {a} + {b} = {a + b}')
print(f'Subtraction: {a} - {b} = {a - b}')
print(f'Division: {a} / {b} = {a / b}')
print(f'Multiplication: {a} * {b} = {a * b}')
print(f'Exponent (Power): {a} ** {b} = {a ** b}')
print(f'Modulus: {a} % {b} = {a % b}')
print(f'Floor division: {a} // {b} = {a // b}')