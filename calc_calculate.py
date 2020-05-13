import random
import math
from validations import positive_integer_value, negative_integer_value, positive_float_value, negative_float_value, check_and_convert, none_validation, manual_convert, manual_input, manual_conversion, manual_input_step
from validations import manual_conversion_step, manual_input_factor, manual_conversion_factor, manual_convert_one, manual_input_diap, manual_conversion_diap, manual_input_round, manual_conversion_round
from calculations import addition, subtraction, multiplication, division, integer_division, modulo, power, sqrt, factor, random_number, round_number, error_text
from supermode import supermode





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












def addition(value1, value2):
	print('Проводимо операцію додавання')
	result = value1 + value2
	return result

def subtraction(value1, value2):
	print('Проводимо операцію віднімання')
	result = value1 - value2
	return result	

def multiplication(value1, value2):
	print('Проводимо операцію множення')
	result = value1 * value2
	return result	

def division(value1, value2):
	print('Проводимо операцію ділення')
	result = value1 / value2
	return result

def integer_division(value1, value2):
	print('Проводимо операцію цілочисленного ділення')
	result = value1 // value2
	return result

def modulo(value1, value2):
	print('Проводимо визначення остачі від ділення націло')
	result = value1 % value2
	return result

def power(value1, value2 = 2):
	print('Проводимо операцію піднесення до степеню')
	result = value1 ** value2
	return result

def sqrt(value1, value2 = 2):
	print('Проводимо операцію визначення кореня')
	if value2 != 0:
		result = value1 ** (1 / value2)
		return result
	else:
		print('На нуль ділити не можна')

def factor(value1):
	print('Проводимо операцію визначення факторіала')
	result = math.factorial(int(value1))
	return result

def random_number(value1, value2):
	print('Виводимо випадкове ціле число в діапазоні')
	if value2 > value1:
		result = random.randint(int(value1), int(value2))
		return result
		
def round_number(value1):
	print('Проводимо операцію округлення числа')
	result = round(value1)
	return result

def error_text():
	print('Неправильно введене значення', '\n')


def addition_valid():
	number1, number2 = manual_conversion()
	if none_validation(number1, number2):
		print(f'Результат додавання: {number1} + {number2} = {addition(number1, number2)}', '\n')
	else:
		error_text()

def substraction_valid():
	number1, number2 = manual_conversion()
	if none_validation(number1, number2):
		print(f'Результат віднімання: {number1} - {number2} = {subtraction(number1, number2)}', '\n')
	else:
		error_text()

def multiplication_valid():
	number1, number2 = manual_conversion()
	if none_validation(number1, number2):
		print(f'Результат множення: {number1} * {number2} = {multiplication(number1, number2)}', '\n')
	else:
		error_text()

def division_valid():
	number1, number2 = manual_conversion()
	if none_validation(number1, number2) and number2 != 0:
		print(f'Результат ділення: {number1} / {number2} = {division(number1, number2)}', '\n')
	else:
		error_text()
	
def integer_division_valid():
	number1, number2 = manual_conversion()
	if none_validation(number1, number2) and number2 != 0:
		print(f'Результат цілочисленного ділення: {number1} // {number2} = {integer_division(number1, number2)}', '\n')
	else:
		error_text()	

def modulo_valid():
	number1, number2 = manual_conversion()
	if none_validation(number1, number2) and number2 != 0:
		print(f'Результат визначення остачі від ділення націло: {number1} % {number2} = {modulo(number1, number2)}', '\n')
	else:
		error_text()

def power_validate():
	number1, number2 = manual_conversion_step()
	if none_validation(number1, number2):
		print(f'Результат піднесення до степеню: {number1} ** {number2} = {power(number1, number2)}', '\n')
	else:
		error_text()

def sqrt_validate():
	number1, number2 = manual_conversion_step()
	if none_validation(number1, number2) and number2 != 0:
		print(f'Результат операції визначення кореня: {number1} sqrt {number2} = {sqrt(number1, number2)}', '\n')
	else:
		error_text()
			
def factor_validate():
	number1 = manual_conversion_factor()
	if none_validation(number1) and number1 >= 0:
		print(f'Факторіал числа {number1} = {factor(number1)}', '\n')
	else:
		error_text()

