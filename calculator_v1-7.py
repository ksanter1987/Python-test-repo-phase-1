import random
import math
from calc_calculate import addition, subtraction, multiplication, division, integer_division, modulo, power, sqrt, factor, random_number, round_number, error_text, addition_valid, substraction_valid, multiplication_valid, division_valid, integer_division_valid, modulo_valid, power_validate, sqrt_validate, factor_validate, random_number_validate, round_number_validate, get_oper, addition_super, subtraction_super, multiplication_super, division_super, integer_division_super, modulo_super, power_super, sqrt_super, factor_super, random_number_super, round_number_super
from calc_validate import positive_integer_value, negative_integer_value, positive_float_value, negative_float_value, check_and_convert, none_validation, manual_convert, manual_convert_one, manual_conversion, manual_input, manual_input_step, manual_conversion_step, manual_input_factor, manual_conversion_factor, manual_input_diap, manual_conversion_diap, manual_input_round, manual_conversion_round
menu_dict ={
    '1': 'Проводимо операцію додавання',
    '2': 'Проводимо операцію віднімання',
    '3': 'Проводимо операцію множення',
    '4': 'Проводимо операцію ділення',
    '5': 'Проводимо операцію цілочисленного ділення',
    '6': 'Проводимо визначення остачі від ділення націло',
    '7': 'Проводимо операцію піднесення до степеню',
    '8': 'Проводимо операцію визначення кореня',
    '9': 'Проводимо операцію визначення факторіала',
    '10':'Виводимо випадкове ціле число в діапазоні',
    '11':'Проводимо операцію округлення числа',
    '12':'СПЕЦІАЛЬНИЙ РЕЖИМ (ручне введення операцій)',
    '13':'Вихід з програми'
} 
operation_list ={
    '+': 'Проводимо операцію додавання',
    '-': 'Проводимо операцію віднімання',
    '*': 'Проводимо операцію множення',
    '/': 'Проводимо операцію ділення',
    'intdiv': 'Проводимо операцію цілочисленного ділення',
    '%': 'Проводимо визначення остачі від ділення націло',
    'power': 'Проводимо операцію піднесення до степеню',
    'sqrt': 'Проводимо операцію визначення кореня',
    'factor': 'Проводимо операцію визначення факторіала',
    'random': 'Виводимо випадкове ціле число в діапазоні',
    'round': 'Проводимо операцію округлення числа',
    'exit': 'Вихід з програми'
}
while True:
    print('Ви використовуєте програму арифметичних обчислень КАЛЬКУЛЯТОР', '\n')
    user_name = input("Будь-ласка, введіть своє ім'я: ")
    user_name = user_name.strip().capitalize()
    if user_name.isalpha():
        print(f'Вітаємо Вас в калькуляторі {user_name}', '\n')
        while True:
            for key, value in menu_dict.items():
                print(key + ':' + value)
            print()
            menu_section = input(f'{user_name} виберіть операцію з вищезазначених: ')
            print()
            menu_func = {
            '1': addition_valid,
            '2': substraction_valid,
            '3': multiplication_valid,
            '4': division_valid,
            '5': integer_division_valid,
            '6': modulo_valid,
            '7': power_validate,
            '8': sqrt_validate,
            '9': factor_validate,
            '10': random_number_validate,
            '11': round_number_validate,
            }
            if menu_section in menu_dict and menu_section in menu_func:
                function = menu_func[menu_section]
                print(menu_dict[menu_section])
                print(function())
            elif menu_section == '12':
                while True:
                    command = input('Введіть математичне рівняння: ')
                    command = command.strip().lower()
                    left_op, operation, right_op = get_oper(command)
                    operation_func_list = {
                    '+': addition_super,
                    '-': subtraction_super,
                    '*': multiplication_super,
                    '/': division_super,
                    'intdiv': integer_division_super,
                    '%': modulo_super,
                    'power': power_super,
                    'sqrt': sqrt_super,
                    'factor': factor_super,
                    'random': random_number_super,
                    'round': round_number_super
                    }
                    if operation in operation_list and operation in operation_func_list:
                        function = operation_func_list[operation]
                        print(operation_list[operation])
                        print(function(left_op, right_op))
                    elif operation == 'exit':
                        break
                    else:
                        error_text()
                        continue                   
            elif menu_section == '13':
                break
            else:
                continue
        print(f'Дякуємо {user_name} за використання калькулятора')
        break
    else:
        print("Будь-ласка, введіть своє ім'я правильно!")
        continue