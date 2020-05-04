import random
import math
from validations import positive_integer_value, negative_integer_value, positive_float_value, negative_float_value, check_and_convert, none_validation, manual_convert, manual_input, manual_conversion, manual_input_step, manual_conversion_step, manual_input_factor, manual_conversion_factor, manual_convert_one, manual_input_diap, manual_conversion_diap, manual_input_round, manual_conversion_round
from calculations import addition, subtraction, multiplication, division, integer_division, modulo, power, sqrt, factor, random_number, round_number, error_text
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


def supermode(command):
	for key in operation_list:
		if key in command and command[0] != '-':
			text = command.partition(key)
			if text[1] == '+':
				number1, number2 = manual_convert(text[0], text[2])
				print(f'Результат додавання: {number1} + {number2} = {addition(number1, number2)}', '\n')
			elif text[1] == '-':
				number1, number2 = manual_convert(text[0], text[2])
				print(f'Результат віднімання: {number1} - {number2} = {subtraction(number1, number2)}', '\n')
			elif text[1] == '*':
				number1, number2 = manual_convert(text[0], text[2])
				print(f'Результат множення: {number1} * {number2} = {multiplication(number1, number2)}', '\n')
			elif text[1] == '/':
				number1, number2 = manual_convert(text[0], text[2])
				if number2 != 0:
					print(f'Результат ділення: {number1} / {number2} = {division(number1, number2)}', '\n')
				else:
					error_text()
			elif text[1] == 'intdiv':
				number1, number2 = manual_convert(text[0], text[2])
				if number2 != 0:
					print(f'Результат цілочисленного ділення: {number1} // {number2} = {integer_division(number1, number2)}', '\n')
				else:
					error_text()
			elif text[1] == '%':
				number1, number2 = manual_convert(text[0], text[2])
				if number2 != 0:
					print(f'Результат визначення остачі від ділення націло: {number1} % {number2} = {modulo(number1, number2)}', '\n')
				else:
					error_text()
			elif text[1] == 'power':
				number1, number2 = manual_convert(text[0], text[2])
				print(f'Результат піднесення до степеню: {number1} ** {number2} = {power(number1, number2)}', '\n')
			elif text[1] == 'sqrt':
				if text[2] != '':
					number1, number2 = manual_convert(text[0], text[2])
					if number2 != 0:
						print(f'Результат операції визначення кореня: {number1} sqrt {number2} = {sqrt(number1, number2)}', '\n')
					else:
						error_text()
				else:
					number1 = manual_convert_one(text[0])
					number2 = 2
					print(f'Результат операції визначення кореня: {number1} sqrt {number2} = {sqrt(number1, number2)}', '\n')
			elif text[1] == 'factor':
				if text[0] == '':
					number2 = manual_convert_one(text[2])
					if number2 >= 0:
						print(f'Факторіал числа {number2} = {factor(number2)}', '\n')
					else:
						error_text()
				else:
					error_text()
			elif text[1] == 'random':
				number1, number2 = manual_convert(text[0], text[2])
				if number2 > number1:
					print(f'випадкове ціле число в діапазоні ({number1}:{number2}) = {random_number(number1, number2)}', '\n')
				else:
					error_text()
			elif text[1] == 'round':
				if text[0] == '':
					number2 = manual_convert_one(text[2])
					print(f'після округлення {number2} отримаємо {round_number(number2)}', '\n')
				else:
					error_text()
		elif key in command and command[0] == '-':
			text = command[1:].partition(key)
			if text[1] == '+':
				number1, number2 = manual_convert(command[0] + text[0], text[2])
				print(number1, type(number1))
				print(number1, type(number1))
				print(f'Результат додавання: {number1} + {number2} = {addition(number1, number2)}', '\n')
			elif text[1] == '-':
				number1, number2 = manual_convert(command[0] + text[0], text[2])
				print(f'Результат віднімання: {number1} - {number2} = {subtraction(number1, number2)}', '\n')
			elif text[1] == '*':
				number1, number2 = manual_convert(command[0] + text[0], text[2])
				print(f'Результат множення: {number1} * {number2} = {multiplication(number1, number2)}', '\n')
			elif text[1] == '/':
				number1, number2 = manual_convert(command[0] + text[0], text[2])
				if number2 != 0:
					print(f'Результат ділення: {number1} / {number2} = {division(number1, number2)}', '\n')
				else:
					error_text()
			elif text[1] == 'intdiv':
				number1, number2 = manual_convert(command[0] + text[0], text[2])
				if number2 != 0:
					print(f'Результат цілочисленного ділення: {number1} // {number2} = {integer_division(number1, number2)}', '\n')
				else:
					error_text()
			elif text[1] == '%':
				number1, number2 = manual_convert(command[0] + text[0], text[2])
				if number2 != 0:
					print(f'Результат визначення остачі від ділення націло: {number1} % {number2} = {modulo(number1, number2)}', '\n')
				else:
					error_text()
			elif text[1] == 'power':
				number1, number2 = manual_convert(command[0] + text[0], text[2])
				print(f'Результат піднесення до степеню: {number1} ** {number2} = {power(number1, number2)}', '\n')
			elif text[1] == 'sqrt':
				if text[2] != '':
					number1, number2 = manual_convert(command[0] + text[0], text[2])
					if number2 != 0:
						print(f'Результат операції визначення кореня: {number1} sqrt {number2} = {sqrt(number1, number2)}', '\n')
					else:
						error_text()
				else:
					number1 = manual_convert_one(command[0] + text[0])
					number2 = 2
					print(f'Результат операції визначення кореня: {number1} sqrt {number2} = {sqrt(number1, number2)}', '\n')
			elif text[1] == 'random':
				number1, number2 = manual_convert(text[0], text[2])
				if number2 > number1:
					print(f'випадкове ціле число в діапазоні ({number1}:{number2}) = {random_number(number1, number2)}', '\n')
				else:
					error_text()
			elif text[1] == 'round':
				if text[0] == '':
					number2 = manual_convert_one(text[2])
					print(f'після округлення {number1} отримаємо {round_number(number1)}', '\n')
				else:
					error_text()
		else:
			continue