def random_number_validate():
	number1, number2 = manual_conversion_diap()
	if none_validation(number1, number2) and number2 > number1:
		print(f'випадкове ціле число в діапазоні ({number1}:{number2}) = {random_number(number1, number2)}', '\n')
	else:
		error_text()

def round_number_validate():
	number1 = manual_conversion_round()
	if none_validation(number1):
		print(f'після округлення {number1} отримаємо {round_number(number1)}', '\n')
	else:
		error_text()


def get_oper(command):
	for key in operation_list:
		if key in command and key != command[0]:
			left_op, operation, right_op = command.partition(key)
			return left_op, operation, right_op
		elif key in command and key == command[0]:
			left_op, operation, right_op = command[1:].partition(key)
			return command[0] + left_op, operation, right_op



def addition_super(value1, value2):
	number1, number2 = manual_convert(value1, value2)
	if none_validation(number1, number2):
		print(f'Результат додавання: {number1} + {number2} = {addition(number1, number2)}', '\n')
	else:
		error_text()

def subtraction_super(value1, value2):
	number1, number2 = manual_convert(value1, value2)
	if none_validation(number1, number2):
		print(f'Результат віднімання: {number1} - {number2} = {subtraction(number1, number2)}', '\n')
	else:
		error_text()

def multiplication_super(value1, value2):
	number1, number2 = manual_convert(value1, value2)
	if none_validation(number1, number2):
		print(f'Результат множення: {number1} * {number2} = {multiplication(number1, number2)}', '\n')
	else:
		error_text()

def division_super(value1, value2):
	number1, number2 = manual_convert(value1, value2)
	if none_validation(number1, number2) and number2 != 0:
		print(f'Результат ділення: {number1} / {number2} = {division(number1, number2)}', '\n')
	else:
		error_text()

def integer_division_super(value1, value2):
	number1, number2 = manual_convert(value1, value2)
	if none_validation(number1, number2) and number2 != 0:
		print(f'Результат цілочисленного ділення: {number1} // {number2} = {integer_division(number1, number2)}', '\n')
	else:
		error_text()

def modulo_super(value1, value2):
	number1, number2 = manual_convert(value1, value2)
	if none_validation(number1, number2) and number2 != 0:
		print(f'Результат визначення остачі від ділення націло: {number1} % {number2} = {modulo(number1, number2)}', '\n')
	else:
		error_text()


def power_super(value1, value2):
	number1, number2 = manual_convert(value1, value2)
	if none_validation(number1, number2):
		print(f'Результат піднесення до степеню: {number1} ** {number2} = {power(number1, number2)}', '\n')
	else:
		error_text()

def sqrt_super(value1, value2):
	if value2 != '':
		number1, number2 = manual_convert(value1, value2)
		if none_validation(number1, number2) and number2 != 0:
			print(f'Результат операції визначення кореня: {number1} sqrt {number2} = {sqrt(number1, number2)}', '\n')
		else:
			error_text()
	else:
		number1 = manual_convert_one(left_op)
		number2 = 2
		if none_validation(number1):
			print(f'Результат операції визначення кореня: {number1} sqrt {number2} = {sqrt(number1, number2)}', '\n')
		else:
			error_text()


def factor_super(value1, value2):
	if value1 == '':
		number2 = manual_convert_one(right_op)
		if none_validation(number2) and number2 >= 0:
			print(f'Факторіал числа {number2} = {factor(number2)}', '\n')
		else:
			error_text()
	else:
		error_text()


def random_number_super(value1, value2):
	number1, number2 = manual_convert(value1, value2)
	if none_validation(number1, number2) and number2 > number1:
		print(f'випадкове ціле число в діапазоні ({number1}:{number2}) = {random_number(number1, number2)}', '\n')
	else:
		error_text()


def round_number_super(value1, value2):
	if value1 == '':
		number2 = manual_convert_one(value2)
		if none_validation(number2):
			print(f'після округлення {number2} отримаємо {round_number(number2)}', '\n')
		else:
			error_text()
	else:
		error_text()




