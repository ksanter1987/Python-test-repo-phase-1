# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?

def oops1():
    msg = input('Введіть повідомлення: ')
    if len(msg) < 6:
        raise IndexError 
    print(msg[5])

def oops2():
    try:
        msg = input('Введіть повідомлення: ')
        print(msg[5])
    except IndexError:
        print('Малувато тексту')

def oops3(): # результат той самий що і в 1-й функції oops1()
    try:
        msg = input('Введіть повідомлення: ')
        print(msg[5])
    except KeyError:
        print('Малувато тексту')


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