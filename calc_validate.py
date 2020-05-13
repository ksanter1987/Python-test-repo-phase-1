def positive_integer_value(value):
    if value.isdigit():
        return True

def negative_integer_value(value):
    if value[0] == '-' and value[1:].isdigit():
        return True

def positive_float_value(value):
    if '.' in value[1:-1] and value[1:-1].find('.') == value[1:-1].rfind('.') and value[0:value.find('.')].isdigit() and value[value.find('.')+1:].isdigit():
        return True

def negative_float_value(value):
    if value[0] == '-' and '.' in value[2:-1] and value[2:-1].find('.') == value[2:-1].rfind('.') and value[1:value.find('.')].isdigit() and value[value.find('.')+1:].isdigit():
        return True

def check_and_convert(value):
    if positive_integer_value(value) == True:
        return int(value)
    if negative_integer_value(value) == True:
        return int(value)
    if positive_float_value(value) == True:
        return float(value)
    if negative_float_value(value) == True:
        return float(value)

def none_validation(*args):
    print(args)
    if None in args:
        print('Невірно внесені дані. Спробуйте ще раз.')
        return False
    return True

def manual_convert(value1, value2):
    number1 = value1.strip()
    number2 = value2.strip()
    if number1 != '' and number2 != '':
        number1 = check_and_convert(number1)
        number2 = check_and_convert(number2)
        return number1, number2
    elif number1 == '' and number2 != '':
        number1 = None
        number2 = check_and_convert(number2)
        return number1, number2
    elif number1 != '' and number2 == '':
        number1 = check_and_convert(number1)
        number2 = None
        return number1, number2
    elif number1 == '' and number2 == '':
        number1 = None
        number2 = None
        return number1, number2

def manual_convert_one(value):
    number1 = value.strip()
    if number1 != '':
        number1 = check_and_convert(value)
        return number1


def manual_conversion():
    number1, number2 = manual_input()
    number1, number2 = manual_convert(number1, number2)
    return number1, number2

def manual_input():
    number1 = (input('Введіть перше число: '))
    number2 = (input('Введіть друге число: '))
    return number1, number2

def manual_input_step():
    number1 = (input('Введіть число: '))
    number2 = (input('Введіть показник: '))
    return number1, number2

def manual_conversion_step():
    number1, number2 = manual_input_step()
    number1, number2 = manual_convert(number1, number2)
    return number1, number2


def manual_input_factor():
    number1 = input("Введіть ціле невід'ємне число, з якого хочете визначити факторіал: ")
    return number1


def manual_conversion_factor():
    number1 = manual_input_factor()
    number1 = manual_convert_one(number1)

def manual_input_diap():
    number1 = (input('Введіть нижню границю діапазону: '))
    number2 = (input('Введіть верхню границю діапазону: '))
    return number1, number2

def manual_conversion_diap():
    number1, number2 = manual_input_diap()
    number1, number2 = manual_convert(number1, number2)
    return number1, number2


def manual_input_round():
    number1 = input('Введіть число, яке хочете округлити: ')
    return number1

def manual_conversion_round():
    number1 = manual_input_round()
    number1 = manual_convert_one(number1)
    return number1

