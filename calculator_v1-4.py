import random
import math
from validations import positive_integer_value, negative_integer_value, positive_float_value, negative_float_value, check_and_convert, none_validation, manual_convert, manual_input, manual_conversion, manual_input_step
from validations import manual_conversion_step, manual_input_factor, manual_conversion_factor, manual_convert_one, manual_input_diap, manual_conversion_diap, manual_input_round, manual_conversion_round
from calculations import addition, subtraction, multiplication, division, integer_division, modulo, power, sqrt, factor, random_number, round_number, error_text
from supermode import supermode
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
			operation = input(f'{user_name} виберіть операцію з вищезазначених: ')
			print()
			operation = operation.strip()
			if operation == '1':
				number1, number2 = manual_conversion()
				if none_validation(number1, number2):
					print(f'Результат додавання: {number1} + {number2} = {addition(number1, number2)}', '\n')
				else:
					error_text()
					continue
			if operation == '2':
				number1, number2 = manual_conversion()
				if none_validation(number1, number2):
					print(f'Результат віднімання: {number1} - {number2} = {subtraction(number1, number2)}', '\n')
				else:
					error_text()
					continue
			if operation == '3':
				number1, number2 = manual_conversion()
				if none_validation(number1, number2):
					print(f'Результат множення: {number1} * {number2} = {multiplication(number1, number2)}', '\n')
				else:
					error_text()
					continue
			if operation == '4':
				number1, number2 = manual_conversion()
				if none_validation(number1, number2) and number2 != 0:
					print(f'Результат ділення: {number1} / {number2} = {division(number1, number2)}', '\n')
				else:
					error_text()
					continue
			if operation == '5':
				number1, number2 = manual_conversion()
				if none_validation(number1, number2) and number2 != 0:
					print(f'Результат цілочисленного ділення: {number1} // {number2} = {integer_division(number1, number2)}', '\n')
				else:
					error_text()
					continue
			if operation == '6':
				number1, number2 = manual_conversion()
				if none_validation(number1, number2) and number2 != 0:
					print(f'Результат визначення остачі від ділення націло: {number1} % {number2} = {modulo(number1, number2)}', '\n')
				else:
					error_text()
					continue
			if operation == '7':
				number1, number2 = manual_conversion_step()
				if none_validation(number1, number2):
					print(f'Результат піднесення до степеню: {number1} ** {number2} = {power(number1, number2)}', '\n')
				else:
					error_text()
					continue	
			if operation == '8':
				number1, number2 = manual_conversion_step()
				if none_validation(number1, number2) and number2 != 0:
					print(f'Результат операції визначення кореня: {number1} sqrt {number2} = {sqrt(number1, number2)}', '\n')
				else:
					error_text()
					continue
			if operation == '9':
				number1 = manual_conversion_factor()
				if none_validation(number1) and number1 >= 0:
					print(f'Факторіал числа {number1} = {factor(number1)}', '\n')
				else:
					error_text()
					continue
			if operation == '10':
				number1, number2 = manual_conversion_diap()
				if none_validation(number1, number2) and number2 > number1:
					print(f'випадкове ціле число в діапазоні ({number1}:{number2}) = {random_number(number1, number2)}', '\n')
				else:
					error_text()
					continue					
			if operation == '11':
				number1 = manual_conversion_round()
				if none_validation(number1):
					print(f'після округлення {number1} отримаємо {round_number(number1)}', '\n')
				else:
					error_text()
					continue
			if operation == '12':
				while True:
					for key, value in operation_list.items():
						print(key + ' : ' + value)
					print()
					command = input('Введіть математичне рівняння: ')
					command = command.strip().lower()
					if command == 'exit':
						break
					supermode(command)
			if operation == '13':
				break

			else:
				continue
		print(f'Дякуємо {user_name} за використання калькулятора')
		break
	else:
		print("Будь-ласка, введіть своє ім'я правильно!")
		continue
