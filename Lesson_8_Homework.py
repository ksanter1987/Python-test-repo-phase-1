# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?

my_list = ['1', '2', '3', '4', '5', '6']
def oops():
    number = int(input('Введіть число: '))
    if number > len(my_list):
        raise IndexError
    return my_list

def some_func(value):
    try:
        print(oops() * value)
    except IndexError:
        print('В списку немає стільки значень(((')


my_list2 = ['1', '2', '3', '4', '5', '6']
def oops2():
    number = int(input('Введіть число: '))
    if number > len(my_list2):
        raise KeyError
    return my_list2

def some_func2(value):
    try:
        print(oops2() * value)
    except KeyError:
        print('В списку немає стільки значень(((')


# Task 2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then 
# returns the value of squared a divided by b, construct a try-except block which raises an exception if the 
# two values given by the input function were not numbers, and if value b was zero (cannot divide by zero). 

def some_math():
    try:
        a = float(input('Введіть перше число: '))
        b = float(input('Введіть друге число: '))
        result = a ** 2 / b
        print(f'Результатом рівняння є {result}')
    except ZeroDivisionError:
        print('На нуль ділити не можна')
        raise Exception('Houston, we have a problem')
    except ValueError:
        print('Це математика, оперуйте числами')
        raise Exception('Houston, we have a problem')